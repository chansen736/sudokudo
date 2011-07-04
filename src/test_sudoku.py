
# Test imports
import sudokutest

# Module-Under-Test imports
import sudoku

import unittest
unittest.TestCase.longMessage = True

class test_sudoku(sudokutest.SudokuTest):

    def test_creating_objec(self):
        sudoku.Sudoku()


    def test_creating_constructor(self):
        sudoku.Sudoku(size=2, rows=["0 0","0 0"])

    def test_constructor_stores_data_correctly(self):
        puzzle = sudoku.Sudoku(size=2, rows=["1 2","2 1"])
        self.assertEqual(puzzle._size, 2,
            "Puzzle isn't storing size correctly.")
        self.assertEqual(puzzle._rows, [[1,2],[2,1]],
            "Puzzle isn't storing rows correctly.")  
   

    def test_constructor_validates_rows(self):
        # Test values above range
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=2, rows=["1 2", "3 1"])

        # Test values below range
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=2, rows=["1 -1", "2 1"])

        # Test too many rows
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=2, rows=["1 2", "2 1", "1 2"])

        # Test too few rows
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=2, rows=["1 2"])

        # Test too many columns
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=2, rows=["1 2", "2 1 2"])

        # Test too few columns
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=2, rows=["1 2", "2"])


#EOF

