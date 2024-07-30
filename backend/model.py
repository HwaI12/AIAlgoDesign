from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import pandas as pd

class RealEstateModel:
    def __init__(self):
        self.models = {
            'Linear': LinearRegression(),
            'Ridge': Ridge(),
            'Lasso': Lasso()
        }
        self.best_model = None
        self.feature_names = None

    def train(self, X, y, feature_names):
        self.feature_names = feature_names
        # データを訓練セットとテストセットに分割
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        best_score = -np.inf
        for name, model in self.models.items():
            if name == 'Linear':
                model.fit(self.X_train, self.y_train)
                score = model.score(self.X_test, self.y_test)
            else:
                param_grid = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100]}
                grid_search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error')
                grid_search.fit(self.X_train, self.y_train)
                score = -grid_search.best_score_
                model = grid_search.best_estimator_

            if score > best_score:
                best_score = score
                self.best_model = model

        print(f"Best model: {type(self.best_model).__name__}")
        if hasattr(self.best_model, 'alpha'):
            print(f"Best alpha: {self.best_model.alpha}")

    def predict(self, input_data):
        prediction = self.best_model.predict(input_data)
        return np.exp(prediction[0])  # 対数変換を戻す

    def evaluate(self):
        # テストデータで予測
        y_pred = self.best_model.predict(self.X_test)

        # 対数変換を戻す
        y_pred_exp = np.exp(y_pred)
        y_test_exp = np.exp(self.y_test)

        # 評価指標の計算
        mse = mean_squared_error(y_test_exp, y_pred_exp)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test_exp, y_pred_exp)
        r2 = r2_score(y_test_exp, y_pred_exp)

        # 決定係数（trainデータ）
        r2_train = self.best_model.score(self.X_train, self.y_train)

        # 特徴量の重要度（係数）
        if hasattr(self.best_model, 'coef_'):
            coef_df = pd.DataFrame({'feature': self.feature_names, 'coefficient': self.best_model.coef_})
            coef_df = coef_df.sort_values('coefficient', key=abs, ascending=False)
            print("\nFeature Importances:")
            print(coef_df)

        return {
            'mse': mse,
            'rmse': rmse,
            'mae': mae,
            'r2': r2,
            'r2_train': r2_train
        }