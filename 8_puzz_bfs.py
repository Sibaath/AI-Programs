import heapq

def manhattan(board, goal):
    distance = 0
    dimension = int(len(board) ** 0.5)
    for i in range(len(board)):
        if board[i] != 0:
            correct_pos = goal.index(board[i])
            current_row, current_col = divmod(i, dimension)
            correct_row, correct_col = divmod(correct_pos, dimension)
            distance += abs(current_row - correct_row) + abs(current_col - correct_col)
    return distance

# Puzzle manipulation functions
def is_goal(board, goal):
    return board == goal

def get_neighbors(board):
    neighbors = []
    dimension = int(len(board) ** 0.5)
    zero_pos = board.index(0)
    row, col = divmod(zero_pos, dimension)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < dimension and 0 <= new_col < dimension:
            new_zero_pos = new_row * dimension + new_col
            new_board = board[:]
            new_board[zero_pos], new_board[new_zero_pos] = new_board[new_zero_pos], new_board[zero_pos]
            neighbors.append(new_board)
    return neighbors

# Solvability check function
def is_solvable(board):
    inv_count = 0
    flat_board = [x for x in board if x != 0]  # Flatten board without the 0 (blank)
    for i in range(len(flat_board)):
        for j in range(i + 1, len(flat_board)):
            if flat_board[i] > flat_board[j]:
                inv_count += 1
    return inv_count % 2 == 0

# Best First Search Algorithm
def best_first_search(start, goal):
    if not is_solvable(start):
        return None

    open_list = []
    heapq.heappush(open_list, (manhattan(start, goal), start))  # (priority, board)
    closed_set = set()
    parent_map = {tuple(start): None}

    while open_list:
        _, current_board = heapq.heappop(open_list)

        if is_goal(current_board, goal):
            return reconstruct_path(current_board, parent_map)

        closed_set.add(tuple(current_board))

        for neighbor in get_neighbors(current_board):
            if tuple(neighbor) not in closed_set:
                parent_map[tuple(neighbor)] = current_board
                heapq.heappush(open_list, (manhattan(neighbor, goal), neighbor))

    return None

# Reconstruct the solution path from parent_map
def reconstruct_path(board, parent_map):
    path = []
    while board:
        path.append(board)
        board = parent_map[tuple(board)]
    return path[::-1]

# Helper function to print the solution
def print_solution(solution):
    if solution:
        for step in solution:
            for i in range(0, len(step), 3):
                print(step[i:i + 3])
            print()
    else:
        print("No solution found or the puzzle is unsolvable.")

def code():
    
    start_board = [1, 2, 3, 0, 4, 5, 6, 7, 8]  # Input board
    goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]   # Goal state

    print("Best First Search Solution:")
    best_first_solution = best_first_search(start_board, goal_board)
    print_solution(best_first_solution)

code()