from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "water_quality_model.pkl")
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        output = "Safe to Drink 💧" if prediction == 1 else "Not Safe 🚫"
    except Exception as e:
        output = f"Error: {e}"
    return render_template("index.html", prediction_text=f"Water Quality: {output}")

if __name__ == "__main__":
    app.run(debug=True)
