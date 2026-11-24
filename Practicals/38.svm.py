from sklearn import svm

# Dataset
X = [[1, 2], [2, 3], [3, 3],
     [6, 7], [7, 8], [8, 8]]

y = [0, 0, 0, 1, 1, 1]

# Create SVM model
model = svm.SVC(kernel='linear')

# Train
model.fit(X, y)

# Predict
result = model.predict([[7, 7]])

print("Predicted Class:", result[0])