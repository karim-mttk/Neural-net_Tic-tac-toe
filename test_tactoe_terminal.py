def create_board():
    # Create a 3x3 matrix to represent the board
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    return board

def display_board(board):
    # Print the board to the console
    for row in board:
        print("|".join(row))


def get_user_move(board):
    # Prompt the user to enter their move
    while True:
        try:
            row = int(input("Enter row number (1-3): ")) - 1
            col = int(input("Enter column number (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "":
                return row, col
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
def make_move(board, row, col, symbol):
    # Update the board with the user's move
    board[row][col] = symbol
def check_win(board):
    # Check for horizontal wins
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]

    # Check for vertical wins
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    # Check for draw
    if all(row.count("") == 0 for row in board):
        return "draw"

    # No winner or draw
    return None

def play_game():
    # Create the initial game board
    board = create_board()

    # Define the players and starting player
    player1 = 'X'
    player2 = 'O'
    current_player = player1

    # Main game loop
    while True:
        # Display the board
        display_board(board)

        # Get the user's move
        row, col = get_user_move(board)

        # Update the board with the user's move
        make_move(board, row, col, current_player)

        # Check for a win or draw
        winner = check_win(board)
        if winner is not None:
            display_board(board)
            if winner == "draw":
                print("The game is a draw!")
            else:
                print(f"Player {winner} wins!")
            break
        # Switch to the next player
        current_player = player2 if current_player == player1 else player1

if __name__ == '__main__':
    play_game()
