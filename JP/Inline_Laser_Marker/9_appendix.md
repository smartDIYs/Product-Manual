# 付録


## レンズの交換方法

レンズ交換・焦点の調整方法は、各製品の製品マニュアル「レンズ」に記載されている「レンズ交換」「高さ調整用レーザーポインター調整」の項目をご覧ください。

- [LM110C 製品マニュアル - https://www.smartdiys.com/assets/pdf/LM110C_Manual.pdf](https://www.smartdiys.com/assets/pdf/LM110C_Manual.pdf)
- [LM140R 製品マニュアル - https://www.smartdiys.com/assets/pdf/LM140R_Manual.pdf](https://www.smartdiys.com/assets/pdf/LM140R_Manual.pdf)
- [LM110U 製品マニュアル - https://www.smartdiys.com/assets/pdf/LM110U_Manual.pdf](https://www.smartdiys.com/assets/pdf/LM110U_Manual.pdf)

<br>

レンズを交換した場合は補正ファイルも変更する必要があります。
補正ファイルが存在しない場合は、[補正ファイルの作成](#補正ファイルの作成)を行なってください。

<div class="annotation">
※ レンズを頻繁に取り替える場合などは、ポインター以外の高さ調整方法（実測での運用やZ軸のメモリの活用等）もご検討ください。
</div>


<div style="page-break-before:always"></div>

## 補正ファイルの作成

この設定はパラメータタブの「加工エリア」画面にて行います。

<div class="danger">
※下記の作業は省略・中断せず、必ず全ての作業を最後まで実施してください。
</div>
<br>

<!-- <img src="./images/lends_correction/001.png" width="400px"/> -->

<div class="subheading">
1. 初期設定
</div>

1. **比率補正** の項目をX軸・Y軸ともに **100%** に設定します。
1. **駆動エリア・加工エリア** の設定値を確認します。<br>
※レンズごとに適切な設定値が異なりますので、[ガルバノスキャナ設定](#ガルバノスキャナ設定)を参照して値を入力してください。
1. **樽型** の補正値に **X軸: 1.05** / **Y軸: 0.96** を入力してください。

<img src="./images/lends_correction/1_initial_settings.png" width="400px"/>


<div class="subheading">
2. 補正値の調整と加工確認
</div>

<div class="subentry">
歪み補正
</div>

テスト加工を行います。**加工エリアより大きい平な素材**を配置し、高さ調整を行なってください。<br>
**補正テスト** をタップして加工を行い、現在の歪みを確認します。<br>
<span class="strongred">※タップと同時に加工が始まります。必ず保護メガネを着用して操作してください。</span>

テスト加工では下記の画像のような四角が加工されます。四角に歪みが発生している場合は上記の **樽型** の補正値を **±0.01** ずつ変更して補正テストを行なってください。この操作を繰り返し、許容できる範囲まで歪みを低減してください。

<!-- <img src="./images/lends_correction/2_test_marking.png" width="400px"/> -->

<table class="noframe">
<tr>
<td><img src="./images/lends_correction/2_test_marking.png" width="380px"/></td>
<td><img src="./images/lends_correction/3_test_mark_result.jpg" width="420px"/></td>
</tr>
</table>

<!-- <img src="./images/lends_correction/3_test_mark_result.jpg" width="400px"/> -->

樽型の補正を行うことで基本的な歪みは補正できます。さらに精度を上げたい場合は[ガルバノスキャナ補正](#ガルバノスキャナ補正)を参考に、傾斜・台形の補正値の調整もお試しください。


<div style="page-break-before:always"></div>

<div class="subentry">
大きさ補正
</div>

歪みがなくなったら、図形の縦幅と横幅を測定します。

<img src="./images/lends_correction/4_test_mark_scale.jpg" width="400px"/>


各軸の「>>」ボタンをそれぞれタップし、測定した数値を **「実サイズ」** に入力します。

<table class="noframe">
<tr>
<td><img src="./images/lends_correction/5_scale_correction_1.png" width="400px"/></td>
<td><img src="./images/lends_correction/6_scale_correction_2.png" width="400px"/></td>
</tr>
</table>

これにより **比率補正** の値が自動で修正されます。


再度「補正テスト」を行い、加工された四角のサイズが設定した加工エリアの値（115mm/205mm/305mm）と同じかどうかを確認します。
<img src="./images/lends_correction/7_test_marking.png" width="400px"/>

※レンズとのズレがある場合は比率補正を 100% に戻して補正テストを行い、計測および実サイズの入力を再度行ってください。


<div style="page-break-before:always"></div>

<div class="subheading">
3. 補正ファイルの保存
</div>

補正が完了したら補正ファイルを保存します。
「エクスポート」をタップし、ファイル名を入力し（ここでは「110」としています）、「確定」をタップしてください。

<table class="noframe">
<tr>
<td><img src="./images/lends_correction/8_export_cor.png" width="400px"/></td>
<td><img src="./images/lends_correction/9_export_cor_2.png" width="400px"/></td>
</tr>
</table>

調整ファイルの切り替えを行う場合、「インポート」を選択し、変更したいファイルを選択してください。
<td><img src="./images/lends_correction/10_import_cor.png" width="400px"/></td>


<div style="page-break-before:always"></div>

## ログの操作

### ログレベルの変更

パラメータタブの「システム設定」画面を開き、「高度な設定」を表示します。
ログレベルを「デバッグ」に設定すると、より詳細なログを取得できます。（ログファイルの容量は大きくなります）
<img src="./images/_change_log_level.png" width="400px"/>


### ログファイルのエクスポート

あらかじめ USB メモリを本体パネルの USB ポートに接続します。<br>
ファイルタブの「管理」画面を開き、ログフォルダ内で対象のログファイルを選択して「コピー」ボタンをタップします。
続いて USB メモリのフォルダを選択し、「ペースト」ボタンをタップします。

<table class="noframe">
<tr>
<td><img src="./images/_log_export_1.png" width="400px"/></td>
<td><img src="./images/_log_export_2.png" width="400px"/></td>
</tr>
</table>

<div style="page-break-before:always"></div>

## ユーザーデータのバックアップ

あらかじめ USB メモリを本体パネルの USB ポートに接続します。<br>
ファイル画面を開き、右上のメニューボタンをタップして「ユーザーデータをバックアップします」を選択します。
続いてUSBメモリフォルダを選択し、「確定」ボタンをタップします。

<div class="annotation">
バックアップファイルには加工ファイルやレンズ補正ファイル、ログデータなどが含まれます。
</div>

<table class="noframe">
<tr>
<td><img src="./images/_backup_menu.png" width="400px"/></td>
<td><img src="./images/_backup_to_usb.png" width="400px"/></td>
</tr>
</table>



## フォントの追加

パラメータタブの「言語とフォント」画面を表示し、画面中央右側の「フォント追加」ボタンから追加してください。
<img src="./images/_add_font.png" width="400px"/>

