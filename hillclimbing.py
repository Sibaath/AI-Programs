import random

# A sample graph represented using an adjacency list
graph = {
    'A': {'B': 1, 'C': 3, 'D': 4},
    'B': {'A': 1, 'C': 2, 'E': 6},
    'C': {'A': 3, 'B': 2, 'D': 5, 'F': 7},
    'D': {'A': 4, 'C': 5, 'F': 8},
    'E': {'B': 6, 'F': 2},
    'F': {'C': 7, 'D': 8, 'E': 2}
}

def get_neighbors(node):
    """ Returns the neighbors of a given node along with their costs. """
    return graph[node]

def objective_function(node, goal_node):
    """
    Example objective function. In this case, we want to minimize the
    "cost" from the current node to the goal node.
    """
    if node == goal_node:
        return 0  # If we have reached the goal node, the cost is 0.
    return sum(get_neighbors(node).values())  # Sum of edges to neighboring nodes.

def local_search(start_node, goal_node, max_iterations=100):
    """
    Perform a simple local search starting from a given node, moving toward the goal node.
    """
    current_node = start_node
    current_value = objective_function(current_node, goal_node)
    
    for iteration in range(max_iterations):
        # If the current node is the goal, stop the search
        if current_node == goal_node:
            print(f"Goal node {goal_node} reached!")
            return current_node, current_value
        
        # Get the neighbors of the current node
        neighbors = get_neighbors(current_node)
        
        # Select a random neighbor (local search does not explore all neighbors exhaustively)
        next_node = random.choice(list(neighbors.keys()))
        next_value = objective_function(next_node, goal_node)
        
        # If the neighbor is better (lower cost), move to the neighbor
        if next_value < current_value or next_node == goal_node:
            current_node = next_node
            current_value = next_value
            print(f"Moving to better node: {current_node}, Objective value: {current_value}")
        else:
            # Otherwise, stay at the current node
            print(f"Staying at node: {current_node}, Objective value: {current_value}")
    
    print(f"Maximum iterations reached without finding the goal.")
    return current_node, current_value

# Main function to run Local Search with user inputs
def code():
    start_node = input("Enter the start node: ").upper()  # Convert to uppercase for consistency
    goal_node = input("Enter the goal node: ").upper()  # Convert to uppercase for consistency
    
    if start_node not in graph or goal_node not in graph:
        print("Invalid start or goal node. Please enter nodes that exist in the graph.")
    else:
        print(f"\nStarting local search from node {start_node} towards goal node {goal_node}...\n")
        final_node, final_value = local_search(start_node, goal_node)
        print(f"\nFinal node after local search: {final_node}")
        print(f"Final objective value: {final_value}")
        
code()
