BOARD_SIZE = 9
COL_SIZE = 3

class Board:

	def __init__(self):
		self.small_board = [" " for _ in range(BOARD_SIZE)]
		# self.small_board = ["o", "o", "o", " ", " ", " ", " ", " ", " "]


	def print_board(self):
		for index, item in enumerate(self.small_board, start = 1):
			print(item, end=" " if index % 3 else '\n')

	def player_move(self, symbol: str):
		number: int = 0
		
		if symbol == "x":
			number = 1
		elif symbol == "o":
			number = 2
		else:
			raise ValueError (f"Incorect {symbol}, can only be 'x' or 'o'")

		square_choice: int = 0
		while True:
			print(f"Your turn player {number}")
			# try catch block should be as small as possible. 
			try:
				square_choice = int(input("Enter square number (1-9): ").strip())
			except ValueError:
				print("Incorrect input, please enter a valid number.")
				continue

			if not (1 <= square_choice <= 9):
				# raise ValueError(f"Incorrect input {square_choice}, try again enter a valid number between 1 and 9.")
				print(f"Incorrect input {square_choice}, try again enter a valid number between 1 and 9.")
				continue

			if self.small_board[square_choice - 1] == " ":
				self.small_board[square_choice - 1] = symbol
				break
			else:
				print()
				print("That space is taken.")

	# converts inputs to nueric values and returns True if equals 3
	@staticmethod
	def input_value_converter(list_of_values: list):
		numeric_values = []

		for value in list_of_values:
			if value == "x":
				numeric_values.append(1)
			elif value == "o":
				numeric_values.append(-1)
			else:
				numeric_values.append(0)

		return abs(sum(numeric_values)) == 3

	def player_won(self, symbol: str, small_board: list):
		start_range = 0
		stop_range = len(small_board)
		step_over = 3

		# positive and negative check 

		# column
		for column in range(COL_SIZE):
			if Board.input_value_converter(small_board[column::COL_SIZE]):
				return True

		# row
		for row in range(start_range, stop_range, step_over):
			if Board.input_value_converter(small_board[row:row + step_over]):
				return True

		# diagonal
		if Board.input_value_converter(small_board[::step_over + 1]):
			return True
		if Board.input_value_converter(small_board[start_range + 2:stop_range - 2:step_over - 1]):
			return True

		return False

	def is_draw(self) -> bool:
		if " " not in self.small_board:
			return True
		else:
			False

if __name__ == "__main__":
	game = Board()

	while True:
		game.print_board()
		game.player_move("x")
		game.print_board()
		if game.player_won("x", game.small_board):
			print("x won")
			break
		elif game.is_draw():
			print("draw")
			break
		game.player_move("o")
		if game.player_won("o", game.small_board):
			game.print_board()
			print("o won")
			break
		elif game.is_draw():
			print("draw")
			break
