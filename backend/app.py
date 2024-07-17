from flask import Flask, request, jsonify
from flask_cors import CORS
from data_processor import DataProcessor
from model import RealEstateModel

app = Flask(__name__)
CORS(app)

data_processor = DataProcessor('SeoulRealEstate.csv')
model = RealEstateModel(data_processor.X, data_processor.y)

@app.route('/predict', methods=['POST'])
def predict():
    features = request.json
    prediction = model.predict(features)
    return jsonify({'predicted_score': prediction})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_processor.get_data())

if __name__ == '__main__':
    app.run(debug=True, port=8080)