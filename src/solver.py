import sudoku

class Solver:
    
    def __init__(self):
        self._puzzle = sudoku.Sudoku()
    
    def load(self, filename):
        """
        Reads a puzzle from a file. The file is of the format:
        
        <size of puzzle: N>
        <row1 of puzzle>
        ...
        <rowN of puzzle>

        """
        f_in = open(filename, 'rb')
        
        # The first line should be the size of the puzzle
        puzzle_size = int(f_in.readline())

        # The rest of the lines are the data
        puzzle_data = f_in.readlines()

        self._puzzle = sudoku.Sudoku(size=puzzle_size, rows=puzzle_data)

        f_in.close() 


    def export(self, filename):
        """
        Exports the current puzzle to a file.
        """

        f_out = open(filename, 'wb')
        f_out.write(self._puzzle.export())
        f_out.close() 


    def getCurrentPuzzleString(self):
        """
        Returns a string representing the solved portion of the puzzle.
        """
        
        return ""


#EOF

