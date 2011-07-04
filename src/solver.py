import sudoku

class Solver:
    
    def __init__(self):
        self._puzzle = sudoku.Sudoku()
    
    def load(self, filename):
        pass


    def export(self, filename):
        """
        Exports the current puzzle to a file.
        """

        f_out = open(filename, 'wb')
        f_out.write("woof\n")
        f_out.close() 


#EOF

