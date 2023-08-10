from board import Board


class Game:
    def __init__(self):
        self.board = Board()

    def play(self):
        while True:
            self.board.print_board()

            self.board.player_move("x")
            self.board.print_board()
            if self.board.player_won("x", self.board.small_board):
                print("x won")
                break
            elif self.board.is_draw():
                print("draw")
                break
            self.board.player_move("o")
            if self.board.player_won("o", self.board.small_board):
                self.board.print_board()
                print("o won")
                break
            elif self.board.is_draw():
                print("draw")
                break
