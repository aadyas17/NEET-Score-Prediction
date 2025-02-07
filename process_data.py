import pandas as pd
from fetch_data import get_quiz_dataframes

# ✅ Fetch DataFrames
current_df, history_df = get_quiz_dataframes()  # ✅ FIXED CODE

# ✅ Save the current quiz data
if not current_df.empty:
    current_df.to_csv("current_quiz.csv", index=False)
    print("✅ Saved: current_quiz.csv")
else:
    print("❌ Warning: current_df is empty. No data saved!")

# ✅ Save the historical quiz data
if not history_df.empty:
    history_df.to_csv("history_quiz.csv", index=False)
    print("✅ Saved: history_quiz.csv")
else:
    print("❌ Warning: history_df is empty. No data saved!")

# ✅ Load CSVs and handle missing files
try:
    current_df = pd.read_csv("current_quiz.csv")
    history_df = pd.read_csv("history_quiz.csv")
    print("📂 Data successfully loaded!")
except FileNotFoundError:
    print("❌ Error: One or more CSV files are missing!")

# ✅ Example: Display Data Preview
print("\n📊 Current Quiz Data Preview:")
print(current_df.head())

print("\n📊 Historical Quiz Data Preview:")
print(history_df.head())

# ✅ Performance Analysis
def analyze_performance(history_df):
    """Analyzes student performance based on accuracy and score"""
    if history_df.empty:
        print("⚠️ No historical data available for performance analysis.")
        return

    print("\n📊 Performance Analysis:")
    avg_accuracy = history_df["accuracy"].mean()
    avg_score = history_df["score"].mean()

    print(f"✅ Average Accuracy: {avg_accuracy:.2f}%")
    print(f"✅ Average Score: {avg_score:.2f}")

# ✅ Difficulty Analysis
def analyze_difficulty(history_df):
    """Analyzes question difficulty based on topic-wise score"""
    if history_df.empty:
        print("⚠️ No historical data available for difficulty analysis.")
        return

    print("\n📊 Difficulty Analysis:")
    topic_difficulty = history_df.groupby("topic")["score"].mean().sort_values()
    print(topic_difficulty)

# ✅ Run the analysis
analyze_performance(history_df)
analyze_difficulty(history_df)
