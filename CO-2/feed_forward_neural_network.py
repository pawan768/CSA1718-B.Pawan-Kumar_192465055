# Feed-forward neural network for XOR (NumPy only)
import numpy as np

np.random.seed(1)
X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
y = np.array([[0],[1],[1],[0]], dtype=float)

W1 = np.random.randn(2, 4)
b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 1)
b2 = np.zeros((1, 1))
sigmoid = lambda z: 1 / (1 + np.exp(-z))

for epoch in range(10000):
    h = sigmoid(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)
    error = out - y
    d2 = error * out * (1 - out)
    d1 = (d2 @ W2.T) * h * (1 - h)
    W2 -= 1.0 * (h.T @ d2) / len(X)
    b2 -= 1.0 * d2.mean(axis=0, keepdims=True)
    W1 -= 1.0 * (X.T @ d1) / len(X)
    b1 -= 1.0 * d1.mean(axis=0, keepdims=True)

print("XOR predictions:")
for row, prediction in zip(X, out):
    print(row.astype(int), "->", int(prediction[0] >= 0.5), "(probability:", round(float(prediction[0]), 3), ")")
