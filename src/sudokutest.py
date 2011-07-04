
# ModuleUnderTest imports
import sudoku

# Imports
import sudokudotest

class SudokuTest(sudokudotest.SudokuDoTest):

    _sudoku = None

    def SetUp(self):
        self._sudoku = sudoku.sudoku()

#EOF

