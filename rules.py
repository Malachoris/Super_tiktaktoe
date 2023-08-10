from constants import COL_SIZE
from converter import Converter
from board import Board


class Rules:
    def __init__(self, board: list):
        self.converter = Converter()
        self.board = board

    def is_win_score(self, list_of_values: list) -> bool:
        return abs(sum(self.converter.input_value_converter(list_of_values))) == 3

    def player_won(self, symbol: str, board: list):
        start_range = 0
        stop_range = len(self.board)
        step_over = 3

        # column
        for column in range(COL_SIZE):
            if self.is_win_score(self.board[column::COL_SIZE]):
                return True

        # row
        for row in range(start_range, stop_range, step_over):
            if self.is_win_score(self.board[row : row + step_over]):
                return True

        # diagonal
        if self.is_win_score(self.board[:: step_over + 1]):
            return True
        if self.is_win_score(
            self.board[start_range + 2 : stop_range - 2 : step_over - 1]
        ):
            return True

        return False

    def is_draw(self) -> bool:
        return " " not in self.board
