
# Test imports
import unittest

# ModuleUnderTest imports
import sudoku

class SudokuTest(unittest.TestCase):

    _sudoku = None

    def SetUp(self):
        self._sudoku = sudoku.sudoku()

#EOF

