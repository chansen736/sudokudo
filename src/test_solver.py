
# Test imports
import SolverTest

# Module-Under-Test imports
import solver

class test_solver(SolverTest.SolverTest):

    def test_creating_object(self):
        solver.solver()

    def test_load_a_puzzle(self):
        self._solver.load(self.data_dir + '/puzzle-01-simple')

    def test_export_a_puzzle(self):
        self._solver.export(self.tmp_dir + '/exported_puzzle')
 
#EOF

