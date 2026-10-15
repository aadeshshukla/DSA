from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
messages = [
    "win money now",
    "claim your free prize",
    "meeting at 10 am",
    "let us discuss the project",
    "free money offer",
    "project meeting tomorrow"
]

labels = [
    "Spam",
    "Spam",
    "Not Spam",
    "Not Spam",
    "Spam",
    "Not Spam"
]

# Convert text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X, labels)

# Test the model
test_message = ["free prize money"]
test_X = vectorizer.transform(test_message)

prediction = model.predict(test_X)

print("Message:", test_message[0])
print("Prediction:", prediction[0])
