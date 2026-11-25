# Basic sentiment analysis using TF-IDF and Naive Bayes
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "I love this product", "This is wonderful and excellent",
    "Very happy with the service", "I hate this product",
    "This is terrible and poor", "Very disappointed and bad"
]
labels = ["positive", "positive", "positive", "negative", "negative", "negative"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB().fit(X, labels)

sentence = input("Enter a review: ")
prediction = model.predict(vectorizer.transform([sentence]))[0]
print("Sentiment:", prediction)
