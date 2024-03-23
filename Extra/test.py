import joblib
import pandas as pd

# Load the test dataset
test_data = pd.read_csv('new_data.csv')

# Extract features and labels from the test dataset
X_test = test_data['instruction']
y_test = test_data['response']

# Load the trained model
model = joblib.load('trained_model.joblib')

# Predict responses for the test dataset
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = (y_pred == y_test).mean()
print("Accuracy:", accuracy)
