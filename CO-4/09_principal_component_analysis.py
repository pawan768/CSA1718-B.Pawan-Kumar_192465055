# PCA dimensionality reduction on the Iris dataset
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X_scaled = StandardScaler().fit_transform(iris.data)
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_scaled)
print("Original shape:", iris.data.shape)
print("Reduced shape:", X_reduced.shape)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("First 5 reduced rows:\n", X_reduced[:5])
