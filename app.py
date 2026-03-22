from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

app = Flask(__name__)
CORS(app)   # 🔥 MUST BE HERE

from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    input_data = [data.get(col, 0) for col in columns]
    
    prediction = model.predict([input_data])[0]
    
    return jsonify({
        "predicted_price": float(prediction)
    })

if __name__ == "__main__":
    app.run(debug=True)
    