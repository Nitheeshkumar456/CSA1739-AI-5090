from textblob import TextBlob

# Input sentence
text = "I love artificial intelligence"

# Sentiment analysis
blob = TextBlob(text)

polarity = blob.sentiment.polarity

if polarity > 0:
    print("Positive Sentiment")
elif polarity < 0:
    print("Negative Sentiment")
else:
    print("Neutral Sentiment")

print("Polarity:", polarity)