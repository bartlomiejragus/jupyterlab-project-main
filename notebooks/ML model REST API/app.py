from flask import Flask, request, jsonify
from models import Perceptron  # Ensure this matches your file and class structure
import numpy as np
import joblib

app = Flask(__name__)

# Load the model at application startup
model = joblib.load('perceptron_model.joblib')

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    x1 = request.args.get('x1', default=0.0, type=float)
    x2 = request.args.get('x2', default=0.0, type=float)
    prediction = model.predict(np.array([[x1, x2]]))
    response = {'features': {'x1': x1, 'x2': x2}, 'predicted_class': int(prediction[0])}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
