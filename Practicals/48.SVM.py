from sklearn.svm import SVC

# Dataset
X = [[1, 2], [2, 3], [3, 3],
     [6, 7], [7, 8], [8, 8]]

y = [0, 0, 0, 1, 1, 1]

# Create SVM model
model = SVC(kernel='linear')

# Train model
model.fit(X, y)

# Prediction
result = model.predict([[2, 2]])

print("Predicted Class:", result[0])