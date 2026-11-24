import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# User-item rating matrix
data = {
    'Movie1': [5, 4, 0],
    'Movie2': [4, 5, 0],
    'Movie3': [0, 0, 5],
    'Movie4': [0, 0, 4]
}

df = pd.DataFrame(
    data,
    index=['User1', 'User2', 'User3']
)

# Calculate user similarity
similarity = cosine_similarity(df)

similarity_df = pd.DataFrame(
    similarity,
    index=df.index,
    columns=df.index
)

print("User Similarity:")
print(similarity_df.round(2))

# Recommend movies for User1
user = 'User1'

similar_users = similarity_df.loc[user].drop(user)

best_user = similar_users.idxmax()

recommendations = df.loc[best_user][
    df.loc[user] == 0
]

print("Recommended Movies:")
print(recommendations.index.tolist())