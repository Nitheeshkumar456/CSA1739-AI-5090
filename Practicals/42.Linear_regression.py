import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Prediction
prediction = model.predict([[6]])

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Predicted value:", prediction[0])