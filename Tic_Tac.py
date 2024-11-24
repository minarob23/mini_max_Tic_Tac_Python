# Constants
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = "E"

# Function to check if the game is over and return the winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    # Check for draw
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return None  # Game is still ongoing
    
    return "Deal Game"  # No empty spaces, it's a draw

# Minimax algorithm to calculate the best move
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 1  # X wins
    elif winner == PLAYER_O:
        return -1  # O wins
    elif winner == "Deal Game":
        return 0  # Draw
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X  # X's move
                    eval = minimax(board, False)  # Minimize for O's turn
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O  # O's move
                    eval = minimax(board, True)  # Maximize for X's turn
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to predict the winner based on the current board
def predict_winner(board):
    result = minimax(board, True)  # Start with maximizing for X
    if result == 1:
        return "X"  # X wins
    elif result == -1:
        return "O"  # O wins
    else:
        return "Deal Game"  # Draw

# Function to input the board state from the user
def input_board():
    board = []
    print("Enter the Tic-Tac-Toe board (use X, O, E for empty spots):")
    for i in range(3):
        row = input(f"Enter row {i+1} (e.g., X O E): ").split()
        board.append(row)
    return board

# Main program
if __name__ == "__main__":
    # Input the board from the user
    board = input_board()

    # Showing the text of Analysing AI
    print("\nAI is analysing...........\n")

    # Predict the winner based on the Minimax algorithm
    winner = predict_winner(board)
    print(f"The Decided winner is: {winner}")
