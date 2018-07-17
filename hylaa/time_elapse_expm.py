'''
Time-elapse object for matrix exponential and expm-mul methods

Stanley Bak
April 2018
'''

from scipy.sparse import csc_matrix
from scipy.sparse.linalg import expm, expm_multiply

import numpy as np

from hylaa.util import Freezable
from hylaa.timerutil import Timers

class TimeElapseExpmMult(Freezable):
    'container object for expm + matrix-vec mult method'

    def __init__(self, time_elapser):
        self.time_elapser = time_elapser
        self.a_csc = csc_matrix(time_elapser.mode.a_csr)
        self.b_csc = None if time_elapser.mode.b_csr is None else csc_matrix(time_elapser.mode.b_csr)
        self.dims = time_elapser.dims

        self.cur_step = 0
        self.cur_basis_matrix = None
        self.cur_input_effects_matrix = None

        self.one_step_matrix_exp = None # one step matrix exponential
        self.one_step_input_effects_matrix = None # one step input effects matrix, if inputs exist

        self.freeze_attrs()

    def init_matrices(self):
        'initialize the one-step basis and input effects matrices'

        dims = self.dims
        Timers.tic('expm')
        self.one_step_matrix_exp = expm(self.a_csc * self.time_elapser.step_size)
        Timers.toc('expm')

        Timers.tic('toarray')
        self.one_step_matrix_exp = self.one_step_matrix_exp.toarray()
        Timers.toc('toarray')

        if self.b_csc is not None:
            self.one_step_input_effects_matrix = np.zeros(self.b_csc.shape, dtype=float)

            for c in range(self.time_elapser.inputs):
                # create the a_matrix augmented with a column of the b_matrix as an affine term
                indptr = self.b_csc.indptr

                data = np.concatenate((self.a_csc.data, self. b_csc.data[indptr[c]:indptr[c+1]]))
                indices = np.concatenate((self.a_csc.indices, self.b_csc.indices[indptr[c]:indptr[c+1]]))
                indptr = np.concatenate((self.a_csc.indptr, [len(data)]))

                aug_a_csc = csc_matrix((data, indices, indptr), shape=(dims + 1, dims + 1))

                mat = aug_a_csc * self.time_elapser.step_size

                # the last column of matrix_exp is the same as multiplying it by the initial state [0, 0, ..., 1]
                init_state = np.zeros(dims + 1, dtype=float)
                init_state[dims] = 1.0
                col = expm_multiply(mat, init_state)

                self.one_step_input_effects_matrix[:, c] = col[:dims]

    def assign_basis_matrix(self, step_num):
        'first step matrix exp, other steps matrix multiplication'

        print(". remove debugging printing (step = {})".format(step_num))

        Timers.tic('init_matrices')
        if self.one_step_matrix_exp is None:
            self.init_matrices()
        Timers.toc('init_matrices')

        if step_num == 0: # step zero, basis matrix is identity matrix
            self.cur_basis_matrix = np.identity(self.dims, dtype=float)
            self.cur_input_effects_matrix = None
            print(". doing step 0")
        elif step_num == 1:
            self.cur_basis_matrix = self.one_step_matrix_exp
            self.cur_input_effects_matrix = self.one_step_input_effects_matrix
            print(". doing step 1")
        elif step_num == self.cur_step + 1:
            print(". doing quick step")
            Timers.tic('quick_step')
            self.cur_basis_matrix = np.dot(self.cur_basis_matrix, self.one_step_matrix_exp)

            # inputs
            if self.b_csc is not None:
                self.cur_input_effects_matrix = np.dot(self.one_step_matrix_exp, self.cur_input_effects_matrix)

            Timers.toc('quick_step')
        else:
            print(". doing slow step, step_num desired was {}, cur_step = {}".format(step_num, self.cur_step))
            Timers.tic('slow_step')

            Timers.tic('expm')
            mat_exp = expm(self.a_csc * step_num)
            Timers.toc('expm')

            Timers.tic('toarray')
            self.cur_basis_matrix = mat_exp.toarray()
            Timers.toc('toarray')

            # inputs
            if self.b_csc is not None:
                Timers.tic("input effects")
                self.cur_input_effects_matrix = (mat_exp * self.one_step_input_effects_matrix).toarray()
                Timers.toc("input effects")

            Timers.toc('slow_step')

        self.cur_step = step_num
