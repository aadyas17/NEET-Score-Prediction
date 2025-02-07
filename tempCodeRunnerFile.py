import requests
import pandas as pd
import urllib3

# ✅ Disable SSL warnings (optional, for `verify=False`)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ✅ Updated API Endpoints
CURRENT_QUIZ_API = "https://jsonkeeper.com/b/LLQT"
HISTORICAL_QUIZ_API = "https://api.jsonserve.com/rJvd7g"
HISTORICAL_API_ENDPOINT = "https://api.jsonserve.com/XgAgFJ"

def fetch_api_data(url):
    """Fetches data from an API endpoint"""
    try:
        response = requests.get(url, verify=False)  # Bypass SSL issue
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API Response from {url}: SUCCESS")
            return data
        else:
            print(f"❌ Error fetching data from {url}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Request Error: {e}")
        return None

# ✅ Fetch Data from APIs
def fetch_all_quiz_data():
    current_data = fetch_api_data(CURRENT_QUIZ_API)
    history_data = fetch_api_data(HISTORICAL_QUIZ_API)
    additional_history = fetch_api_data(HISTORICAL_API_ENDPOINT)

    return current_data, history_data, additional_history

# ✅ Convert JSON to DataFrames with more quizzes
def get_quiz_dataframes():
    current_data, history_data, additional_history = fetch_all_quiz_data()

    # ✅ Extract available keys correctly
    current_df = pd.DataFrame([current_data]) if current_data else pd.DataFrame()

    # ✅ Fix: Extract `questions`, `accuracy`, `score` from **ALL** quizzes
    all_questions = []

    # 🔹 Process first historical API response
    if history_data:
        if "quiz" in history_data and "questions" in history_data["quiz"]:
            for q in history_data["quiz"]["questions"]:
                q["topic"] = history_data["quiz"]["topic"]  # Add topic info
                q["accuracy"] = history_data.get("accuracy", None)  # ✅ Extract accuracy
                q["score"] = history_data.get("score", None)  # ✅ Extract score
                all_questions.append(q)

    # 🔹 Process additional historical API response (contains multiple quizzes)
    if additional_history:
        for record in additional_history:  # Loop through multiple quizzes
            if "quiz" in record and "questions" in record["quiz"]:
                for q in record["quiz"]["questions"]:
                    q["topic"] = record["quiz"]["topic"]  # Add topic info
                    q["accuracy"] = record.get("accuracy", None)  # ✅ Extract accuracy
                    q["score"] = record.get("score", None)  # ✅ Extract score
                    all_questions.append(q)

    # ✅ Create DataFrame with all quizzes
    history_df = pd.DataFrame(all_questions) if all_questions else pd.DataFrame()

    return current_df, history_df  # ✅ FIXED: Returning only 2 values

# ✅ Run and Save DataFrames
if __name__ == "__main__":
    current_df, history_df = get_quiz_dataframes()

    if not current_df.empty:
        current_df.to_csv("current_quiz.csv", index=False)
        print("✅ Saved: current_quiz.csv")

    if not history_df.empty:
        history_df.to_csv("history_quiz.csv", index=False)
        print("✅ Saved: history_quiz.csv")

    print("🎯 Data Fetching & Saving Completed Successfully!")
