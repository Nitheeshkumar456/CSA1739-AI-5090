from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = [[1, 2], [2, 3], [3, 3],
     [6, 7], [7, 8], [8, 8]]

y = [0, 0, 0, 1, 1, 1]

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X, y)

# Predict
result = model.predict([[5, 6]])

print("Predicted Class:", result[0])