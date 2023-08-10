from constants import COL_SIZE
from Converter import Converter
from Board import Board

class Rules:

	def __init__(self, board: list):
		self.converter = Converter()
		self.board = board

	def is_win_score(self, list_of_values: list) -> bool:
		return abs(sum(self.converter.input_value_converter(list_of_values))) == 3

	def player_won(self, symbol: str, small_board: list):
		start_range = 0
		stop_range = len(small_board)
		step_over = 3

		# column
		for column in range(COL_SIZE):
			if self.is_win_score(small_board[column::COL_SIZE]):
				return True

		# row
		for row in range(start_range, stop_range, step_over):
			if self.is_win_score(small_board[row:row + step_over]):
				return True

		# diagonal
		if self.is_win_score(small_board[::step_over + 1]):
			return True
		if self.is_win_score(small_board[start_range + 2:stop_range - 2:step_over - 1]):
			return True

		return False

	def is_draw(self) -> bool:
		return " " not in self.board