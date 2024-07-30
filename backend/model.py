from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

class RealEstateModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        # データを訓練セットとテストセットに分割
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # モデルを訓練
        self.model.fit(self.X_train, self.y_train)

    def predict(self, input_data):
        prediction = self.model.predict(input_data)
        return np.round(prediction[0], 2)

    def evaluate(self):
        # テストデータで予測
        y_pred = self.model.predict(self.X_test)

        # 評価指標の計算
        mse = mean_squared_error(self.y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)

        # 決定係数（trainデータ）
        r2_train = self.model.score(self.X_train, self.y_train)

        return {
            'mse': mse,
            'rmse': rmse,
            'mae': mae,
            'r2': r2,
            'r2_train': r2_train
        }