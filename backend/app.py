from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from data_processor import DataProcessor
from model import RealEstateModel
import numpy as np
import os
import traceback

app = Flask(__name__, static_folder='../frontend')
CORS(app, resources={r"/*": {"origins": "*"}})

try:
    # データの読み込みと前処理
    data_processor = DataProcessor('SeoulRealEstate.csv')
    X, y = data_processor.prepare_data()

    # モデルのトレーニング
    model = RealEstateModel()
    model.train(X, y)
except Exception as e:
    print(f"Error during initialization: {str(e)}")
    traceback.print_exc()
    model = None
    data_processor = None

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or data_processor is None:
        return jsonify({'error': 'Model or data processor not initialized properly'}), 500

    data = request.json
    try:
        processed_input = data_processor.process_input(data)
        prediction = model.predict(processed_input)
        return jsonify({'predicted_price': float(prediction)})
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)