from sklearn.tree import DecisionTreeClassifier

# Dataset
X = [[1, 20], [2, 25], [3, 30],
     [6, 60], [7, 65], [8, 70]]

y = [0, 0, 0, 1, 1, 1]

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Prediction
result = model.predict([[2, 28]])

print("Predicted Class:", result[0])