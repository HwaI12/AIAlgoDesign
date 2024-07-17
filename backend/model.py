import numpy as np

class RealEstateModel:
    def __init__(self, X, y):
        self.X = np.c_[np.ones(X.shape[0]), X]  # Add bias term
        self.y = y
        self.theta = self.least_squares()

    def least_squares(self):
        return np.linalg.inv(self.X.T @ self.X) @ self.X.T @ self.y

    def predict(self, X):
        X_with_bias = np.c_[np.ones(X.shape[0]), X]
        return X_with_bias @ self.theta