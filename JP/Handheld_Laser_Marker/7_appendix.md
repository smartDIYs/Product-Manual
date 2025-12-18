# 付録

<TODO:翻訳確認>

## バーコードスキャナの使い方

バーコードスキャナを使用する場合は、システムの設定を変更する必要があります。

### 設定方法

<div class="subentry">
通信設定
</div>

1. バーコードスキャナを加工機のUSBポートに接続します。
2. 設定 > 通信設定を開き、各項目を設定します。

<img src="./images/barcode_scanner/image3.png"  width="400px"/>

 項目 | 設定 |
|:---:|---|
| 通信モード | 通信1 |
| 繰り返しを許可 | 有効 |
| 起動時にクリア | 有効 |
| デバッグモード | 有効 |

※設定を行ったら、「再起動」をタップしてデバイスを再起動してください。

<div class="subentry">
システム設定 - バーコードスキャナ
</div>

<img src="./images/barcode_scanner/image5.png"  width="400px"/>
<img src="./images/barcode_scanner/image4.png"  width="400px"/>

 項目 | 設定 |
|:---:|---|
| 起動状態 | 起動 |
| システム起動後に自動開始 | 有効 |


### 使用方法

1. テキスト要素の「外部データ」を追加し、「編集」ボタンをタップします。
2. 変数名称を`sv1`に設定します。

<img src="./images/barcode_scanner/image7.png"  width="400px"/>

この状態でバーコードリーダーでコードを読み取ると、上記のテキスト要素の文字列が読み取った文字列に変更されます。