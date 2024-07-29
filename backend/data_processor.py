import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.scaler = StandardScaler()

    def prepare_data(self):
        # 必要な特徴量を選択
        features = ['lat', 'lng', 'households', 'score', 'm2', 'p']
        X = self.df[features].copy()  # .copyを使用してビューではなくコピーを作成
        y = self.df['avg_sales'].copy()

        # buildDateを年に変換
        X['year'] = pd.to_datetime(self.df['buildDate'], format='%Y%m').dt.year
        
        # 欠損値を含む行を削除
        non_nan_mask = ~np.isnan(y)
        X = X[non_nan_mask]
        y = y[non_nan_mask]

        # 特徴量のスケーリング
        X_scaled = self.scaler.fit_transform(X)
        
        return X_scaled, y

    def process_input(self, input_data):
        input_df = pd.DataFrame([input_data])
        input_scaled = self.scaler.transform(input_df)
        return input_scaled