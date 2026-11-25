# User-based collaborative filtering with cosine similarity
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

users = ["A", "B", "C", "D"]
items = ["Movie1", "Movie2", "Movie3", "Movie4"]
ratings = np.array([
    [5, 4, 0, 0],
    [4, 5, 0, 1],
    [0, 0, 5, 4],
    [0, 1, 4, 5]
], dtype=float)

similarity = cosine_similarity(ratings)
target = 0
scores = similarity[target] @ ratings
rated = ratings[target] > 0
scores[rated] = -1
recommended = int(np.argmax(scores))
print("Similarity with other users:", np.round(similarity[target], 2))
print("Recommended item for user A:", items[recommended])
