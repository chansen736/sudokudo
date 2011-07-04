
class Sudoku:

    def __init__(self, size=0, rows=[]):
        self._size = size
        self._rows = []
        for row in rows:
            self._rows.append(map(int, row.split()))
        self._validateRows()

    def _validateRows(self):
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

#EOF

