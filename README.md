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

## **⚙️ Setup**  
```sh
git clone https://github.com/aadyas17/NEET-Score-Prediction.git
cd NEET-Score-Prediction
pip install -r requirements.txt
python main.py
```
## **🛠 Methodology**  
1️⃣ **Data Fetching** → `fetch_data.py` pulls quiz data from APIs (CSV format).  
2️⃣ **Processing & Analysis** → `process_data.py` computes accuracy & difficulty.  
3️⃣ **ML Model** → `model.py` trains a Linear Regression model for score prediction.  
4️⃣ **Recommendations** → `recommendations.py` identifies weak topics.  
5️⃣ **Flask API** → `api.py` serves predictions via REST API.  

## **📊 Insights**  
| Topic                     | Avg Score | Difficulty |
|---------------------------|-----------|-----------|
| Genetics & Evolution      | 10.0      | High      |
| Human Physiology         | 12.0      | Medium    |
| Ecology & Environment    | 15.0      | Easy      |

*💡 Focus more on "Genetics and Evolution"!*  

## **🚀 Running API**  
```sh
python api.py
```
**Example Request:**  
```python
import requests
response = requests.get("http://127.0.0.1:5000/recommendations")
print(response.json())
```  
## **Screenshot** 
![image](https://github.com/user-attachments/assets/c49d126c-7be3-43fb-86ba-fac5d614f4ac)

## 📽️ Video Demonstration  
Watch the demo video ((https://drive.google.com/file/d/1Pp8wUQZ5xsPjity-WGP3uHtpOMbEa9pU/view?usp=drive_link)).

## **📜 License**  
This project is licensed under the **MIT License**.  

