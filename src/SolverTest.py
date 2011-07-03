
# Test imports
import unittest

# ModuleUnderTest imports
import solver

class SolverTest(unittest.TestCase):

    _solver = None

    data_dir = 'data'
    tmp_dir = 'tmp'

    def setUp(self):
        self._solver = solver.solver()
        #TODO: remove the tmp_dir directory

#EOF

