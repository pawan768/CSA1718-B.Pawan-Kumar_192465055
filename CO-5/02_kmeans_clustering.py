# K-Means clustering on sample 2D data
from sklearn.cluster import KMeans
import numpy as np

X = np.array([
    [1, 2], [1, 4], [1, 0],
    [10, 2], [10, 4], [10, 0],
    [5, 7], [6, 8], [4, 8]
])
model = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = model.fit_predict(X)
print("Data points and cluster labels:")
for point, label in zip(X, labels):
    print(point, "-> Cluster", label)
print("Cluster centers:\n", model.cluster_centers_)
