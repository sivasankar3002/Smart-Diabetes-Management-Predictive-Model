from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load('best_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [
        data['pregnancies'],
        data['glucose'],
        data['bloodpressure'],
        data['skinthickness'],
        data['insulin'],
        data['bmi'],
        data['dpf'],
        data['age']
    ]
    prediction = model.predict([features])
    suggestions = "Your health suggestions based on the prediction."

    return jsonify({
        'prediction': int(prediction[0]),
        'suggestions': suggestions
    })

if __name__ == '__main__':
    app.run(debug=True)
