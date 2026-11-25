# Hyperparameter tuning with GridSearchCV
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

X, y = load_iris(return_X_y=True)
parameters = {
    "C": [0.1, 1, 10],
    "kernel": ["linear", "rbf"],
    "gamma": ["scale", "auto"]
}
search = GridSearchCV(SVC(), parameters, cv=5)
search.fit(X, y)
print("Best parameters:", search.best_params_)
print("Best cross-validation accuracy:", round(search.best_score_ * 100, 2), "%")
