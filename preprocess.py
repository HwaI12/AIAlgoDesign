# preprocess.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# データの読み込み
df = pd.read_csv('./SeoulRealEstate.csv')

# 必要な列を選択
features = ['lat', 'lng', 'households', 'buildDate', 'm2', 'p']
X = df[features].values
y = df['score'].values

# データの標準化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# トレーニングデータとテストデータへの分割
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# データの保存
np.save('X_train.npy', X_train)
np.save('X_test.npy', X_test)
np.save('y_train.npy', y_train)
np.save('y_test.npy', y_test)
np.save('scaler.npy', scaler)
