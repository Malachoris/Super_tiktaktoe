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
        for index, row in enumerate(self.ultimate_board, start=1):
            print(index, end=" " if index % 3 else "\n")
            # print(index)
            # print(row)# self.print_row(row)
            # print("-" * 25)
            for index, board in enumerate(row, start=1):
                # print(board)
                print(board, end=" " if index % 3 else "\n")
                # print(board)
                # for index, item in enumerate(board.small_board, start = 1):
                    # print(index, end=" " if index % 3 else "\n")
                    # print()


if __name__ == "__main__":
    board = UltimateBoard()
    print(board.ultimate_board)
    board.print_ultimate_board()
