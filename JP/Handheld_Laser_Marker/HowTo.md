# マニュアル作成環境構築

本マニュアルの作成に必要なソフトウェア等をまとめます。
基本的にはVSCodeを使用して編集を行い、いくつかのプラグインやスクリプトにてPDFを作成します。

## VSCodeプラグイン

### Markdown Preview Enhanced
https://shd101wyy.github.io/markdown-preview-enhanced/#/

mdファイルをPDFへ変換する方法として採用しています。VSコード上のプレビュー画面と出力PDFの一致度が高く、PDF出力も高速です。


## Pythonスクリプト

`merge.py`を実行すると、`__indexes.json`に記載された情報をもとに各セクションの記事を一つにまとめ、ヘッダ番号を更新したファイルを出力します。

ページ番号は`page_numbers.json`に定義されており、目次の作成に使用されます。`page_fetch.py`を実行すると`README.md`の目次内容と`README.pdf`を内容を利用して目次ページ番号を取得します。

具体的な更新手順は下記のとおりです。
1. `python merge.py`を実行
2. プラグインで`README.md`をPDFに変換
3. `python page_fetch.py`を実行
4. `python merge.py`を再実行
2. プラグインで`README.md`をPDFに再変換