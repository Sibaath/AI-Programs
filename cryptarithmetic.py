import itertools

# Function to check if the current assignment of letters to digits is valid
def is_valid(solution, first, second, result):
    # Convert the word to a number based on the current assignment
    def word_to_number(word):
        return int("".join(str(solution[letter]) for letter in word))

    # Check if the sum of first and second equals result
    return word_to_number(first) + word_to_number(second) == word_to_number(result)

# Solve the cryptarithmetic problem
def solve_cryptarithmetic(first, second, result):
    letters = set(first + second + result)  # Unique letters involved
    assert len(letters) <= 10, "There are more than 10 unique letters!"

    # Try every possible digit permutation for the letters
    for perm in itertools.permutations(range(10), len(letters)):
        solution = dict(zip(letters, perm))
        # Check if the first letters (SEND, MORE, MONEY) are non-zero
        if solution[first[0]] == 0 or solution[second[0]] == 0 or solution[result[0]] == 0:
            continue  # Skip invalid solutions where any word starts with 0
        
        # Check if this is a valid solution
        if is_valid(solution, first, second, result):
            return solution

    return None  # No solution found

def code():
    # Define the words for the cryptarithmetic problem
    first = input("Enter the first word : ")
    second = input("Enter the second word : ")
    result = input("Enter the result word : ")

    # Solve the problem
    solution = solve_cryptarithmetic(first, second, result)

    if solution:
        print("Solution found:")
        for letter, digit in solution.items():
            print(f"{letter} = {digit}")
    else:
        print("No solution found.")
        
code()



#         return int("".join(str(solution[letter]) for letter in word))


# val = 0
# for i in first:
#     val = val*10 + solution[i]