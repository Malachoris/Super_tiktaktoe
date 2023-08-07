BOARD_SIZE = 9
COL_SIZE = 3

# small_board = [" " for _ in range(BOARD_SIZE)]
small_board = ["x", "x", "x", " ", " ", " ", " ", " ", " "]

start_range = 0
stop_range = len(small_board)
step_over = 3


def input_value_converter(list_of_values: list):
	numeric_values = [1 if value == "x" else -1 if value == "o" else 0 for value in list_of_values]
	return abs(sum(numeric_values)) == 3

def win_condition(small_board: list):

	# column
	for column in range(COL_SIZE):
		if input_value_converter(small_board[column::COL_SIZE]):
			return True

	# row
	for row in range(start_range, stop_range, step_over):
		if input_value_converter(small_board[row:row + step_over]):
			return True

	# diagonal
	if input_value_converter(small_board[::4]):
		return True
	if input_value_converter(small_board[1:8:3]):
		return True

	return False

if win_condition(small_board) == True:
	print("player won")
