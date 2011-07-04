
# Test imports
import solvertest

# Module-Under-Test imports
import solver

# Imports
import filecmp
import os.path

class test_solver(solvertest.SolverTest):

    simple_puzzle = os.path.join(solvertest.SolverTest.data_dir, 'puzzle-01-simple')
    exported_puzzle = os.path.join(solvertest.SolverTest.tmp_dir, 'exported_puzzle')

    def test_creating_object(self):
        solver.Solver()

    def test_load_a_puzzle(self):
        self._solver.load(self.simple_puzzle)

    def test_export_a_puzzle(self):
        self._solver.export(self.exported_puzzle)
        self.assertTrue(os.path.exists(self.exported_puzzle))

    def test_exported_puzzle_matches_loaded_puzzle(self):
        self._solver.load(self.simple_puzzle) 
        self._solver.export(self.exported_puzzle)
        self.assertTrue(filecmp.cmp(self.simple_puzzle, self.exported_puzzle),
            "The exported file doesn't match the original.")
        
#EOF

