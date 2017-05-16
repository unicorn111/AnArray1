from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1
    NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    NEIGHBORS1 = [ (0, 1), (1, 0), (1, 1)]
    NEIGHBORS2 = [(-1, -1), (-1, 0),  (0, -1)]
    NEIGHBORS3 = [(0, -1), (1, -1), (1, 0)]
    NEIGHBORS4 = [(-1, 0), (-1, 1), (0, 1)]


    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.

        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        self.num_rows = num_rows
        self.num_cols = num_cols
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.

        :return: the number rows in the grid.
        """
        return self.num_rows

    def num_cols(self):
        """
        Returns the number of columns in the grid.

        :return:Returns the number of columns in the grid.
        """
        return self.num_cols

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list:
        :return:
        """
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._grid.__setitem__((i, j), 0)
        for k in coord_list:
            self._grid.__setitem__(k, 1)

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        if self._grid.__getitem__((row, col)) == LifeGrid.LIVE_CELL:
            return LifeGrid.LIVE_CELL
        else:
            return LifeGrid.DEAD_CELL

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid.__setitem__((row, col), 0)

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid.__setitem__((row, col), 1)

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.

        :param row: row of the cell.
        :param col: column of the cell.
        :return:
        """
        res = 0
        if row == 0 and col == self.num_cols - 1:
            for i in LifeGrid.NEIGHBORS3:
                new_row = row + i[0]
                new_col = col + i[1]
                res += LifeGrid.is_live_cell(self, new_row, new_col)
        elif row == self.num_rows - 1 and col == 0:
            for i in LifeGrid.NEIGHBORS4:
                new_row = row + i[0]
                new_col = col + i[1]
                res += LifeGrid.is_live_cell(self, new_row, new_col)
        elif row == 0 or col == 0 or row == 0 and col == 0:
            for i in LifeGrid.NEIGHBORS1:
                new_row = row + i[0]
                new_col = col + i[1]
                res += LifeGrid.is_live_cell(self, new_row, new_col)
        elif row == self.num_rows - 1 or col == self.num_cols - 1 or row == self.num_rows - 1 and col == self.num_cols - 1:
            for i in LifeGrid.NEIGHBORS2:
                new_row = row + i[0]
                new_col = col + i[1]
                res += LifeGrid.is_live_cell(self, new_row, new_col)
        else:
            for i in LifeGrid.NEIGHBORS:
                new_row = row + i[0]
                new_col = col + i[1]
                res += LifeGrid.is_live_cell(self, new_row, new_col)
        return res

    def __str__(self):
        a = ''
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                print(self._grid.__getitem__((i, j)))
        return '{}'.format(a)