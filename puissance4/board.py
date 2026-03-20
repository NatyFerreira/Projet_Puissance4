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

    def check_victory(self, symbol):
        # Horizontal
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if (self.grid[r][c] == symbol and
                    self.grid[r][c+1] == symbol and
                    self.grid[r][c+2] == symbol and
                    self.grid[r][c+3] == symbol):
                    return True

        # Vertical
        for r in range(self.rows - 3):
            for c in range(self.cols):
                if (self.grid[r][c] == symbol and
                    self.grid[r+1][c] == symbol and
                    self.grid[r+2][c] == symbol and
                    self.grid[r+3][c] == symbol):
                    return True

        # Diagonal crescente (/)
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if (self.grid[r][c] == symbol and
                    self.grid[r-1][c+1] == symbol and
                    self.grid[r-2][c+2] == symbol and
                    self.grid[r-3][c+3] == symbol):
                    return True

        # Diagonal decrescente (\)
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if (self.grid[r][c] == symbol and
                    self.grid[r+1][c+1] == symbol and
                    self.grid[r+2][c+2] == symbol and
                    self.grid[r+3][c+3] == symbol):
                    return True

        return False

    def check_draw(self):
        return all(self.grid[0][c] != " " for c in range(self.cols))
