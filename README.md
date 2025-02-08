# NEET-Score-Prediction
*Predicting student performance based on historical quiz data using Machine Learning.*  

## **📜 Project Overview**  
This project predicts **NEET scores** based on students' historical quiz performances. It fetches quiz data from APIs, processes and analyzes performance trends, and provides recommendations for improvement. The model is built using **Linear Regression** to estimate scores based on accuracy and past quiz results.  

### **🎯 Key Features:**  
✅ Fetches **current and historical** quiz data from APIs.  
✅ Cleans, processes, and analyzes quiz performance.  
✅ Builds an **ML model** to predict NEET scores.  
✅ Provides **recommendations** based on weak topics.  
✅ Deploys a **Flask API** to serve predictions.  

## **⚙️ Setup Instructions**  
### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/aadyas17/NEET-Score-Prediction.git
cd NEET-Score-Prediction
```

### **3️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Full Pipeline**  
```sh
python main.py
```

## **🛠 Approach & Methodology**  

### **🔹 Step 1: Data Fetching**  
- Uses `fetch_data.py` to **pull quiz data** from API endpoints.  
- Saves it in CSV files (`current_quiz.csv`, `history_quiz.csv`).  

### **🔹 Step 2: Data Processing & Analysis**  
- `process_data.py` cleans and analyzes the data.  
- Computes **accuracy**, **average score**, and **difficulty levels**.  

### **🔹 Step 3: Machine Learning Model**  
- `model.py` trains a **Linear Regression model** using `sklearn`.  
- Predicts **NEET scores** based on accuracy and past scores.  

### **🔹 Step 4: Generating Recommendations**  
- `recommendations.py` identifies weak topics and suggests focus areas.  

### **🔹 Step 5: Flask API Deployment**  
- `api.py` provides a **REST API** for predicting NEET scores.  
- Can be queried using `POST` requests.  

---

## **📊 Insights & Visualizations**  
| Topic                         | Avg Score | Difficulty Level |
|--------------------------------|-----------|-----------------|
| **Genetics and Evolution**     | 10.0      | High           |
| **Human Physiology**           | 12.0      | Medium         |
| **Ecology and Environment**    | 15.0      | Easy           |
| **Structural Organisation**    | 15.5      | Easy           |

*💡 Based on analysis, "Genetics and Evolution" needs more focus!*  

---

## **🚀 Running the Flask API**  
### **1️⃣ Start the API Server**  
```sh
python api.py
```
### **2️⃣ Make a Prediction Request (Example)**  
```python
import requests
response = requests.get("http://127.0.0.1:5000/recommendations")
print(response.json())
```

## **Screenshot** 
![image](https://github.com/user-attachments/assets/c49d126c-7be3-43fb-86ba-fac5d614f4ac)

## **📜 License**  
This project is licensed under the **MIT License**.  

