from collections import deque

def solve_puzzle(start, goal):
    queue = deque([(start, [])])
    visited = {tuple(start)}
    moves = {
        'Up': -3,
        'Down': 3,
        'Left': -1,
        'Right': 1
    }

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for move, change in moves.items():
            if move == 'Up' and row == 0:
                continue
            if move == 'Down' and row == 2:
                continue
            if move == 'Left' and col == 0:
                continue
            if move == 'Right' and col == 2:
                continue

            new_zero = zero + change
            new_state = state[:]
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]

            key = tuple(new_state)

            if key not in visited:
                visited.add(key)
                queue.append((new_state, path + [new_state]))

    return None


start = list(map(int, input("Enter initial state (0 for blank): ").split()))
goal = list(map(int, input("Enter goal state: ").split()))

if len(start) != 9 or len(goal) != 9:
    print("Invalid input")
else:
    result = solve_puzzle(start, goal)

    if result is None:
        print("No solution exists")
    else:
        print("Solution found:")
        for state in result:
            for i in range(0, 9, 3):
                print(*state[i:i + 3])
            print()
        print("Total moves:", len(result))