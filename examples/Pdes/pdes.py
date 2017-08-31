"""This module contains methods for producing ODEs from PDEs"""
from __future__ import division
import copy
from scipy.sparse import csr_matrix
from scipy import sparse
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
import numpy as np
import math

class HeatEquationOneDimension(object):
    """Generate ODEs from 1-d diffusion heat equation"""

    # consider 1-d diffusion problem
    # boundary conditions (BCs): u(0,t) = u0 in range [a, b]; u(len_x, t) = uN in range [c, d]
    # initial condition (IC): u(x,0) = 0
    # no heat source

    # todo: generate ODEs of 1-d diffusion equation with heat source: u_t = a*u_xx + u(x,t)
    # where heat source position is given
    # first element in heat_source_pos array is where heat source start
    # second element in heat_source_pos array is where heat source end
    
    def __init__(self, diffusity_const, len_x, has_heat_source, heat_source_pos):
        self.diffusity_const = diffusity_const if diffusity_const > 0 else 0 # diffusity constant
        self.len_x = len_x if len_x > 0 else 0 # length along x-axis
        if self.diffusity_const == 0 or self.len_x == 0:
            raise ValueError('inappropriate parameters')
        self.has_heat_source = has_heat_source
        assert isinstance(heat_source_pos, np.ndarray), "heat_source_pos is not an array"
        if heat_source_pos.shape[0] != 2:
            raise ValueError('heat_source_pos should be an array with shape (2,)')
        else:
            self.heat_source_pos = heat_source_pos # shoule be somewhere between 0 and len_x

    def get_odes(self, num_mesh_point):
        'Generate linear state space model dot(x) = Ax + Bu'

        # method returns matrix A and B in the form of csr sparse matrices

        if num_mesh_point <= 0: # number of mesh point between x = 0 and x = len_x
            raise ValueError('num_mesh_point <= 0')
        else:
            disc_step = float((self.len_x)/(num_mesh_point +1)) # discretization step
            alpha = self.diffusity_const/disc_step**2

            print "\ndiscretization step: {}".format(disc_step)
            print "\nnumber of mesh point: {}".format(num_mesh_point)
            print "\nlength of grid: {}".format(self.len_x)
            print "\nalpha: {}".format(alpha)

            data_start = np.array([-2, 1])
            data_end = np.array([1, -2])
            data_middle = np.array([1, -2, 1])

            # fill data
            data = copy.copy(data_start)
            for i in xrange(0, num_mesh_point):

                if i == num_mesh_point - 1 and i > 0:
                    data = np.append(data, data_end)
                elif i > 0:
                    data = np.append(data, data_middle)

            data = alpha*data

            # fill index pointer
            indptr = np.zeros((num_mesh_point + 1,), dtype=np.int64)
            indptr[0] = 0
            for i in xrange(1, num_mesh_point + 1):
                if i == 1 or i == num_mesh_point:
                    indptr[i] = indptr[i-1] + 2
                else:
                    indptr[i] = indptr[i-1] + 3

            # number of nonzeros 
            if num_mesh_point <= 2:
                nnz = 2*num_mesh_point
            else:
                nnz = 4 + (num_mesh_point-2)*3

            # fill indices
            indices = np.zeros((nnz,), dtype = np.int64) # indices of csr matrix
            for i in xrange(0, num_mesh_point):
                j = indptr[i+1] - 1
                if j < nnz - 1:
                    indices[j] = i+1
                else:
                    indices[j] = i
                while j > indptr[i]:
                    j = j -1
                    indices[j] = indices[j+1] - 1

            matrix_a = csr_matrix((data, indices, indptr), shape=(num_mesh_point, num_mesh_point))

            # get matrix_b which may be related to heat source

            if not self.has_heat_source:
                z = np.zeros((num_mesh_point, 2))
                z[0, 0] = alpha
                z[num_mesh_point-1, 1] = alpha

                matrix_b = sparse.csr_matrix(z) # no heat source
            else:
                heat_start_pos = int(math.ceil(self.heat_source_pos[0]/disc_step))
                heat_end_pos = int(math.ceil(self.heat_source_pos[1]/disc_step))
                print "\nheat source is supplied from mesh point x_{} to mesh point x_{}"\
                  .format(heat_start_pos, heat_end_pos)
                z = np.zeros((num_mesh_point, 3))
                z[0, 0] = alpha
                z[num_mesh_point - 1, 1] = alpha
                z[heat_start_pos-1:heat_end_pos, 2] = 1

                matrix_b = sparse.csr_matrix(z)

            return matrix_a, matrix_b

class HeatEquationTwoDimensions(object):
    """Generate ODEs from 2-d Heat equation"""

    # We consider the 2-d heat diffusion equation on a rectangle metal plate with the form:
    # u_t = alpha*(u_xx + u_yy) + q(t)
    # q(t) is the heat source
    # we assume the following boundary conditions (BCs):
    # BC1: u(x,0,t) = 0, BC2: u(x, len_y, t) = 0, BC3: u(0,y,t) = 0
    # In the right side of the metal plate, the heat is exchanged with the environment
    # The boundary condition for the right hand side is: BC4:  u_x(len_x,y,t) = -k*[u(len_x,y,t) - g(t)]
    # k is the heat_lost_constant and g(t) is environment temperature, c1 <= g(t) <= c2
    # The BC4 shows that the metal plate lost its heat linearly to the environment

    # we assume the following initial condition (IC): u(x,y,0) = 0

    def __init__(self, diffusity_const, heat_exchange_coeff, thermal_cond, \
                     len_x, len_y, has_heat_source, heat_source_pos):
        self.diffusity_const = diffusity_const if diffusity_const > 0 else 0 # diffusity constant
        self.heat_exchange_coeff = heat_exchange_coeff if heat_exchange_coeff > 0 else 0 # heat exchange coefficient
        self.thermal_cond = thermal_cond if thermal_cond > 0 else 0 # thermal conductivity
        self.len_x = len_x if len_x > 0 else 0 # length x
        self.len_y = len_y if len_y > 0 else 0 # length y

        if self.diffusity_const == 0 or self.heat_exchange_coeff == 0 or \
          self.thermal_cond == 0 or  self.len_x == 0 or self.len_y == 0:
            raise ValueError("inappropriate parameters")
        self.heat_lost_const = self.thermal_cond/self.heat_exchange_coeff

        self.has_heat_source = has_heat_source
        assert isinstance(heat_source_pos, np.ndarray), "heat source pos is not an ndarray"
        if heat_source_pos.shape != (2, 2):
            raise ValueError("heat source position is not 2x2 array")
        if heat_source_pos[0, 0] < 0 or heat_source_pos[0, 1] > self.len_x or \
                heat_source_pos[1, 0] < 0 or heat_source_pos[1, 1] > self.len_y:
            raise ValueError("Heat source position value error")
        self.heat_source_pos = heat_source_pos # an array to indicate the position of heat source
        # heat_source_pos = ([[x_start, x_end], [y_start, y_end]])

    def get_odes(self, num_x, num_y):
        'obtain the linear model of 2-d heat equation'

        assert isinstance(num_x, int), "number of mesh point should be an integer"
        assert isinstance(num_y, int), "number of messh point should be an integer"

        if num_x <= 0 or num_y <= 0:
            raise ValueError('number of mesh points should be larger than zero')

        disc_step_x = self.len_x/num_x # dicrezation step along x axis
        disc_step_y = self.len_y/num_y # discrezation step along y axis

        if self.has_heat_source:
            heat_start_pos_x = int(math.ceil(self.heat_source_pos[0, 0]/disc_step_x))
            heat_end_pos_x = int(math.ceil(self.heat_source_pos[0, 1]/disc_step_x))
            heat_start_pos_y = int(math.ceil(self.heat_source_pos[1, 0]/disc_step_y))
            heat_end_pos_y = int(math.ceil(self.heat_source_pos[1, 1]/disc_step_y))

            print "\nheat source is from point {} to point {} on x-axis".\
              format(heat_start_pos_x, heat_end_pos_x)
            print "\nheat source is from point {} to point {} on y-axis".\
              format(heat_start_pos_y, heat_end_pos_y)

        # we use explicit semi- finite-difference method to obtain the
        # linear model of heat equation

        num_var = num_x*num_y # number of discrezation variables
        # changing the sparsity structure of a csr_matrix is expensive. lil_matrix is more efficient
        matrix_a = sparse.lil_matrix((num_var, num_var))
        matrix_b = sparse.lil_matrix((num_var, 2))
        a = 1/disc_step_x**2
        b = 1/disc_step_y**2
        c = -2*(a+b)
        k = self.heat_lost_const
        step_x = disc_step_x

        # fill matrix_a

        for i in xrange(0, num_var):
            matrix_a[i, i] = c # filling diagonal
            x_pos = i%num_x # x-position corresponding to i-th state variable
            y_pos = int((i - x_pos)/num_x) # y-position corresponding to i-th variable

            # fill along x - axis
            if x_pos - 1 >= 0:
                matrix_a[i, i-1] = a
            if x_pos + 1 <= num_x -1:
                matrix_a[i, i+1] = a
            else:
                # fill diffusion term
                matrix_a[i, i] = matrix_a[i, i] + 1/(1+k*step_x)
                matrix_b[i, 0] = (k*step_x)/(1+k*step_x)
            # fill along y-axis
            if y_pos - 1 >= 0:
                matrix_a[i, (y_pos-1)*num_x + x_pos] = b

            if y_pos + 1 <= num_y - 1:
                matrix_a[i, (y_pos+1)*num_x + x_pos] = b

            # fill heat source
            if x_pos >= heat_start_pos_x and x_pos <= heat_end_pos_x and y_pos >= heat_start_pos_y and \
                y_pos <= heat_end_pos_y:
                matrix_b[i, 1] = 1

        return matrix_a.tocsr(), matrix_b.tocsr()

def sim_odeint_sparse(sparse_a_matrix, init_vec, input_vec, step, num_steps):
    'use odeint and keep the A matrix sparse'

    num_dims = sparse_a_matrix.shape[0]
    times = np.linspace(0, step, num_steps)

    def der_func(state, _):
        'linear derivative function'

        rv = np.array(sparse_a_matrix * state) + input_vec
        rv.shape = (num_dims,)

        return rv

    start = time.time()
    result = odeint(der_func, init_vec, times)
    runtime = time.time() - start

    return runtime, result


def test_1d():
    'test 1-d heat equation'
    len_x = 1
    diffusity_const = 0.1
    has_heat_source = True
    heat_source_pos = np.array([0.3, 0.5])
    he = HeatEquationOneDimension(diffusity_const, len_x, has_heat_source, heat_source_pos)
    matrix_a, matrix_b = he.get_odes(10)
    print "\nmatrix_a:\n{}".format(matrix_a.toarray())
    print "\nmatrix_b:\n{}".format(matrix_b.toarray())

def test_2d():
    'test 2-d heat equation'

    # parameters
    diffusity_const = 0.1
    heat_exchange_coeff = 1
    thermal_cond = 1
    len_x = 1
    len_y = 1
    has_heat_source = True
    heat_source_pos = np.array([[0, 0.4], [0, 1]])

    he = HeatEquationTwoDimensions(diffusity_const, heat_exchange_coeff, thermal_cond,\
                                   len_x, len_y, has_heat_source, heat_source_pos)

    # get linear ode model of 2-d heat equation
    num_x = 10 # number of discretized steps between 0 and len_x
    num_y = 10 # number of discretized steps between 0 and len_y
    matrix_a, matrix_b = he.get_odes(num_x, num_y)
    print "\nmatrix_a :\n{}".format(matrix_a.todense())
    print "\nmatrix_b :\n{}".format(matrix_b.todense())

    # simulate the linear ode model of 2-d heat equation
    
    heat_source = 1 # the value of heat source is 1 degree celcius 
    envi_temp = 0   # environment temperature is 0 degree celcius
    inputs = np.array([envi_temp, heat_source]) # input to linear ode model

    print "\ninputs to the odes including heat_source = {} and environment temperature = {}".\
      format(heat_source, envi_temp)

    input_vec = matrix_b*inputs
    print "\input vector v = matrix_b*inputs is: \n{}".format(input_vec)

    init_vec = np.zeros((matrix_a.shape[0]),)
    step = 0.3
    num_steps = 1000000
    times = np.linspace(0, step, num_steps)
    runtime, result = sim_odeint_sparse(matrix_a, init_vec, input_vec, step, num_steps)

    print "\n the result is: \n{}".format(result)
    print "\n result shape is: \n{}".format(result.shape)
    
    # plot the result

    # plot the center point temperature
    center_point_pos_x = int(math.ceil(num_x/2)) - 1
    center_point_pos_y = int(math.ceil(num_y/2)) - 1

    center_point_state_pos = center_point_pos_y*num_x + center_point_pos_x
    print "\ncenter_point corresponds to the {}-th state variable".format(center_point_state_pos)

    center_point_temp = result[:, center_point_state_pos]
    plt.plot(times, center_point_temp, 'b', label = 'center_point')
    plt.legend(loc = 'best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

    # plot all points in 3-d
    
    
    
    
    
if __name__ == '__main__':
    #test_1d()
    test_2d()