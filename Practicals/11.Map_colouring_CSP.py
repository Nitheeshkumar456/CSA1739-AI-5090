def is_valid(color, region, assignment, graph):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, assignment):
    if len(assignment) == len(graph):
        return assignment

    region = next(r for r in graph if r not in assignment)

    for color in colors:
        if is_valid(color, region, assignment, graph):
            assignment[region] = color

            result = map_coloring(graph, colors, assignment)
            if result:
                return result

            del assignment[region]

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
solution = map_coloring(graph, colors, {})

if solution:
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(region, ":", color)
else:
    print("No solution exists")