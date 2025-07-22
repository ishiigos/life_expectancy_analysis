import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 0 = all logs, 1 = filter INFO, 2 = filter INFO+WARNINGS, 3 = only ERRORS

from flask import Flask, render_template, request
import numpy as np
import joblib
import tensorflow as tf

# Initialize app
app = Flask(__name__)

# Load models
ml_model = joblib.load("models/final_rf_model.pkl")
preprocessor = joblib.load("models/life_expectancy_scaler.pkl")
dl_model = tf.keras.models.load_model("models/life_expectancy_dl_model.h5")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Get form data
            user_input = [float(request.form.get(f'feature{i}')) for i in range(1, 16)]
            model_type = request.form.get("model")

            # Preprocess
            processed_input = preprocessor.transform([user_input])

            if model_type == "ml":
                prediction = ml_model.predict(processed_input)[0]
            else:
                prediction = dl_model.predict(processed_input)[0][0]

            prediction = round(prediction, 2)

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)