# Python-Flask-Electron-AdminLTE
venv仮想環境にて、AdminLTEを反映させます。これは使いやすいプレーンな状況を想定していますので、スタートアップにお役立てください。

## 1.まず仮想環境を用意
venv仮想環境構築がわからない方は下記を参考にしてください。
参考：[【簡単Python】venvでサクッと仮想環境を用意してみる【Mac開発環境構築】](https://global-hack.com/blog/archives/93)

## 2.Electronを入れる
仮想環境内のディレクトリにて下記コマンドを実行
```bash
npm install --location=global electron
```

## 3.PythonのフレームワークFlaskを入れる
```bash
pip install Flask
```

## 4.初期化
```bash
npm init -y
```

## 5.requestのインストール
```bash
npm install --save request
npm install --save request-promise
```

## 6.Node.js上で、javascriptコード・Pythonコード間の処理をするためのpython-shell
```bash
npm install --save python-shell
```

## 7.リポジトリをローカルにclone
```bash
git clone https://github.com/Global-Hack/Pythone-Flask-Electron-AdminLTE.git
```
Python-Flask-Electron-AdminLTEディレクトリの中身だけを使いますので、当該ディレクトリから出してお使いください。

中身だけcloneする方法もありますのでご参考までに。
```bash
git init
git remote add origin https://github.com/Global-Hack/Pythone-Flask-Electron-AdminLTE.git
git fetch --all --prune
git pull origin master
```

# 動作の確認方法
```bash
electron .
```

あとは煮るなり焼くなり好きにしてください！
