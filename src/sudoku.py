
class Sudoku:

    def __init__(self, size=0, rows=[]):
        """
        Constructs a puzzle of the specified size and given rows. The size is the maximum value the puzzle can take; for example, typical sudoku puzzles have size=9. A value of "0" in a row means "empty".
        """
        self._size = size
        self._rows = []
        for row in rows:
            self._rows.append(map(int, row.split()))
        self._validateRows()


    def _validateRows(self):
        """
        Throws an error if the puzzle is in an invalid state.
        """
        if len(self._rows) != self._size:
            raise ValueError("Number of rows '%s' must match puzzle size '%s'."%(self._rows, self._size))
 
        for row in self._rows:
            if len(row) != self._size:
                raise ValueError("All rows should have length '%s'; some have length '%s'."%(self._size, len(row)))
            for value in row:
                if value > self._size:
                    raise ValueError("'%s' outside the range for a puzzle of size '%s'."%(value, self._size)) 
                if value < 0:
                    raise ValueError("'%s' is not a valid value; must be non-negative."%(value))

    def export(self):
        """
        Exports the puzzle data with the format:
        
        <size>
        <row1>
        ...
        <rowN>
        """

        # The size is the first row
        data = [ str(self._size) ]
 
        # The values, joined by spaces, are each row
        for row in self._rows:
            data.append(" ".join(map(str, row)))

        # The result is joined by newlines
        return "\n".join(data)
     
 
#EOF

