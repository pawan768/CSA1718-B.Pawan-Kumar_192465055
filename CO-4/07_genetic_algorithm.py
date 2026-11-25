# Genetic Algorithm to maximize f(x) = x^2, where x is in [0, 31]
import random

POPULATION_SIZE = 10
GENERATIONS = 30
CHROMOSOME_LENGTH = 5

def decode(chromosome):
    return int("".join(map(str, chromosome)), 2)

def fitness(chromosome):
    return decode(chromosome) ** 2

def select(population):
    return max(random.sample(population, 3), key=fitness)

population = [[random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]
              for _ in range(POPULATION_SIZE)]

for _ in range(GENERATIONS):
    new_population = []
    while len(new_population) < POPULATION_SIZE:
        p1, p2 = select(population), select(population)
        point = random.randint(1, CHROMOSOME_LENGTH - 1)
        child = p1[:point] + p2[point:]
        if random.random() < 0.1:
            i = random.randrange(CHROMOSOME_LENGTH)
            child[i] = 1 - child[i]
        new_population.append(child)
    population = new_population

best = max(population, key=fitness)
print("Best x:", decode(best))
print("Maximum f(x):", fitness(best))
