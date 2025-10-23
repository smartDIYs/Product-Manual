# マニュアル作成環境構築

本マニュアルの作成に必要なソフトウェア等をまとめます。
基本的にはVSCodeを使用して編集を行い、いくつかのプラグインやスクリプトにてPDFを作成します。

## VSCodeプラグイン

### Markdown Preview Enhanced
https://shd101wyy.github.io/markdown-preview-enhanced/#/

mdファイルをPDFへ変換する方法として採用しています。VSコード上のプレビュー画面と出力PDFの一致度が高く、PDF出力も高速です。


## Pythonスクリプト

`merge.py`を実行すると、`__indexes.json`に記載された情報をもとに各セクションの記事を一つにまとめ、ヘッダ番号を更新したファイルを出力します。

