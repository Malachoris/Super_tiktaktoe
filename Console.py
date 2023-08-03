BOARD_SIZE = 9
ROW_SIZE = 3

small_board = [_ for _ in range(BOARD_SIZE)]

start_range = 0
stop_range = len(small_board)
step_over = 3

for _ in range(ROW_SIZE):
	print(small_board[_::ROW_SIZE])

print()

for _ in range(start_range, stop_range, step_over):
	print(small_board[_:_ + step_over])

print()

print(small_board[::4])
print(small_board[1:8:3])

