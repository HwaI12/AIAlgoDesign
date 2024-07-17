from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from data_processor import DataProcessor
from model import RealEstateModel
import os

app = Flask(__name__)
CORS(app)

data_processor = DataProcessor('SeoulRealEstate.csv')
model = RealEstateModel(data_processor.X_scaled, data_processor.y)

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def send_frontend(path):
    return send_from_directory('../frontend', path)

@app.route('/predict', methods=['POST'])
def predict():
    features = request.json
    prediction = model.predict(data_processor.scale_input(features))
    return jsonify({'predicted_score': float(prediction)})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_processor.get_data())

if __name__ == '__main__':
    app.run(debug=True)