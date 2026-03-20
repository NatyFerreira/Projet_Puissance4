class Player:
    def __init__(self, name, pawn):
        self.name = name
        self.pawn = pawn

    def choose_column(self):
        col = input(f"{self.name}, escolha uma coluna (0-6): ")
        return int(col)
