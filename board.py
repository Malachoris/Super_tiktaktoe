BOARD_SIZE = 9
COL_SIZE = 3
ROW_SIZE = 3


class Board:
    def __init__(self):
        self.small_board = [" " for _ in range(BOARD_SIZE)]

    def print_board(self):
        for index, item in enumerate(self.small_board, start=1):
            print(item, end=" " if index % 3 else "\n")

    def player_move(self, symbol: str):
        number: int = 0

        if symbol == "x":
            number = 1
        elif symbol == "o":
            number = 2
        else:
            raise ValueError(f"Incorect {symbol}, can only be 'x' or 'o'")

        square_choice: int = 0
        while True:
            print(f"Your turn player {number}")
            # try catch block should be as small as possible.
            try:
                square_choice = int(input("Enter square number (1-9): ").strip())
            except ValueError:
                print("Incorrect input, please enter a valid number.")
                continue

            if not (1 <= square_choice <= BOARD_SIZE):
                # raise ValueError(f"Incorrect input {square_choice}, try again enter a valid number between 1 and 9.")
                print(
                    f"Incorrect input {square_choice}, try again enter a valid number between 1 and 9."
                )
                continue

            if self.small_board[square_choice - 1] == " ":
                self.small_board[square_choice - 1] = symbol
                break
            else:
                print()
                print("That space is taken.")

    @staticmethod
    def input_value_converter(list_of_values: list):
        numeric_values = []

        conversions = {"x": 1, "o": -1}

        for value in list_of_values:
            numeric_values.append(conversions.get(value, 0))

        return numeric_values

    def is_win_score(self, list_of_values: list) -> bool:
        return abs(sum(self.input_value_converter(list_of_values))) == 3

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
            if self.is_win_score(small_board[row : row + step_over]):
                return True

        # diagonal
        if self.is_win_score(small_board[:: ROW_SIZE + 1]):
            return True
        if self.is_win_score(small_board[start_range + (ROW_SIZE - 1) : stop_range - (ROW_SIZE - 1) : ROW_SIZE - 1]):
            return True

        return False

    def is_draw(self) -> bool:
        return " " not in self.small_board
