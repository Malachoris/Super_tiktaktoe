BOARD_SIZE = 9
COL_SIZE = 3

class Board:

	def __init__(self):
		self.small_board = [" " for _ in range(BOARD_SIZE)]


	def print_board(self):
		for i in range(BOARD_SIZE):
		pass

	def player_move(self, symbol: str):
		number: int = 0
		if symbol == 'x':
			number = 1
		elif symbol == 'o':
			number = 2
		print(f"Your turn player {number}")


		# try:
		square_choice = int(inpu("Enter square number (1-9): ").strip())
		if not (1 <= square_choice <= 9):
			return square_choice
			if small_board[square_choice - 1] == " ":
				small_board[square_choice - 1] = symbol
			else:
				print()
				print("That space is taken.")
		else:
			print("Incorect input, please enter valid number.")
		# except Exception:
		# 	print("Incorect input, please enter valid number.")

	def player_won(self, symbol: str, small_board: []):
		start_range = 0
		stop_range = len(small_board)
		step_over = 3

		for column in range(COL_SIZE):
			if small_board[column::COL_SIZE] == symbol:
				return True

		for row in range(start_range, stop_range, step_over):
			if small_board[row:row + step_over] == symbol:
				return True

		if small_board[::4] == symbol:
			return True
		if small_board[1:8:3] == symbol:
			return True

		return False

	def is_draw(self):
		pass

board = Board()
print(board.small_board)