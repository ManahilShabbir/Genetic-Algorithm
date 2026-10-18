
N = 4

population = [
    [2, 4, 3, 1],
    [1, 2, 3, 4],
    [2, 1, 3, 2],
    [4, 3, 1, 1]
]

def count_conflicts(chromosome):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            if chromosome[i] == chromosome[j]:
                conflicts += 1

            elif abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def fitness(chromosome):
    return 6 - count_conflicts(chromosome)

def evaluate(population, generation):
    print("\nGeneration", generation)
    print("-" * 45)

    total = 0

    for i in range(len(population)):
        conflicts = count_conflicts(population[i])
        fit = fitness(population[i])
        total += fit

        print("State:", population[i],
              "| Conflicts:", conflicts,
              "| Fitness:", fit)

    print("Total Fitness:", total)

def roulette_selection(population, random_values):
    total_fitness = sum(fitness(ch) for ch in population)
    selected = []

    for value in random_values:
        cumulative = 0

        for chromosome in population:
            probability = fitness(chromosome) / total_fitness
            cumulative += probability

            if value < cumulative:
                selected.append(chromosome[:])
                break

    return selected

def crossover(parent1, parent2):
    child1 = parent1[:2] + parent2[2:]
    child2 = parent2[:2] + parent1[2:]

    return child1, child2

def create_generation(parents):
    new_population = []

    for i in range(0, len(parents), 2):
        child1, child2 = crossover(
            parents[i], parents[i + 1]
        )

        new_population.append(child1)
        new_population.append(child2)

    return new_population

evaluate(population, 0)

random_values_1 = [0.12, 0.67, 0.91, 0.43]

parents = roulette_selection(population, random_values_1)
population = create_generation(parents)

evaluate(population, 1)

random_values_2 = [0.10, 0.35, 0.60, 0.85]

parents = roulette_selection(population, random_values_2)
population = create_generation(parents)

