from collections import deque

def water_jug(capacity1, capacity2, target):
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            for state in path:
                print(state)
            return

        states = [
            (capacity1, y),
            (x, capacity2),
            (0, y),
            (x, 0),
            (x - min(x, capacity2 - y), y + min(x, capacity2 - y)),
            (x + min(y, capacity1 - x), y - min(y, capacity1 - x))
        ]

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No solution exists")

capacity1 = int(input("Enter capacity of jug 1: "))
capacity2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

water_jug(capacity1, capacity2, target)