from .board import Board
from .player import Player
from .pawn import Pawn

class Engine:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Jogador 1", Pawn("X"))
        self.player2 = Player("Jogador 2", Pawn("O"))
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def run(self):
        while True:
            self.board.display()
            col = self.current_player.choose_column()

            if col < 0 or col >= self.board.cols:
                print("Coluna inválida! Escolha entre 0 e 6.")
                continue

            if not self.board.is_valid_move(col):
                print("Coluna cheia! Tente outra.")
                continue

            self.board.drop_pawn(col, self.current_player.pawn.symbol)

            if self.board.check_victory(self.current_player.pawn.symbol):
                self.board.display()
                print(f"\n🎉 {self.current_player.name} venceu!\n")
                break

            if self.board.check_draw():
                self.board.display()
                print("\nEmpate! O tabuleiro está cheio.\n")
                break

            self.switch_player()
