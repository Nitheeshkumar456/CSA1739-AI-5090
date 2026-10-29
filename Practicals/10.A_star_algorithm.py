def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Total cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                open_list.append((new_f, new_g, neighbor, path + [neighbor]))

    print("No path found")


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 1,
    'D': 0
}

start = 'A'
goal = 'D'

astar(graph, heuristic, start, goal)