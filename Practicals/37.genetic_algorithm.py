import random

# Fitness function
def fitness(x):
    return x * x

# Initial population
population = [random.randint(0, 31)
              for _ in range(6)]

for generation in range(20):

    population.sort(key=fitness, reverse=True)

    # Select best individuals
    parents = population[:3]

    # Generate offspring
    children = []

    while len(children) < 3:
        p1, p2 = random.sample(parents, 2)

        child = (p1 + p2) // 2

        # Mutation
        if random.random() < 0.2:
            child = random.randint(0, 31)

        children.append(child)

    population = parents + children

best = max(population, key=fitness)

print("Best Solution:", best)
print("Maximum Fitness:", fitness(best))