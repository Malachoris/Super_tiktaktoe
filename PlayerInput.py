from Boardy import Boardy

class PlayerInput:

	def __init__(self, board: list):
		self.board = board

	def player_move(self, symbol: str):
		number: int = 0
		
		if symbol == "x":
			number = 1
		elif symbol == "o":
			number = 2
		else:
			raise ValueError (f"Incorrect {symbol}, can only be 'x' or 'o'")

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
				print(f"Incorrect input {square_choice}, try again enter a valid number between 1 and 9.")
				continue

			if self.board[square_choice - 1] == " ":
				self.board[square_choice - 1] = symbol
				break
			else:
				print()
				print("That space is taken.")
