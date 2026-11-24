from sklearn.tree import DecisionTreeClassifier

# Dataset
X = [[1, 2], [2, 3], [3, 4],
     [6, 7], [7, 8], [8, 9]]

y = [0, 0, 0, 1, 1, 1]

# Create Decision Tree
model = DecisionTreeClassifier(random_state=42)

# Train
model.fit(X, y)

# Predict
result = model.predict([[7, 7]])

print("Predicted Class:", result[0])