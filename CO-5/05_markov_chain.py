# Markov Chain model for predicting the next weather state
import random

transitions = {
    "Sunny": [("Sunny", 0.7), ("Rainy", 0.3)],
    "Rainy": [("Sunny", 0.4), ("Rainy", 0.6)]
}

def next_state(current):
    choices, probabilities = zip(*transitions[current])
    return random.choices(choices, weights=probabilities)[0]

state = "Sunny"
print("Day 1:", state)
for day in range(2, 8):
    state = next_state(state)
    print(f"Day {day}: {state}")
