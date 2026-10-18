from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model.pkl")
FEATURES = ["MedInc", "HouseAge", "AveRooms", "AveBedrms",
            "Population", "AveOccup", "Latitude", "Longitude"]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    X = pd.DataFrame([data])[FEATURES]
    price = model.predict(X)[0]
    return jsonify({"predicted_price_usd": round(float(price) * 100000)})

if __name__ == "__main__":
    app.run(debug=True)