# クイックスタート

この章では、ログインから加工、保存、終了までの基本操作を順番に説明します。

## 本体の起動

電源ケーブルをコンセントに接続し、本体側面の電源スイッチをオンにします。緊急停止ボタンが押されいる場合は矢印の向きに回して解除してください。

<img src="./images/photos/power_switch.jpg"  width="380px"/>

## ログイン

ログインボタンをタップするとログインダイアログが表示されます。必要に応じてログインを行なってください。

<img src="./images/quickstart_login.png" width="540px"/>


<div class="annotation">
管理者の初期パスワードは「123」です。<br>

ログインユーザー（または未ログイン）ごとに操作を制限することも可能です。詳細は [ユーザー管理](#ユーザー管理) をご確認ください。

</div>


<div style="page-break-before:always"></div>


## 新規ファイルの作成

メニューバーの「新規」ボタンをタップして新規ファイルを開きます。

<img src="./images/quickstart_new_file.png" width="540px"/>

<div class="annotation">
「編集中のファイルを保存しますか？」と表示された場合、「OK」をタップすると現在のファイルの変更内容が保存されます。「キャンセル」をタップすると変更内容が破棄されます。
</div>


## データ作成

<div class="subentry">オブジェクトの作成</div>

ここでは一例として、刻印ごとに「ABC0000」「ABC0001」「ABC0002」... とカウントアップしていくテキストオブジェクトを作成します。
この場合「ABC」という 固定テキスト要素 と「0001, 0002, 0003, ...」とカウントアップする シリアル番号要素 を組み合わせて実現します。

<div class="annotation">

「テキスト」要素は固定文字列を表現します。「シリアル番号」要素は加工ごとにカウントアップを行う可変文字列を表現します。
その他、各要素の詳細は [テキスト](#テキスト) をご確認ください。

</div>

**加工例**

<img src="./images/photos/handgun_result.jpg"  width="300px"/>


<div style="page-break-before:always"></div>


**テキストオブジェクトの作成**

オブジェクトパネルにある「テキスト」アイコンをタップします。<img src="./images/quickstart_add_text_icon.png" style="display:inline;margin-bottom:0;" width="30px"/>



テキストオブジェクトを新規作成すると、「テキスト」要素が自動的に登録されています。

文字列リストにある該当の「テキスト」要素を選択し、「編集」ボタンをタップします。
表示されたダイアログの入力フォームに「ABC」と入力して「OK」ボタンをタップします。（大文字を入力する場合は`Caps`を有効にします）

<!-- <img src="./images/quickstart_text_edit_input.png"  width="400px"/> -->

<table class="noframe">
<tr>
<td style="padding:0px"><img src="./images/quickstart_text_edit.png" width="350px" /></td>
<td style="padding:0px; width:5px"></td>
<td style="padding:0px"><img src="./images/quickstart_text_edit_input.png" width="350px" /></td>
</tr>
</table>


次に「シリアル番号」要素を追加します。「シリアル番号」をタップすると文字列リストに追加されます。
プレビューには各要素が連結された文字列が表示されます。

<img src="./images/quickstart_add_serial_element.png" width="460px"/>


**フォントの編集**<br>

フォントの「選択」ボタンをタップし、「輪郭線」フォントから「Arial Unicode MS」を選択します。


<img src="./images/quickstart_text_font_select.png" width="260px"/>

テキスト修正ダイアログ画面右上の「OK」ボタンをタップしてホーム画面に戻ります。


<div style="page-break-before:always"></div>


<div class="subentry">オブジェクトの編集</div>

ここでは作成したオブジェクトに対して位置や大きさの調整、塗りつぶしなどの設定を行います。


**オブジェクトの選択**<br>
グラフィックビューに表示されているテキストオブジェクトをタップすると、オブジェクトが選択状態になります。
選択状態のオブジェクトは緑色の枠線が表示されます。（プリセットの「点」オブジェクトを除く）

**位置の調整**<br>
テキストオブジェクトが選択された状態で、位置を X:0 / Y:0 に設定します。<br>
※コントロールパネルの「中央揃え」をタップすることでも同等の操作が可能です。

<img src="./images/quickstart_text_position_edit.png"  width="540px"/>



**塗潰し設定**<br>
テキストオブジェクトが選択された状態で、コントロールパネルの「塗潰し」をタップします。
表示されたダイアログで下記の設定を行います。パラメータの詳細は  [塗りつぶし](#塗りつぶし)  をご確認ください。

<img src="./images/quickstart_text_fill_edit.png"  width="540px"/>

<!-- <div class="fixed-table">

| 項目 | 設定 |
|:---:|:--:|
| 塗潰し有効 | 有効 |
| 塗潰し角度 | 0.00 度 |
| 線間隔 | 0.15 mm |
| 輪郭 | 有効 |
| 塗潰し種類 | 通常 |

</div> -->

<!-- 設定を行うと、グラフィックビューに塗りつぶされた状態のテキストが表示されます。 -->


<div style="page-break-before:always"></div>

## パラメータ設定

コントロールパネルの パラメータ「変更」ボタンをタップします。表示されたパラメータ設定画面で加工パラメータを設定します。各設定項目の詳細は [加工パラメータ](#加工パラメータ)  をご確認ください。

<img src="./images/quickstart_parameter_edit.png"  width="520px"/>


**参考パラメータ表**

<div class="fixed-table">

| 素材 | 加工速度 | パワー | 周波数 |
|:---|:---:|:---:|:---:|
| ステンレス | 1000 | 60 | 30 |
| MDF | 100 | 50 | 50 |
| ABS樹脂 | 2000 | 20 | 30 |

</div>


<div class="annotation">
加工パラメータは加工素材や加工内容、要求品質等に応じて調整を行なってください。
</div>


<div style="page-break-before:always"></div>


## 加工操作

<span class="subheading">各部位の説明</div>

<div class="subentry">セキュリティボタン</div>

<div class="img-float-left">

<img src="./images/photos/handgun_switch.jpg" width="320px" />
セキュリティボタンを押すとガンヘッドが起動し、照明やファンが作動します。（マグネットカバーの場合は電磁石も作動します）<br>
再度ボタンを押すとガンヘッドが停止します。<br>
トリガーを引いて加工を行う場合は、ガンヘッドが起動している必要があります。

</div>


<div class="subentry">ステータスランプ</div>

<div class="img-float-left">

<table class="noframe" style="float:left; width:auto; margin:0 20px 0 0;">
  <tr>
    <td style="padding:0; line-height:0; font-size:0;">
      <img src="./images/photos/handgun_led_green.jpg" width="150" style="margin:0;">
    </td>
    <td style="width:20px; padding:0; margin:0px"></td>
    <td style="padding:0;">
      <img src="./images/photos/handgun_led_red.jpg" width="150" style="margin:0;">
    </td>
  </tr>
  <tr>
    <td style="text-align:center; padding:0;">起動中</td>
    <td style="width:0px; padding:0; margin:0px"></td>
    <td style="text-align:center; padding:0;">加工中</td>
  </tr>
</table>

ガンヘッドが起動中はLEDが緑色に点灯し、加工中は赤色に点灯します。

</div>


<div class="subentry">トリガー</div>

<div class="img-float-left">

<img src="./images/photos/handgun_trigger_zoom.jpg" width="320px" />

トリガーを引く際は中央部分をしっかりと奥まで押し込んでください。<br>

</div>



<div style="page-break-before:always"></div>


<span class="subheading">基本手順</div>

**ガンヘッドを起動**

ガンヘッドをしっかりと保持し、加工素材や安全な方向に向けた状態で、セキュリティボタンを押してガンヘッドを起動します。


**マーキングモードへの切り替え**

次に、ステータスバーの「START」ボタンをタップし、マーキングモードに切り替えます。<br>

<div style="margin: 30px 10px 40px">

操作モード
<img src="./images/quickstart_status_bar_idle.png"  width="540px" style="margin-bottom:15px" />

マーキングモード
<img src="./images/quickstart_status_bar_marking.png"  width="540px"/>

</div>

<div class="danger">
マーキングモードでは、ガンヘッドのトリガーを引くと直ちに加工が開始されます。ガンヘッドを倒したり、人体に向けたりしないよう十分に注意してください。<br>

また、<span class="strongred">操作モード中やガンヘッドが停止中の状態であっても、テストマーキングや強制照射などの機能によってレーザーが照射される場合があります。</span>モードやLEDの状態のみで安全と判断せず、操作前には必ず照射方向と周囲の安全を確認してください。
</div>


**位置の調整**


赤色のガイド光で刻印位置を確認しながら、配置を微調整してください。

<img src="./images/photos/handgun_guidelight.jpg"  width="450px"/>





<div style="page-break-before:always"></div>


**加工開始**

トリガーを引くと加工が始まります。トリガーの中央部分をしっかりと奥まで押し込んでください。<br>
加工中はガンヘッドをしっかり保持し、揺らさないように注意してください。<br>
位置を変えながら複数回刻印を行うと、刻印ごとにシリアル番号がカウントアップされます。

<img src="./images/photos/handgun_result.jpg"  width="300px"/>


**加工終了**

加工が終わったら、ステータスバーの「STOP」ボタンをタップしてマーキング状態を解除します。
また、必要に応じてガンヘッドを停止します。



## データ保存

作成したファイルを内部に保存します。
メニューバーの「保存」または「別名保存」をタップし、ファイル名を入力して「OK」をタップします。

<img src="./images/quickstart_save_project.png"  width="450px"/>


## 終了操作

本体側面の電源ボタンを切ります。ガンヘッドも同時にオフになります。