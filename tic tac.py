board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

game_still_on = True

winner = "none"

current_player = "X"


def display_board():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])


def play_game():
    display_board()

    while game_still_on:
        handle_turn(current_player)

        check_if_game_is_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner, "won")
    elif winner == "none":
        print("tie")


def handle_turn(player):
    print(player,"'s turn")
    position = input("choose a position from 1-9: ")
    valid=False
    while not valid:
     while position not in ["1","2","3","4","5","6","7","8","9"]:
        position = input("try again")
     if position in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("wanna change y/n")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("try again")
        position = int(position) - 1
     if board[position] == "_":
      valid = True
     else:
        position = input("not possible")

    board[position] = player
    display_board()




def check_if_game_is_over():
    if_win()
    if_tie()


def if_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = "none"
    return


def check_rows():
    global game_still_on

    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    if row_1 or row_2 or row_3:
        game_still_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_on

    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_still_on = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    global game_still_on

    bin1 = board[0] == board[4] == board[8] != "_"
    bin2 = board[2] == board[4] == board[6] != "_"
    if bin1 or bin2:
        game_still_on = False
    if bin1:
        return board[0]
    if bin2:
        return board[2]
    return


def if_tie():
    global game_still_on
    if "_" not in board:
        game_still_on = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()
