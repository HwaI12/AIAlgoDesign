from sklearn.linear_model import LinearRegression
import numpy as np

class RealEstateModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, input_data):
        prediction = self.model.predict(input_data)
        return np.round(prediction[0], 2)