# Q-learning agent in a small 1D environment
import numpy as np
import random

states, actions = 5, 2       # action 0=left, action 1=right
goal = 4
Q = np.zeros((states, actions))
alpha, gamma, epsilon = 0.1, 0.9, 0.2

for episode in range(500):
    state = 0
    for _ in range(20):
        action = random.randrange(actions) if random.random() < epsilon else int(np.argmax(Q[state]))
        next_state = max(0, state - 1) if action == 0 else min(goal, state + 1)
        reward = 10 if next_state == goal else -1
        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        state = next_state
        if state == goal:
            break

print("Learned Q-table:\n", np.round(Q, 2))
state, path = 0, [0]
while state != goal and len(path) < 10:
    action = int(np.argmax(Q[state]))
    state = max(0, state - 1) if action == 0 else min(goal, state + 1)
    path.append(state)
print("Learned path:", path)
