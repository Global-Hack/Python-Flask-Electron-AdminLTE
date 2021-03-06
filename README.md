# Python-Flask-Electron-AdminLTE
venv仮想環境にて、AdminLTEを反映させます。これは使いやすいプレーンな状況を想定していますので、スタートアップにお役立てください。

## 1.まず仮想環境を用意
venv仮想環境構築がわからない方は下記を参考にしてください。

参考：[【簡単Python】venvでサクッと仮想環境を用意してみる【Mac開発環境構築】](https://global-hack.com/blog/archives/93)

## 2.リポジトリをローカルに
中身だけが必要なので下記のコマンドになります。
```bash
git init
git remote add origin https://github.com/Global-Hack/Python-Flask-Electron-AdminLTE.git
git fetch --all --prune
git pull
```

## 3.Electronを入れる
仮想環境内のディレクトリにて下記コマンドを実行
```bash
npm install electron
```

## 4.PythonのフレームワークFlaskを入れる
```bash
pip install Flask
```

## 5.初期化
```bash
npm init -y
```

## 6.requestのインストール
```bash
npm install --save request
npm install --save request-promise
```

## 7.Node.js上で、javascriptコード・Pythonコード間の処理をするためのpython-shell
```bash
npm install --save python-shell
```

## 8.動作の確認方法
```bash
electron .
```
## 9.もう少し細かい説明が必要な方
下記リンクを参考に実践してみてください！

参考：[超絶簡単！Python+Flask+Electron+AdminLTEで管理画面を構築してみる！](https://global-hack.com/blog/archives/99)

あとは煮るなり焼くなり好きにしてください！
