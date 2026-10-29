from itertools import permutations

n = int(input("Enter number of cities: "))
dist = []

for i in range(n):
    row = list(map(int, input().split()))
    dist.append(row)

cities = list(range(1, n))
min_cost = float('inf')
best_path = []

for p in permutations(cities):
    path = [0] + list(p) + [0]
    cost = 0

    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Shortest path:", " -> ".join(map(str, best_path)))
print("Minimum cost:", min_cost)