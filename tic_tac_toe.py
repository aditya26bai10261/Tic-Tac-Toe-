# Tic Tac Toe Game

def show_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_win(board, player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def get_position(board, player):
    while True:
        value = input("Player " + player + ", enter position (1-9): ")

        if not value.isdigit():
            print("Please enter a number.")
            continue

        position = int(value) - 1

        if position < 0 or position > 8:
            print("Choose a number from 1 to 9.")
            continue

        if board[position] == "X" or board[position] == "O":
            print("This position is already taken.")
            continue

        return position


def play_game():
    x_wins = 0
    o_wins = 0
    draws = 0

    while True:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        player = "X"
        moves = 0

        print("\n===== TIC TAC TOE =====")

        while True:
            show_board(board)

            position = get_position(board, player)
            board[position] = player
            moves = moves + 1

            if check_win(board, player):
                show_board(board)
                print("Player", player, "wins!")

                if player == "X":
                    x_wins = x_wins + 1
                else:
                    o_wins = o_wins + 1
                break

            if moves == 9:
                show_board(board)
                print("It's a draw!")
                draws = draws + 1
                break

            if player == "X":
                player = "O"
            else:
                player = "X"

        print("\nScore")
        print("Player X:", x_wins)
        print("Player O:", o_wins)
        print("Draws:", draws)

        again = input("\nDo you want to play again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
