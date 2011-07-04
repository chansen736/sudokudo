
# ModuleUnderTest imports
import solver

# Imports
import os
import shutil
import sudokudotest

class SolverTest(sudokudotest.SudokuDoTest):

    _solver = None

    data_dir = 'data'
    tmp_dir = 'tmp'

    def setUp(self):
        self._solver = solver.Solver()
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir) 
        os.mkdir(self.tmp_dir)

#EOF

