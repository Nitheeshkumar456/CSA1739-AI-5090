from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# Dataset
X = np.array([
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7],
    [6, 7, 8]
])

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)

X_reduced = pca.fit_transform(X_scaled)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_reduced.shape)
print("Reduced Data:")
print(X_reduced)