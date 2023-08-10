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
			for board in row:
				board.print_board()
				print("  |  ", end="")
		print("\n" + "-" * 25)

if __name__ == "__main__":
	board = UltimateBoard()
	board.print_ultimate_board()
	