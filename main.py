import pandas as pd
from fetch_data import fetch_all_quiz_data
from process_data import analyze_performance, analyze_difficulty
from recommendations import generate_recommendations

if __name__ == "__main__":
    print("\n🔄 Fetching Quiz Data...")
    current_data, history_data, additional_history = fetch_all_quiz_data()

    # ✅ Extract questions from `quiz` before converting to DataFrame
    if isinstance(history_data, dict) and "quiz" in history_data and "questions" in history_data["quiz"]:
        history_df = pd.DataFrame(history_data["quiz"]["questions"])
    else:
        history_df = pd.DataFrame()  # Empty DataFrame if no valid data

    # ✅ Ensure history data exists before analysis
   # ✅ Only update `history_df` if new data is not empty
if not history_df.empty:
    print("\n📊 Analyzing Data...")
    analyze_performance(history_df)
    analyze_difficulty(history_df)

    print("\n🎯 Generating Recommendations...")
    print(generate_recommendations(history_df))
else:
    print("⚠️ Warning: No historical data found. Using previously loaded data.")

    print("\n✅ Process Completed Successfully!")
