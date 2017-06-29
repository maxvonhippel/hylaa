'''
Generalized Star and other Star data structures
Stanley Bak
Aug 2016
'''

import math
import time

import numpy as np
from numpy import array_repr
from numpy.linalg import lstsq
from numpy.testing import assert_array_almost_equal

from hylaa.glpk_interface import LpInstance
from hylaa.hybrid_automaton import HyperRectangle, LinearAutomatonTransition
from hylaa.hybrid_automaton import LinearAutomatonMode, SparseLinearConstraint
from hylaa.timerutil import Timers as Timers
from hylaa.util import Freezable
from hylaa.starutil import GuardOptData, InitParent
from hylaa.containers import PlotSettings, HylaaSettings
from hylaa.time_elapse import TimeElapser

class Star(Freezable):
    '''
    A representation of a set of continuous states. Contains logic for plotting that states if
    requested in the settings.
    '''

    def __init__(self, hylaa_settings, constraint_list, mode):

        assert len(constraint_list) > 0
        assert isinstance(hylaa_settings, HylaaSettings)

        self.settings = hylaa_settings

        assert isinstance(mode, LinearAutomatonMode)
        self.mode = mode # the LinearAutomatonMode
        self.dims = mode.parent.dims

        self.time_elapse = TimeElapser(mode, hylaa_settings)

        for lc in constraint_list:
            assert isinstance(lc, SparseLinearConstraint), "constraint_list should be a list SpraseLinearConstraints"
            assert lc.vector.shape[1] == self.dims, \
                "each star's constraint's size should match dims. {} length is not {}".format(lc, self.dims)

        self.constraint_list = [c.clone() for c in constraint_list] # copy constraints

        self.total_steps = 0

        ###################################
        ## private member initialization ##
        ###################################
        self._plot_lpi = None # LpInstance for plotting
        #self._guard_opt_data = GuardOptData(self) # contains LP instance(s) for guard checks
        self._verts = None # for plotting optimization, a cached copy of this star's projected polygon verts

        self.freeze_attrs()

    def get_plot_lpi(self):
        'get (maybe create) the LpInstance object for this star, and return it'

        assert self.time_elapse.cur_time_elapse_mat is not None

        rv = self._plot_lpi

        if rv is None:
            rv = LpInstance(2, self.dims)

            for lc in self.constraint_list:
                rv.add_init_constraint(lc.vector, lc.value)

            rv.update_time_elapse_matrix(self.time_elapse.cur_time_elapse_mat[:2])

            self._plot_lpi = rv

        return rv

    def step(self):
        'update the star based on values from a new simulation time instant'

        self.time_elapse.step()

        Timers.tic('star.step-update-lp')

        if self._plot_lpi is not None:
            self._plot_lpi.update_time_elapse_matrix(self.time_elapse.cur_time_elapse_mat[:2])

        self._verts = None # cached vertices for plotting are no longer valid

        #Timers.tic('guard_opt_data.update_from_sim')
        #self._guard_opt_data.update_from_sim(input_star)
        #Timers.toc('guard_opt_data.update_from_sim')

        Timers.toc('star.step-update-lp')

    ######### star plotting methods below ############

    # global
    plot_vecs = None # list of vectors to optimize in for plotting, assigned in Star.init_plot_vecs
    plot_settings = None # assigned in Star.init_plot_vecs
    high_vert_mode = False # reduce plotting directions if the set has lots of verticies (drawing optimization)

    @staticmethod
    def init_plot_vecs(plot_settings):
        'initialize plot_vecs'

        Star.plot_settings = plot_settings
        Star.plot_vecs = []

        assert plot_settings.num_angles >= 3, "needed at least 3 directions in plot_settings.num_angles"

        step = 2.0 * math.pi / plot_settings.num_angles

        for theta in np.arange(0.0, 2.0*math.pi, step):
            x = math.cos(theta)
            y = math.sin(theta)

            vec = np.array([x, y], dtype=float)

            Star.plot_vecs.append(vec)

    def verts(self):
        'get the verticies of the polygon projection of the star used for plotting'

        assert Star.plot_settings is not None, "init_plot_vecs() should be called before verts()"

        if self._verts is None:
            use_binary_search = True

            if Star.high_vert_mode:
                use_binary_search = False

            pts = self._find_star_boundaries(use_binary_search=use_binary_search)

            if len(pts) > len(Star.plot_vecs)/2 and not Star.high_vert_mode:
                # don't use binary search anymore, and reduce the number of directions being plotted

                Star.high_vert_mode = True
                new_vecs = []

                if len(Star.plot_vecs) > 32:
                    for i in xrange(len(Star.plot_vecs)):
                        if i % 4 == 0:
                            new_vecs.append(Star.plot_vecs[i])

                    Star.plot_vecs = new_vecs

            verts = [[pt[0], pt[1]] for pt in pts]

            # wrap polygon back to first point
            verts.append(verts[0])

            self._verts = verts

        return self._verts

    def _binary_search_star_boundaries(self, start, end, start_point, end_point):
        '''
        return all the optimized points in the star for the passed-in directions, between
        the start and end indices, exclusive

        points which match start_point or end_point are not returned
        '''

        star_lpi = self.get_plot_lpi()

        dirs = Star.plot_vecs
        rv = []

        if start + 1 < end:
            mid = (start + end) / 2
            mid_point = np.zeros(2)

            star_lpi.minimize(dirs[mid], mid_point, error_if_infeasible=True)

            not_start = not np.array_equal(start_point, mid_point)
            not_end = not np.array_equal(end_point, mid_point)

            if not_start:
                rv += self._binary_search_star_boundaries(start, mid, start_point, mid_point)

            if not_start and not_end:
                rv.append(mid_point)

            if not np.array_equal(end_point, mid_point):
                rv += self._binary_search_star_boundaries(mid, end, mid_point, end_point)

        return rv

    def _find_star_boundaries(self, use_binary_search=True):
        '''
        find a constaint-star's boundaries using Star.plot_vecs. This solves several LPs and
        returns a list of points on the boundary (in the standard basis) which maximize each
        of the passed-in directions
        '''

        star_lpi = self.get_plot_lpi()

        point = np.zeros(2)
        direction_list = Star.plot_vecs
        rv = []

        assert len(direction_list) > 2

        if not use_binary_search:
            # straightforward approach: minimize in each direction
            last_point = None

            for direction in direction_list:
                star_lpi.minimize(direction, point, error_if_infeasible=True)

                if last_point is None or not np.array_equal(point, last_point):
                    last_point = point.copy()
                    rv.append(point)
        else:
            # optimized approach: do binary search to find changes
            star_lpi.minimize(direction_list[0], point, error_if_infeasible=True)
            rv.append(point.copy())

            # add it in thirds, to ensure we don't miss anything
            third = len(direction_list) / 3

            # 0 to 1/3
            star_lpi.minimize(direction_list[third], point, error_if_infeasible=True)

            if not np.array_equal(point, rv[-1]):
                rv += self._binary_search_star_boundaries(0, third, rv[-1], point)
                rv.append(point.copy())

            # 1/3 to 2/3
            star_lpi.minimize(direction_list[2*third], point, error_if_infeasible=True)

            if not np.array_equal(point, rv[-1]):
                rv += self._binary_search_star_boundaries(third, 2*third, rv[-1], point)
                rv.append(point.copy())

            # 2/3 to end
            star_lpi.minimize(direction_list[-1], point, error_if_infeasible=True)

            if not np.array_equal(point, rv[-1]):
                rv += self._binary_search_star_boundaries(2*third, len(direction_list) - 1, rv[-1], point)
                rv.append(point.copy())

        # pop last point if it's the same as the first point
        if len(rv) > 1 and np.array_equal(rv[0], rv[-1]):
            rv.pop()

        return rv
