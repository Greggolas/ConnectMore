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

    # working on this
    def row_check(self, index):
        # check each cell in row
        pass

    def col_check(self):
        # check each cell in column
        pass

    def diag_check(self):
        pass
    
    def win_check(self):
        # for each index check columns and rows
        pass

