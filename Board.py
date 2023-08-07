BOARD_SIZE = 9
COL_SIZE = 3

class Board:

	def __init__(self):
		self.small_board = ["x" for _ in range(BOARD_SIZE)]
		# self.small_board = ["o", "o", "o", " ", " ", " ", " ", " ", " "]


	# def print_board(self):
	# 	for i in range(BOARD_SIZE):
	# 	pass

	def player_move(self, symbol: str):
		number: int = 0
		if symbol == 'x':
			number = 1
		elif symbol == 'o':
			number = 2
		print(f"Your turn player {number}")

		# try catch block should be as small as possible. 
		try:
			square_choice = int(input("Enter square number (1-9): ").strip())
		except ValueError:
			print("Incorrect input, please enter a valid number.")

		if not (1 <= square_choice <= 9):
			print("Incorrect input, please enter a valid number between 1 and 9.")
			return

		if self.small_board[square_choice - 1] == " ":
			self.small_board[square_choice - 1] = symbol
		else:
			print()
			print("That space is taken.")

	# need to calculate indexes of each row and make it abs value so either 111 or -1-1-1. 
	# loop over elemets and check if value is equal abs value 3.

	# Converts inputs to nueric values and returns True if equals 3
	def input_value_converter(list_of_values: list):
		numeric_values = [1 if value == "x" else -1 if value == "o" else 0 for value in list_of_values]
		return abs(sum(numeric_values)) == 3

	def player_won(self, symbol: str, small_board: list):
		start_range = 0
		stop_range = len(small_board)
		step_over = 3

		# positive and negative check 
		# Read about decorators in python

		for column in range(COL_SIZE):
			if Board.input_value_converter(small_board[column::COL_SIZE]):
				return True

		for row in range(start_range, stop_range, step_over):
			if Board.input_value_converter(small_board[row:row + step_over]):
				return True

		if Board.input_value_converter(small_board[::4]):
			return True

		if Board.input_value_converter(small_board[1:8:3]):
			return True

		return False

	def is_draw(self):
		pass

if __name__ == "__main__":
	game = Board()
	board = game.small_board

	while True:
		game.player_move("x")
		if game.player_won("x", board):
			print("x won")
			break
		elif game.is_draw():
			print("draw")
			break
		game.player_move("o")
		if game.player_won("o", board):
			print("o won")
			break
		elif game.is_draw():
			print("draw")
			break
	# print(board.player_won("x", board.small_board))
	# print(board.small_board)
