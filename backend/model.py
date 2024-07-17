from sklearn.linear_model import LinearRegression

class RealEstateModel:
    def __init__(self, X, y):
        self.model = LinearRegression()
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)[0]