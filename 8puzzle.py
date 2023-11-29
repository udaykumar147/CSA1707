import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def generate_moves(state):
    zero_index = state.index(0)
    row, col = zero_index // 3, zero_index % 3
    moves = []

    if row > 0:
        moves.append(-3)  
    if row < 2:
        moves.append(3)   
    if col > 0:
        moves.append(-1)  
    if col < 2:
        moves.append(1)   

    return moves

def apply_move(state, move):
    zero_index = state.index(0)
    new_state = list(state)
    new_index = zero_index + move
    new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
    return tuple(new_state)

def manhattan_distance(state):
    distance = 0
    for i in range(1, 9):
        current_row, current_col = divmod(state.index(i), 3)
        goal_row, goal_col = divmod(i - 1, 3)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_move_description(node):
    move = node.action
    cost = node.cost

    if move == -3:
        return f"Move the blank space Up (Cost: {cost})"
    elif move == 3:
        return f"Move the blank space Down (Cost: {cost})"
    elif move == -1:
        return f"Move the blank space Left (Cost: {cost})"
    elif move == 1:
        return f"Move the blank space Right (Cost: {cost})"

def solve_puzzle(initial_state):
    initial_node = PuzzleNode(state=initial_state, heuristic=manhattan_distance(initial_state))
    priority_queue = [initial_node]
    visited = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.state == (1, 2, 3, 4, 5, 6, 7, 8, 0):
            # Solution found
            path = []
            while current_node:
                path.insert(0, current_node)
                current_node = current_node.parent
            return path

        visited.add(current_node.state)

        for move in generate_moves(current_node.state):
            next_state = apply_move(current_node.state, move)
            if next_state not in visited:
                next_node = PuzzleNode(
                    state=next_state,
                    parent=current_node,
                    action=move,
                    cost=current_node.cost + 1,
                    heuristic=manhattan_distance(next_state)
                )
                heapq.heappush(priority_queue, next_node)

    return None  

def get_user_input():
    print("Enter the initial state of the puzzle (use 0 to represent the blank space):")
    initial_state = tuple(map(int, input().split()))
    return initial_state

if __name__ == "__main__":
    initial_state = get_user_input()
    solution_path = solve_puzzle(initial_state)

    if solution_path:
        print("Solution found:")
        total_cost = 0
        for step, node in enumerate(solution_path):
            move_description = get_move_description(node)
            print(f"Step {step + 1}: {move_description}")
            print(f"{node.state[0]} {node.state[1]} {node.state[2]}\n{node.state[3]} {node.state[4]} {node.state[5]}\n{node.state[6]} {node.state[7]} {node.state[8]}\n")
            total_cost = node.cost
        print(f"Total Cost: {total_cost}")
    else:
        print("No solution found.")
