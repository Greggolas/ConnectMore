class Cell:
    def __init__(self, value=None):
        self.value = value


class Grid:
    def __init__(self, size):
        self.indexes = range(size)
        self.layout = {}

        for x in self.indexes:
            self.layout[x] = {}
            
            for y in self.indexes:
                self.layout[x][y] = Cell()

    def paint(self):
        for y in self.indexes:
            row_out = ""
            
            for x in self.indexes:
                row_out += "|"
                
                cell = self.layout[x][y]
                if cell.value:
                    row_out += str(cell.value)
                else:
                    row_out += "#"

                row_out += "|"

            print(row_out)

    def play(self, column, player):
        column = int(column)
        for y in reversed(self.indexes):
            if not self.layout[column][y].value:
                self.layout[column][y].value = player
                return True

        return False

    def _all_winners(self, list):
        return all(i == list[0] and i for i in list)

    # working on this
    def row_check(self, index):
        # check each cell in row
        pass

    def col_check(self, x):
        col = self.layout[x]
        col_vals = []
        for y in col:
            cell = col[y]
            if cell:
                col_vals.append(cell.value)
            else:
                return False
            
        return self._all_winners(col_vals)

    def diag_check(self):
        pass
    
    def win_check(self):
        for x in self.indexes:
            col_win = self.col_check(x)

            if col_win:
                return True
        
        return False

