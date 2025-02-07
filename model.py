from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Load Data
history_df = pd.read_csv("history_quiz.csv")

# Prepare dataset
X = history_df[["accuracy", "score"]]  # Features
y = history_df["final_score"]  # Target

# Train a simple regression model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Predict future NEET rank
test_data = pd.DataFrame([[85, 20]], columns=["accuracy", "score"])
predicted_score = model.predict(test_data)  # Example: 80% accuracy, 32 score
print(f"Predicted NEET Score: {predicted_score}")
