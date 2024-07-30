import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.scaler = StandardScaler()

    def prepare_data(self):
        # 必要な特徴量を選択
        features = ['lat', 'lng', 'households', 'score', 'm2', 'p']
        X = self.df[features].copy()
        y = self.df['avg_sales'].copy()

        # 築年数の計算
        current_year = datetime.now().year
        X['age'] = current_year - pd.to_datetime(self.df['buildDate'], format='%Y%m').dt.year

        # 面積の対数変換
        X['log_m2'] = np.log(X['m2'])

        # 緯度と経度の交互作用項
        X['lat_lng_interaction'] = X['lat'] * X['lng']

        # 価格の対数変換
        y = np.log(y)

        # 最終的な特徴量の選択
        final_features = ['households', 'score', 'p', 'age', 'log_m2', 'lat', 'lng', 'lat_lng_interaction']
        X = X[final_features]

        # 欠損値を含む行を削除
        non_nan_mask = ~np.isnan(y) & ~X.isna().any(axis=1)
        X = X[non_nan_mask]
        y = y[non_nan_mask]

        # 特徴量のスケーリング
        X_scaled = self.scaler.fit_transform(X)
        
        return X_scaled, y, final_features

    def process_input(self, input_data):
        input_df = pd.DataFrame([input_data])
        
        # 'buildDate' カラムが存在するかチェック
        if 'buildDate' in input_df.columns:
            # 新しい特徴量の作成
            current_year = datetime.now().year
            input_df['age'] = current_year - pd.to_datetime(input_df['buildDate'], format='%Y%m').dt.year
        else:
            # 'buildDate' カラムが存在しない場合はエラーメッセージを返す
            raise ValueError("'buildDate' is required in the input data")
        
        # 数値型に変換
        input_df['m2'] = pd.to_numeric(input_df['m2'], errors='coerce')
        input_df['lat'] = pd.to_numeric(input_df['lat'], errors='coerce')
        input_df['lng'] = pd.to_numeric(input_df['lng'], errors='coerce')

        # 面積の対数変換
        input_df['log_m2'] = np.log(input_df['m2'])

        # 緯度と経度の交互作用項
        input_df['lat_lng_interaction'] = input_df['lat'] * input_df['lng']

        # 最終的な特徴量の選択
        final_features = ['households', 'score', 'p', 'age', 'log_m2', 'lat', 'lng', 'lat_lng_interaction']
        input_df = input_df[final_features]

        # 特徴量のスケーリング
        input_scaled = self.scaler.transform(input_df)
        return input_scaled
