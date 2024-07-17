import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.X = self.data[['m2', 'p', 'buildDate']]
        self.y = self.data['score']  # 'price' の代わりに 'score' を使用

        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(self.X)

    def get_data(self):
        return self.data.to_dict(orient='records')

    def scale_input(self, input_data):
        return self.scaler.transform(input_data)