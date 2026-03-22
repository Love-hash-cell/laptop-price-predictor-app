from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import os

# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Initialize app
app = Flask(__name__)
CORS(app)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)

        # Prepare input data
        input_data = []
        for col in columns:
            val = data.get(col)

            # Handle different cases (ram vs RAM etc.)
            if val is None:
                val = data.get(col.lower())
            if val is None:
                val = data.get(col.capitalize())

            # Default = 0 if not found
            input_data.append(float(val) if val is not None else 0)

        # Prediction
        prediction = model.predict([input_data])[0]

        return jsonify({
            "predicted_price": float(prediction)
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "error": str(e)
        })

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    