class Board:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.grid = [[" " for _ in range(cols)] for _ in range(rows)]

    def display(self):
        for row in self.grid:
            print("| " + " | ".join(row) + " |")
        print("  " + "   ".join(str(i) for i in range(self.cols)))

    def is_valid_move(self, col):
        return self.grid[0][col] == " "

    def drop_pawn(self, col, symbol):
        for row in reversed(self.grid):
            if row[col] == " ":
                row[col] = symbol
                return True
        return False
