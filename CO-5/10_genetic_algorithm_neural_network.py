# Genetic algorithm evolves weights of a tiny neural network for XOR.
# NumPy is required: pip install numpy
import numpy as np
import random

X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
y = np.array([0,1,1,0], dtype=float)
GENES = 2*4 + 4 + 4*1 + 1
POP = 30

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -30, 30)))

def fitness(g):
    i = 0
    W1 = g[i:i+8].reshape(2,4); i += 8
    b1 = g[i:i+4]; i += 4
    W2 = g[i:i+4].reshape(4,1); i += 4
    b2 = g[i]
    pred = sigmoid(sigmoid(X @ W1 + b1) @ W2 + b2).ravel()
    return -float(np.mean((pred-y)**2))

population = [np.random.uniform(-2, 2, GENES) for _ in range(POP)]
for generation in range(150):
    population.sort(key=fitness, reverse=True)
    next_gen = population[:4]
    while len(next_gen) < POP:
        p1, p2 = random.sample(population[:15], 2)
        mask = np.random.rand(GENES) < 0.5
        child = np.where(mask, p1, p2).copy()
        child += np.random.normal(0, 0.15, GENES) * (np.random.rand(GENES) < 0.1)
        next_gen.append(child)
    population = next_gen

best = max(population, key=fitness)
print("Best fitness:", fitness(best))
i = 0
W1 = best[i:i+8].reshape(2,4); i += 8
b1 = best[i:i+4]; i += 4
W2 = best[i:i+4].reshape(4,1); i += 4
b2 = best[i]
predictions = sigmoid(sigmoid(X @ W1 + b1) @ W2 + b2).ravel()
print("XOR predictions:", np.round(predictions, 3))
print("Classes:", (predictions >= 0.5).astype(int))
