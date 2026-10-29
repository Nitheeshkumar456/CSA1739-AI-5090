import numpy as np
from sklearn.neural_network import MLPClassifier

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

model = MLPClassifier(hidden_layer_sizes=(4,), activation='relu',
                      solver='lbfgs', max_iter=2000, random_state=1)

model.fit(X, y)

predictions = model.predict(X)

print("Input:")
print(X)
print("Predictions:")
print(predictions)
print("Accuracy:", model.score(X, y))