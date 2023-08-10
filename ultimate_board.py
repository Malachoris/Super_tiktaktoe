from constants import BOARD_SIZE, ROW_SIZE, COL_SIZE
from board import Board


class UltimateBoard:
    def __init__(self):
        self.ultimate_board = []
        for _ in range(COL_SIZE):
            row = []
            for _ in range(ROW_SIZE):
                row.append(Board())
            self.ultimate_board.append(row)

    def print_ultimate_board(self):
        for row in self.ultimate_board:
            self.print_row(row)
            print("-" * (BOARD_SIZE * 2 + COL_SIZE + 1))

    def print_row(self, row):
        for index in range(ROW_SIZE):
            for board in row:
                self.print_board_section(board, index)
                print(" | ", end="")
            print()

    def print_board_section(self, board, row_index):
        start_index = row_index * ROW_SIZE
        end_index = start_index + ROW_SIZE
        board_section = board.small_board[start_index:end_index]
        for index, item in enumerate(board_section, start=1):
            print(item, end=" " if index % 3 else "")
        print(end="")


if __name__ == "__main__":
    board = UltimateBoard()
    board.print_ultimate_board()
