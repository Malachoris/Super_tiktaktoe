super_board = [[" " for _ in range(9)] for _ in range(9)]

# print(super_board)

def print_board():
    for row in super_board:
        print(' | '.join(row))
        print('-' * 34)

# Game starts, player 1 choose big square and then small_square to put "X".
# Script checks if big_square is not depleted if depleted next player can place icon in any small square if not script says which square player can play.
# Script checks if big_square score  


def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    big_choice = int(input("Enter big square nuber (1-9): ").strip())
    if super_board[big_choice - 1] != None:
        # super_board[big_choice - 1] == icon
        choice = int(input("Enter small square nuber (1-9): ").strip()) 
        if super_board[big_choice - 1][choice - 1] == " ":
            super_board[big_choice - 1][choice - 1] = icon
        else:
            print()
            print("Space is taken")
    else:
        print("Square is depleted")


while True:
    print_board()
    player_move("X")
    # print_board()
#     if is_victory("X"):
#         print("X wins")
#         break
#     elif is_draw():
#         print("It's a draw")
#         break
#     player_move("O")
#     if is_victory("O"):
#         print_board()
#         print("O wins")
#         break
#     elif is_draw():
#         print("It's a draw")
#         break