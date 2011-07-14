
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
    simple_puzzle_as_string = os.path.join(solvertest.SolverTest.data_dir, 'puzzle-01-simple-string')

    def test_creating_object(self):
        solver.Solver()

    def test_load_a_puzzle(self):
        self._solver.load(self.simple_puzzle)

    def test_export_a_puzzle(self):
        self._solver.export(self.exported_puzzle)
        self.assertTrue(os.path.exists(self.exported_puzzle))

    def test_exported_puzzle_matches_loaded_puzzle(self):

        # Load and export a puzzle
        self._solver.load(self.simple_puzzle) 
        self._solver.export(self.exported_puzzle)

        # Read the original file (for comparison)
        file = open(self.simple_puzzle, 'rb')
        original_data = file.read()
        file.close()

        # Read the exported file (for comparison)
        file = open(self.exported_puzzle, 'rb')
        exported_data = file.read()
        file.close()

        # Test the two sets of data
        self.assertEqual(original_data, exported_data,
            "The exported file doesn't match the original.")

    def test_get_current_puzzle_string_gives_right_string(self):
        self._solver.load(self.simple_puzzle)
        puzzle_string = self._solver.getCurrentPuzzleString()

        file = open(self.simple_puzzle_as_string)
        correct_puzzle_string = file.read()
        file.close()

        self.assertEqual(puzzle_string, correct_puzzle_string,
            "The solver gave the wrong puzzle string.")

        
#EOF

