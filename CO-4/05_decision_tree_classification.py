# Decision tree classification using the Iris dataset
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=1
)
tree = DecisionTreeClassifier(criterion="entropy", random_state=1)
tree.fit(X_train, y_train)
predictions = tree.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")
print("Predicted:", iris.target_names[predictions[0]])
