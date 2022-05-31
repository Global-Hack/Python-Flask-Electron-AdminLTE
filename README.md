# Python-Flask-Electron-AdminLTE
venv仮想環境にて、AdminLTEを反映させます。これは使いやすいプレーンな状況を想定していますので、スタートアップにお役立てください。

## まず仮想環境を用意
参考：[【簡単Python】venvでサクッと仮想環境を用意してみる【Mac開発環境構築】](https://global-hack.com/blog/archives/93)

## Electronを入れる
仮想環境内のディレクトリにて下記コマンドを実行
```bash
npm install --location=global electron
```

## PythonのフレームワークFlaskを入れる
```bash
pip install Flask
```

## 初期化
```bash
npm init -y
```
## requestのインストール
```bash
npm install --save request
npm install --save request-promise
```

## Node.js上で、javascriptコード・Pythonコード間の処理をするためのpython-shell
```bash
npm install --save python-shell
```
