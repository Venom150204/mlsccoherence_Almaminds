import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv('new_data.csv')

# Split dataset into features and labels
X = data['instruction']
y = data['response']

# Initialize TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# Initialize LinearSVC classifier
svm_classifier = LinearSVC()

# Create pipeline
pipeline = Pipeline([('tfidf', tfidf_vectorizer),
                     ('clf', svm_classifier)])

# Fit the pipeline
pipeline.fit(X, y)

# Save the trained model
joblib.dump(pipeline, 'trained_model.joblib')

# Test the trained model
def get_response(instruction):
    model = joblib.load('trained_model.joblib')
    response = model.predict([instruction])
    return response[0]

# Example usage
instruction = "I want to track my order."
print(get_response(instruction))