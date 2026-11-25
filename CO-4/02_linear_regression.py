# Simple linear regression: predict marks from study hours
from sklearn.linear_model import LinearRegression
import numpy as np

hours = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
marks = np.array([35, 40, 50, 55, 65, 70])
model = LinearRegression().fit(hours, marks)
test_hours = np.array([[7]])
print("Slope:", round(model.coef_[0], 2))
print("Intercept:", round(model.intercept_, 2))
print("Predicted marks for 7 study hours:", round(model.predict(test_hours)[0], 2))
