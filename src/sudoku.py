
class Sudoku:

    def __init__(self, size=0, rows=[]):
        """
        Constructs a puzzle of the specified size and given rows. The size is 
        the maximum value the puzzle can take; for example, typical sudoku 
        puzzles have size=9. A value of "0" in a row means "empty".
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

        # The square side is how big a "box" region is; so square_side^2 = size
        MAX_SQUARE_SIDE = 10
        MAX_SIZE = MAX_SQUARE_SIDE ** 2
        if self._size > MAX_SIZE:
            raise ValueError("Size '%s' greater than MAX_SIZE '%s'." % 
                (self._size, MAX_SIZE))

        # Make sure the size is a square
        if self._size not in [x ** 2 for x in range(MAX_SQUARE_SIDE + 1)]:
            raise ValueError("Size '%s' must be a square."%self._size)
         
        if len(self._rows) != self._size:
            raise ValueError("Number of rows '%s' must match puzzle size '%s'."
                %(self._rows, self._size))
 
        for row in self._rows:
            if len(row) != self._size:
                raise ValueError("All rows should have length '%s'; some have "
                    "length '%s'."%(self._size, len(row)))
            for value in row:
                if value > self._size:
                    raise ValueError("'%s' outside the range for a puzzle of "
                        "size '%s'."%(value, self._size)) 
                if value < 0:
                    raise ValueError("'%s' is not a valid value; must be non-"
                        "negative."%(value))

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
        return "\n".join(data) + "\n"
     

    def __str__(self):
        """
        Prints the puzzle in an easy-to-read way. Only works for sizes < 10.
        """
        
        if self._size > 9:
            return ("<puzzle has size '%s', which is too large to display>"
                %self._size)

        return "" 


#EOF

