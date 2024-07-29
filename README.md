# ソウル不動産価格予測ツール

大学の授業にて作成した成果物です。最小二乗法を用いた線形回帰モデルを使用して、ソウルの不動産価格を予測するウェブアプリケーションを開発しました。地図上で位置を選択し、物件の詳細を入力することで、価格を予測できます。

![](https://github.com/user-attachments/assets/e8df9689-fa5e-4b78-8090-370da8f6f0aa)

## 技術スタック
- バックエンド: Python (Flask)
- フロントエンド: HTML, CSS, JavaScript
- 機械学習: scikit-learn（最小二乗法による線形回帰）
- 地図: Leaflet.js

## 最小二乗法について
scikit-learnのLinearRegressionクラスを使用して最小二乗法を実装しています。

## セットアップ
1. リポジトリをクローン
    ```sh
    $ https://github.com/HwaI12/aialgodesign.git
    $ cd aialgodesign
    ```
2. Pythonパッケージをインストール
    ```sh
    $ pip install -r requirements.txt
    ```
3. サーバーを起動
    ```sh
    $ python backend/app.py
    ```

## 使用方法
1. 地図上で物件の位置をクリックします。
2. フォームに物件の詳細を入力します
    - 世帯数
    - 評価スコア（0-5）
    - 面積（m²）
    - 階数
    - 建築年
3. "価格を予測" ボタンをクリックします。
4. 最小二乗法により予測価格が表示されます。