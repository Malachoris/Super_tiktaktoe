from Boardy import Boardy
from PlayerInput import PlayerInput
from Rules import Rules

class Game:
	def __init__(self):
		self.board = Boardy()
		self.player_input = PlayerInput(self.board.small_board)
		self.rules = Rules(self.board.small_board)

	def play (self):
		while True:
			self.board.print_board()

			self.player_input.player_move("x")
			self.board.print_board()
			if self.rules.player_won("x", self.board.small_board):
				print("x won")
				break
			elif self.rules.is_draw():
				print("draw")
				break
			self.player_input.player_move("o")
			if self.rules.player_won("o", self.board.small_board):
				self.board.print_board()
				print("o won")
				break
			elif self.rules.is_draw():
				print("draw")
				break