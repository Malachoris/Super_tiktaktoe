from constants import BOARD_SIZE

class UltimateBoard:
	
	def __init__(self):
		self.ultimate_board = [Board.print_board() for _ in range(BOARD_SIZE)]

	def print_ultimate_board(self):
		for index, item in enumerate(self.ultimate_board, start = 1):
			print(item, end=" " if index % 3 else '\n')
			