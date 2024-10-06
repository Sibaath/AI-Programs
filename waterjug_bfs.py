import heapq

# Greedy BFS algorithm to solve the Water Jug problem
def greedy_bfs(jug1_capacity, jug2_capacity, goal, target_jug):
    # Initial state (both jugs are empty)
    start_state = (0, 0)
    
    # Priority queue to store the states based on the heuristic (h)
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start_state, goal), start_state))
    
    # To keep track of visited states
    visited = set()
    visited.add(start_state)
    
    # Parent dictionary to reconstruct the path
    parent = {}
    parent[start_state] = None
    
    while priority_queue:
        # Get the state with the lowest heuristic cost
        _, (jug1, jug2) = heapq.heappop(priority_queue)
        
        # If we reached the goal in the specified jug
        if (target_jug == 1 and jug1 == goal) or (target_jug == 2 and jug2 == goal):
            return reconstruct_path(parent, (jug1, jug2))
        
        # Explore the neighbors (valid moves)
        for next_state in get_neighbors(jug1, jug2, jug1_capacity, jug2_capacity):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (jug1, jug2)
                heapq.heappush(priority_queue, (heuristic(next_state, goal), next_state))
    
    return None

# Heuristic function (Manhattan distance to the goal)
def heuristic(state, goal):
    jug1, jug2 = state
    return min(abs(jug1 - goal), abs(jug2 - goal))

# Reconstruct the path from the parent dictionary
def reconstruct_path(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    return path[::-1]

# Get all valid neighbors (possible next states)
def get_neighbors(jug1, jug2, jug1_capacity, jug2_capacity):
    neighbors = []
    
    # Fill Jug 1
    neighbors.append((jug1_capacity, jug2))
    
    # Fill Jug 2
    neighbors.append((jug1, jug2_capacity))
    
    # Empty Jug 1
    neighbors.append((0, jug2))
    
    # Empty Jug 2
    neighbors.append((jug1, 0))
    
    # Pour Jug 1 -> Jug 2
    pour_amount = min(jug1, jug2_capacity - jug2)
    neighbors.append((jug1 - pour_amount, jug2 + pour_amount))
    
    # Pour Jug 2 -> Jug 1
    pour_amount = min(jug2, jug1_capacity - jug1)
    neighbors.append((jug1 + pour_amount, jug2 - pour_amount))
    
    return neighbors

# To solve the problem
def water_jug_solver_greedy(jug1_capacity, jug2_capacity, goal, target_jug):
    path = greedy_bfs(jug1_capacity, jug2_capacity, goal, target_jug)
    if path:
        print(f"Solution found with the goal in Jug {target_jug}:")
        for state in path:
            print(state)
    else:
        print("No solution found.")

jug1_capacity = int(input("Enter the jug1 capacity: "))
jug2_capacity = int(input("Enter the jug2 capacity: "))
goal = int(input("Enter the goal amount of water: "))
target_jug = int(input("Which jug should contain the goal amount? (1 or 2): "))

if target_jug in [1, 2]:
    water_jug_solver_greedy(jug1_capacity, jug2_capacity, goal, target_jug)
else:
    print("Invalid input! Please enter 1 or 2.")
