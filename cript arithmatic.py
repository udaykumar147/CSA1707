from itertools import permutations

def solve_cryptarithmetic(puzzle):
    letters = set(char for word in puzzle for char in word if char.isalpha())
    if len(letters) > 10:
        print("Invalid puzzle: Too many unique letters.")
        return

    for perm in permutations(range(1, 10), len(letters)):
        mapping = dict(zip(letters, perm))
        if is_solution_valid(puzzle, mapping):
            print_solution(puzzle, mapping)
            return

    print("No solution found.")

def is_solution_valid(puzzle, mapping):
    num1 = ''.join(str(mapping[char]) for char in puzzle[0])
    num2 = ''.join(str(mapping[char]) for char in puzzle[1])
    result = ''.join(str(mapping[char]) for char in puzzle[2])

    if int(num1) + int(num2) == int(result):
        return True
    return False

def print_solution(puzzle, mapping):
    for word in puzzle:
        print(''.join(str(mapping[char]) for char in word), end=' ')
        if word != puzzle[-1]:
            print("+ ", end='')
    print()
    
puzzle = ["BASE", "BALL", "GAMES"]
solve_cryptarithmetic(puzzle)
