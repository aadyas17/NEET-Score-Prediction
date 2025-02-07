import pandas as pd

def generate_recommendations():
    """Generates topic recommendations based on quiz history."""
    
    # ✅ Load the history data
    try:
        history_df = pd.read_csv("history_quiz.csv")
    except FileNotFoundError:
        print("❌ Error: history_quiz.csv not found! Please run fetch_data.py first.")
        return None

    # ✅ Debug: Print the available columns
    print("📌 history_df Columns:", history_df.columns)
    print("📊 history_df Preview:\n", history_df.head())

    # ✅ Fix: Use "topic" instead of "quiz.topic"
    if "topic" not in history_df.columns:
        print("❌ Error: 'topic' column not found in history_quiz.csv!")
        return None

    # ✅ Count number of attempts per topic
    topic_performance = history_df.groupby("topic")["selected_option"].count()

    # ✅ Generate recommendations based on least attempted topics
    recommendations = topic_performance.sort_values(ascending=True).head(5)  

    # ✅ Save recommendations
    recommendations.to_csv("recommendations.csv")
    print("✅ Saved: recommendations.csv")

    # ✅ Return recommendations
    return recommendations

# ✅ Run if executed directly
if __name__ == "__main__":
    recs = generate_recommendations()
    if recs is not None:
        print("🎯 Recommended Topics to Focus On:")
        print(recs)
