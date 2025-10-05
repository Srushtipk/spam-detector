import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

df = pd.read_csv('spam.csv', encoding='latin-1', usecols=['v1', 'v2'])
df.columns = ['label', 'message']

df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
X = df['message']
y = df['label_num']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

print("--- Data Preparation Complete ---")
print(f"Training data shape: {X_train_counts.shape}")
print(f"Testing data shape: {X_test_counts.shape}")
print("\nData is ready for model training.")

model = MultinomialNB()
model.fit(X_train_counts, y_train)

print("\n--- Model Training Complete ---")
print("Model trained successfully!")


joblib.dump(model, 'spam_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("\n--- Model and Vectorizer Saved ---")
print("Files 'spam_model.pkl' and 'vectorizer.pkl' have been created.")



