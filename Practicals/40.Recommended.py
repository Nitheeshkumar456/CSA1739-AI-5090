import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# User-item rating matrix
ratings = np.array([
    [5, 4, 0, 0],
    [4, 5, 0, 0],
    [0, 0, 5, 4],
    [0, 0, 4, 5]
], dtype=float)

# Calculate user similarity
similarity = cosine_similarity(ratings)

# Select user
user = 0

# Find most similar user
similar_user = np.argsort(
    similarity[user]
)[-2]

# Recommend unrated items
recommendations = np.where(
    ratings[user] == 0
)[0]

print("Similar User:", similar_user)
print("Recommended Items:", recommendations + 1)