import math

# Define players
PLAYER_X = "X"  # Human
PLAYER_O = "O"  # AI
EMPTY = " "

# Initialize the board
def create_board():
    return [[EMPTY]*3 for i in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if the current player is a winner
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([spot == player for spot in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True

    if all([board[i][i] == player for i in range(3)]):  # Check main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check anti-diagonal
        return True

    return False

# Check if the board is full
def is_full(board):
    return all([board[i][j] != EMPTY for i in range(3) for j in range(3)])

# Get all available moves (empty spots)
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

# Alpha-Beta Pruning algorithm
def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, PLAYER_X):
        # return -10 + depth  # Human wins, negative score
        return -1
    elif is_winner(board, PLAYER_O):
        # return 10 - depth  # AI wins, positive score
        return 1
    elif is_full(board):
        return 0  # Tie

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = PLAYER_O
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:  # Prune the remaining branches
                break
        return best_score
    else:
        best_score = math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = PLAYER_X
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:  # Prune the remaining branches
                break
        return best_score

# Get the best move for the AI using Alpha-Beta Pruning
def get_best_move(board):
    best_score = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for (i, j) in get_available_moves(board):
        board[i][j] = PLAYER_O
        score = minimax(board, 0, False, alpha, beta)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

# Check if the game is over
def is_game_over(board):
    return is_winner(board, PLAYER_X) or is_winner(board, PLAYER_O) or is_full(board)

# Main game loop
def play_game():
    board = create_board()
    current_player = PLAYER_X

    while not is_game_over(board):
        print_board(board)
        if current_player == PLAYER_X:
            print("Player X's turn!")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                current_player = PLAYER_O
            else:
                print("Invalid move! Try again.")
        else:
            print("AI's turn!")
            move = get_best_move(board)
            if move:
                board[move[0]][move[1]] = PLAYER_O
                current_player = PLAYER_X

    print_board(board)
    if is_winner(board, PLAYER_X):
        print("Player X wins!")
    elif is_winner(board, PLAYER_O):
        print("AI wins!")
    else:
        print("It's a tie!")

play_game()
