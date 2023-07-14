# Tic Tac Toe

# Function to create the game board
def create_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

# Function to print the game board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if any player has won
def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

# Function to play the game
def play_game():
    board = create_board()
    current_player = 'X'

    while True:
        print_board(board)
        print("Player", current_player)
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board):
            print_board(board)
            print("Player", current_player, "wins!")
            break

        if all(all(cell != ' ' for cell in row) for row in board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()