from flask import Flask, jsonify
import pandas as pd
from recommendations import generate_recommendations

app = Flask(__name__)

# ✅ Root URL to check if API is running
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is running!"})

# ✅ Get recommendations
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    try:
        recommendations = generate_recommendations()
        
        # Ensure recommendations are JSON serializable
        if isinstance(recommendations, pd.Series):
            recommendations = recommendations.to_dict()
        
        return jsonify({"status": "success", "recommendations": recommendations})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500  # Return error message

if __name__ == '__main__':
    app.run(debug=True)
