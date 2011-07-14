import math

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
 
        # Now that the basic data is validated, we can compute additional values
        self._square_side = int(size ** 0.5)


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

        Should look like:
        +---+---+
        |1 2|3 4|
        |3 4|1 2|
        +---+---+
        |2 1|4 3|
        |4 3|2 1|
        +---+---+
        """
        
        if self._size > 9:
            return ("<puzzle has size '%s', which is too large to display>"
                %self._size)

        # Do some shortcut creation
        m = self._square_side
        n = self._size

        # Build the horizontal lines
        horizontal_line = ['+' for x in range(m + 1)]
        dashes = '-'.join(['-' for x in range(m)])
        horizontal_line = dashes.join(horizontal_line)

        #
        # Build the rows
        #

        # Final_parts will aggregate the rows
        final_parts = [horizontal_line]

        # Use an m x m double-loop to loop through the rows
        for index1 in range(m):
            rows = []

            for index2 in range(m):
                current_row = index1 * m + index2
                
                # From here, we'll build the row by looping through the portion 
                # of each row that fits within a box
                box_rows = []

                for index3 in range(m):

                    # Grab the portion of the current row that fits in this box
                    current_slice = self._rows[current_row][index3*m:index3*m+m]

                    # Make a string out of it, separated by spaces
                    values = " ".join([str(x) for x in current_slice])

                    # Replace 0's with spaces, since they represent unknown 
                    # squares
                    values = values.replace("0", " ")

                    # Save the created row
                    box_rows.append(values)

                # Combine the created box rows with bars (as graphics), and save
                # it to the list of rows
                row = '|' + '|'.join(box_rows) + '|'
                rows.append(row) 

            # Combine the rows within this box into a big "box string"
            box = "\n".join(rows)

            # Then add the box string and a separator line
            final_parts.append(box)
            final_parts.append(horizontal_line)

        # Combine it all
        
        final_string = "\n".join(final_parts)

        return final_string


#EOF

