import numpy as np
from sklearn.linear_model import LinearRegression

class RealEstateModel:
    def __init__(self, X, y):
        self.model = LinearRegression()
        self.model.fit(X, y)

    def predict(self, features):
        input_data = np.array([[
            features['m2'],
            features['p'],
            features['buildDate']
        ]])
        return self.model.predict(input_data)[0]