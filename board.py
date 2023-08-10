from constants import BOARD_SIZE


class Board:
    def __init__(self):
        self.small_board = [" " for _ in range(BOARD_SIZE)]

    def print_board(self):
        for index, item in enumerate(self.small_board, start=1):
            print(item, end=" " if index % 3 else "\n")
