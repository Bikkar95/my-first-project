from flask import Flask, jsonify
from flask_cors import CORS  # <-- YAHA CHECK KARO: Yeh line honi chahiye
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # <-- YAHA CHECK KARO: Yeh line bhi honi chahiye

FILE_PATH = os.path.join('files', 'Sample_Data_Analytics.csv')

@app.route('/')
def home():
    return "Backend Server Chal Raha Hai, Bikkar Bhai!"

@app.route('/api/data-preview', methods=['GET'])
def get_data_preview():
    try:
        if os.path.exists(FILE_PATH):
            df = pd.read_csv(FILE_PATH)
            df = df.fillna("") 
            data_dict = df.head(10).to_dict(orient='records')
            return jsonify({"status": "success", "data": data_dict})
        else:
            return jsonify({"status": "error", "message": f"File nahi mili! Path check karo: {FILE_PATH}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)