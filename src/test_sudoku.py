
# Test imports
import sudokutest

# Module-Under-Test imports
import sudoku

import unittest
unittest.TestCase.longMessage = True

class test_sudoku(sudokutest.SudokuTest):

    ROWS_4 = ["1 2 3 4",
              "3 4 1 2",
              "2 1 4 3",
              "4 3 2 1"]

    def test_creating_objec(self):
        sudoku.Sudoku()


    def test_creating_constructor(self):
        sudoku.Sudoku(size=4, 
                      rows=["0 0 0 0" for x in range(4)])

    def test_constructor_stores_data_correctly(self):
        puzzle = sudoku.Sudoku(size=len(self.ROWS_4), rows=self.ROWS_4)

        self.assertEqual(puzzle._size, 4,
            "Puzzle isn't storing size correctly.")
        
        self.assertEqual(puzzle._square_side, 2,
            "Puzzle isn't storing square side correctly.")
        
        # Rows should be stored as a a matrix of the values in the original 
        # string
        self.assertEqual(puzzle._rows, [ [int(x) for x in row.split()]
                                         for row in self.ROWS_4],
            "Puzzle isn't storing rows correctly.")  


    def test_constructor_validates_rows(self):
        # Test values above range
        rows = ["5 2 3 4",
                "3 4 1 2",
                "2 1 4 3",
                "4 3 2 1"]
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=4, rows=rows)

        # Test values below range
        rows = ["-1 2 3 4",
                "3 4 1 2",
                "2 1 4 3",
                "4 3 2 1"]
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=4, rows=rows)

        # Test too many rows
        rows = ["1 2 3 4",
                "3 4 1 2",
                "2 1 4 3",
                "2 1 4 3",
                "0 0 0 0"]
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=4, rows=rows)

        # Test too few rows
        rows = ["1 2 3 4",
                "2 1 4 3",
                "4 3 2 1"]
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=4, rows=rows)

        # Test too many columns
        rows = ["1 2 3 4",
                "3 4 1 2",
                "2 1 4 3 0",
                "4 3 2 1"]
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=4, rows=rows)

        # Test too few columns
        rows = ["1 2 3 4",
                "3 4 1",
                "2 1 4 3",
                "4 3 2 1"]
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=4, rows=rows)


    def test_constructor_forces_size_to_be_a_square(self):
        with self.assertRaises(ValueError):
            sudoku.Sudoku(size=3, rows=["1 2 3", "2 3 1", "3 1 2"])


    def test_export_has_right_output(self):
        rows = ["1 2 3 4",
                "3 4 1 2",
                "2 1 4 3",
                "4 3 2 1"]
        puzzle = sudoku.Sudoku(size=len(rows), rows=rows)
        exported_data = puzzle.export()
        self.assertEqual(exported_data, 
                         "4\n1 2 3 4\n3 4 1 2\n2 1 4 3\n4 3 2 1\n",
                         "Exported puzzle data is wrong.")


    def test_large_puzzles_have_nice_error_when_getting_str(self):
        rows=[ " ".join(["0" for x in range(16)]) for x in range(16) ]
        puzzle = sudoku.Sudoku(size=16, rows=rows)
        self.assertEqual(str(puzzle), 
            "<puzzle has size '16', which is too large to display>") 


    def test_str_works(self):
        rows=["1 2 3 4","3 4 1 2","2 1 4 3","4 3 2 1"]
        puzzle = sudoku.Sudoku(size=len(rows), rows=rows)
        self.assertEqual(str(puzzle), """
+---+---+
|1 2|3 4|
|3 4|1 2|
+---+---+
|2 1|4 3|
|4 3|2 1|
+---+---+
""".strip(), "The puzzle doesn't str() properly."
 )


#EOF

