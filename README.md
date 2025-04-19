# **NEET Score Prediction**  
📊 *Predicting student performance using historical quiz data and Machine Learning.*  

## **📌 Project Overview**  
This project predicts **NEET scores** based on students' past quiz performances. It fetches quiz data from APIs, processes and analyzes trends, and provides recommendations to improve weak topics. The model leverages **Linear Regression** to estimate scores based on accuracy and quiz history.  

### **🔹 Features**  
✅ Fetches **current & historical** quiz data through APIs.  
✅ Cleans, processes, and analyzes quiz performance.  
✅ Trains a **Linear Regression model** for score prediction.  
✅ Identifies weak topics and **provides recommendations**.  
✅ Deploys a **Flask API** to serve predictions.  

---

## **⚙️ Setup & Installation**  
```sh
# Clone the repository
git clone https://github.com/aadyas17/NEET-Score-Prediction.git  
cd NEET-Score-Prediction  

# Install dependencies
pip install -r requirements.txt  

# Run the complete pipeline
python main.py  
```

---

## **🛠 Workflow & Methodology**  
1️⃣ **Fetch Quiz Data** → `fetch_data.py` retrieves quiz data from APIs & saves it as CSV.  
2️⃣ **Data Processing & Analysis** → `process_data.py` calculates accuracy & difficulty.  
3️⃣ **Train ML Model** → `model.py` trains a **Linear Regression** model for score prediction.  
4️⃣ **Generate Recommendations** → `recommendations.py` suggests weak topics to improve.  
5️⃣ **Deploy API** → `api.py` serves predictions via a Flask REST API.  

---

## **📊 Insights & Recommendations**  
| **Topic**                  | **Avg Score** | **Difficulty** |
|----------------------------|--------------|---------------|
| Genetics & Evolution       | 10.0         | 🔴 High       |
| Human Physiology           | 12.0         | 🟠 Medium     |
| Ecology & Environment      | 15.0         | 🟢 Easy       |

💡 *Recommendation: Focus on "Genetics and Evolution" for improvement!*  

---

## **🚀 Running the API**  
```sh
python api.py
```
🔹 **Example API Request:**  
```python
import requests
response = requests.get("http://127.0.0.1:5000/recommendations")
print(response.json())
```  

## **📸 Screenshot**  
![Dashboard Screenshot](https://github.com/user-attachments/assets/c49d126c-7be3-43fb-86ba-fac5d614f4ac)  

---

## **📽️ Video Demonstration**  
🎥 **Watch the demo**: [Click Here](https://drive.google.com/file/d/1Pp8wUQZ5xsPjity-WGP3uHtpOMbEa9pU/view?usp=drive_link)  

---

## **📜 License**  
🔹 This project is licensed under the **MIT License**.  

