from textblob import TextBlob

# Input sentence
text = input("Enter a sentence: ")

# Sentiment analysis
blob = TextBlob(text)

polarity = blob.sentiment.polarity

print("Polarity:", polarity)

if polarity > 0:
    print("Positive Sentiment")
elif polarity < 0:
    print("Negative Sentiment")
else:
    print("Neutral Sentiment")