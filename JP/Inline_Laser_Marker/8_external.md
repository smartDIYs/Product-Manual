# 外部機器との通信

## 外部からの文字列指定

インラインレーザーマーカーのテキスト機能は外部デバイスからのデータ入力に対応しています。
あらかじめ文字列（QRコードやデータマトリクス等も含む）の位置や大きさを設定したテキストオブジェクトをファイル上に作成しておくことで、加工文字列を外部デバイスから受信して刻印を行うことが可能です。

外部通信は下記の方法に対応しています。
- TCP通信
- シリアル通信（RS232）

### TCP通信の例

下記の例はコントローラとデバイス（PC）を LAN ケーブルで一対一で接続した場合の設定例です。

<div class="subentry">事前準備</div>

**[1] LAN ケーブル接続**
1. PCとコントローラをLANケーブルで接続します。コントローラ側のLANコネクタは画面裏にあります。

**[2] コントローラの IP アドレス設定**
1. 「パラメータ」タブ > システム設定 > 高度な設定 > ネットワーク設定 を開きます。
1. IPアドレスやサブネットマスクを設定します。<br>
例）IPアドレス: 192.168.1.10 / サブネットマスク: 255.255.255.0 / デフォルトゲートウェイ: 192.168.1.1

**[3] 外部通信の設定**
1. 「パラメータ」タブ > システム設定 > 外部通信 を開きます。
1. 「通信プラグイン」に「plugin_tcp 0.0※」を設定します。
1. 「通信プラグイン」の設定を開き、ポート番号を適宜設定します。（例: 45678）
1. 「解析プラグイン」に「stdParser 0.0※」を設定します。<br>
※プラグインの数字はバージョンによって異なります。

**[4] PC のネットワーク設定**
1. PC側のLAN接続のネットワーク設定を適宜設定します。<br>
例）IP アドレス: 192.168.1.5 / サブネットマスク: 255.255.255.0 / デフォルトゲートウェイ: 192.168.1.1

**[5] テスト**
1. 「パラメータ」タブ > システム設定 > 外部通信を開きます。
1. 「起動」ボタンをタップします。
1. PCデバイスのターミナルで上記に接続します。<br>
例）$ telnet 192.168.1.10 45678
1. ターミナル上で「ABC;;」と入力し、エンターキーを押します。
1. コントローラ画面上に「ABC;;」と表示されたら正常に通信ができています。<br>
※「;;」はデフォルトのデータの区切り文字です。この文字列で入力完了と判断されます。


<div class="subentry">データ作成と加工</div>

**プロジェクトの作成**
1. 「ファイル」タブ→「新規」をタップし、新しいプロジェクトを作成します。
1. 「編集」タブを開き、「テキスト」「追加」「外部データ」「OK」の順にタップします。
1. フォントや大きさなどの設定を適宜行い、右上の「確定」をタップします。

**プロジェクトの加工**
1. 上記のプロジェクトファイルを開きます。
1. 「マーク」タブを開き、「マーキング」ボタンを有効にします。
1. PC デバイスのターミナルで上記に接続します。<br>
例）$ telnet 192.168.1.10 45678
1. ターミナル上で文字列（例 :「TEST;;」）を入力し、エンターキーを押します。
1. 「手動トリガー」または IO などから刻印開始指示を行います。
1. 文字列が「TEST」に置き換わり、刻印されます。


### シリアル通信の例

下記の例はコントローラとデバイス（PC）をシリアル通信ケーブルで接続した場合の設定例です

<div class="subentry">事前準備</div>

**[1] シリアル通信ケーブル接続**
1. PCとコントローラをシリアル通信ケーブルで接続します。コントローラ側のシリアルコネクタは画面裏にあります。

**[2] 外部通信の設定**
1. 「パラメータ」タブ→システム設定→外部通信を開きます。
1. 「通信プラグイン」に「plugin_com 0.0※」を設定します。
1. 「通信プラグイン」の設定を開き、シリアルポートを「ttyS2」に設定します。必要に応じてボーレート等を適宜設定します。
1. 「解析プラグイン」に「stdParser 0.0※」を設定します。<br>
※プラグインの数字はバージョンによって異なります。

**[2] テスト**
1. 「パラメータ」タブ→システム設定→外部通信を開きます。
2. 「起動」ボタンをタップします。
3. PC デバイスのターミナルで上記に接続します。<br>
例）$ screen /dev/ttyUSB0 9600　（デバイス名は環境によって異なります）
4. ターミナル上で「ABC;;」と入力し、エンターキーを押します。
5. コントローラ画面上に「ABC;;」と表示されたら正常に通信ができています。<br>
※「;;」はデフォルトのデータの区切り文字です。この文字列で入力完了と判断されます。


<div class="subentry">データ作成と加工</div>

**プロジェクトの作成**
1. 「ファイル」タブ→「新規」をタップし、新しいプロジェクトを作成します。
1. 「編集」タブを開き、「テキスト」「追加」「外部データ」「OK」の順にタップします。
1. フォントや大きさなどの設定を適宜行い、右上の「確定」をタップします。

**プロジェクトの加工**
1. 上記のプロジェクトファイルを開きます。
1. 「マーク」タブを開き、「マーキング」ボタンを有効にします。
1. PC デバイスのターミナルで上記に接続します。<br>
例）$ screen /dev/ttyUSB0 9600
1. ターミナル上で文字列（例 :「TEST;;」）を入力し、エンターキーを押します。
1. 「手動トリガー」または IO などから刻印開始指示を行います。
1. 文字列が「TEST」に置き換わり、刻印されます。



## コマンド制御

コマンド制御機能を有効にすることで、外部通信によるコマンド制御（加工操作やデータの編集）が可能になります。<br>
※この機能を使用する場合は[外部通信](#外部通信)の解析プラグインの設定項目にある「コマンド制御」にチェックを入れてください。

コマンド制御は下記の通信方法に対応しています。
- TCP通信
- シリアル通信（RS232）

<div class="annotation">
コマンド制御機能を有効にした場合でも、外部からの文字列指定機能は利用できます。
</div>


### プロトコル形式

- 送信内容: `開始記号` `内容` `終了記号`
- 受信内容: `開始記号` `内容` `終了記号`

開始記号と終了記号はインターフェース上で設定可能で、デフォルトでは開始記号は空で、終了記号は「;;」です。
以下のプロトコル説明は、すべてこのデフォルトの開始記号と終了記号を例としています。<br>
また、設定は16進数表示をサポートします。例えば、開始記号がASCIIの02である場合、0x02と設定できます。
<!-- プロトコルの内容は、コマンド制御タイプとデータタイプの2種類に分かれます。 -->

送信されたコマンド形式が正しくない場合、外部データ用の文字列として解釈され「 receive;; 」を返します。


### コマンド一覧

以下の送信例は、開始記号を「」（空文字）、終了記号を「;;」に設定している場合の例です。


<div class="commandcontrol">





<!-- Original ID: 1 -->
<div class="no-break">
<div class="command">
1. コントロールボード接続状態の取得 - GetLinkStatus
</div>

コントロールボードの接続状態を取得します。

<table>
<tr><td>コマンド</td><td>GetLinkStatus</td></tr>
<tr><td>送信例</td><td>GetLinkStatus;;</td></tr>
<tr><td>返信例</td><td>1;;</td></tr>
</table>

<div class="annotation">
0：未接続 / 1：接続済み
</div>
</div>

<!-- Original ID: 2 -->
<div class="no-break">
<div class="command">
2. システム動作状態の取得 - GetMarkStatus
</div>

現在のシステムの動作状態を取得します。

<table>
<tr><td>コマンド</td><td>GetMarkStatus</td></tr>
<tr><td>送信例</td><td>GetMarkStatus;;</td></tr>
<tr><td>返信例</td><td>0;;</td></tr>
</table>

<div class="annotation">
0：アイドル（待機） / 1：シミュレーション中 / 2：マーキング中 / 3：プレビュー中 / 4：レーザー校正テスト中 / 5：赤色ガイド光校正テスト中 / 6：レーザー強制出力中 / 7：回転マーキング中 / 8：赤色ガイド光フォーカス中
</div>
</div>

<!-- Original ID: 3 -->
<div class="no-break">
<div class="command">
3. マーキングカウントの取得 - GetCount
</div>

マーキングに関するカウント情報を取得します。総マーキング数、連続マーキング数、マーキング漏れ回数、直近のマーキング所要時間が含まれます。

<table>
<tr><td>コマンド</td><td>GetCount</td></tr>
<tr><td>送信例</td><td>GetCount;;</td></tr>
<tr><td>返信例</td><td>2,1,0,100;;</td></tr>
</table>

<div class="annotation">
返信値は順に、総マーキング数、連続マーキング数、マーキング漏れ回数、直近のマーキング所要時間（単位：ms）を示します。<br>
返信例では、総マーキング数：2、連続マーキング数：1、マーキング漏れ回数：0、所要時間：100msです。<br>
なお、取得前にレーザーテストまたはプレビューを実行した場合は、そのテストまたはプレビューの所要時間などが返されます。
</div>
</div>

<!-- Original ID: 4 -->
<div class="no-break">
<div class="command">
4. 総マーキング数の取得 - GetMarkedCount
</div>

総マーキング数を取得します。

<table>
<tr><td>コマンド</td><td>GetMarkedCount</td></tr>
<tr><td>送信例</td><td>GetMarkedCount;;</td></tr>
<tr><td>返信例</td><td>2;;</td></tr>
</table>

<div class="annotation">
返信例の2は、総マーキング数を示します。
</div>
</div>

<!-- Original ID: 5 -->
<div class="no-break">
<div class="command">
5. マーキング漏れ回数の取得 - GetMissedCount
</div>

マーキング漏れ回数を取得します。

<table>
<tr><td>コマンド</td><td>GetMissedCount</td></tr>
<tr><td>送信例</td><td>GetMissedCount;;</td></tr>
<tr><td>返信例</td><td>0;;</td></tr>
</table>

<div class="annotation">
返信例の0は、マーキング漏れ回数を示します。
</div>
</div>

<!-- Original ID: 6 -->
<div class="no-break">
<div class="command">
6. カウントのクリア - ClearCount
</div>

マーキングに関するカウント情報をクリアします。

<table>
<tr><td>コマンド</td><td>ClearCount</td></tr>
<tr><td>送信例</td><td>ClearCount;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
クリアに失敗した場合は、Failed,ErrorInfoが返されます。ErrorInfoにはエラーの詳細が含まれます。例えば、is marking;はマーキング中のためカウントをクリアできないことを示します。
</div>
</div>

<!-- Original ID: 7 -->
<div class="no-break">
<div class="command">
7. テンプレートのテキスト内容の取得 - GetMarkData
</div>

現在のテンプレートに含まれるテキスト、QRコード、バーコードの内容を全て取得します。

<table>
<tr><td>コマンド</td><td>GetMarkData</td></tr>
<tr><td>送信例</td><td>GetMarkData;;</td></tr>
<tr><td>返信例</td><td>DATA1DATA2;;</td></tr>
</table>

<div class="annotation">
DATA1、DATA2の順に、対象となる図形の内容が返されます。対象となる図形がない場合は空になります。<br>
各文字列は、それぞれの図形で前回マーキングした内容を示します。
</div>
</div>

<!-- Original ID: 8 -->
<div class="no-break">
<div class="command">
8. ライン方向の取得 - GetAssemblyLineDir
</div>

現在のライン方向を取得します。

<table>
<tr><td>コマンド</td><td>GetAssemblyLineDir</td></tr>
<tr><td>送信例</td><td>GetAssemblyLineDir;;</td></tr>
<tr><td>返信例</td><td>0;;</td></tr>
</table>

<div class="annotation">
0：右から左 / 1：左から右
</div>
</div>

<!-- Original ID: 9 -->
<div class="no-break">
<div class="command">
9. ライン方向の設定 - SetAssemblyLineDir
</div>

ライン方向を設定します。

<table>
<tr><td>コマンド</td><td>SetAssemblyLineDir</td></tr>
<tr><td>送信例</td><td>SetAssemblyLineDir,1;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
0：右から左 / 1：左から右<br>
設定は次回のマーキングから有効になります。
</div>
</div>

<!-- Original ID: 10 -->
<div class="no-break">
<div class="command">
10. ライン動作方式の取得 - GetAssemblyLineType
</div>

現在のライン動作方式（エンコーダ、固定ライン速度、静的マーク）を取得します。

<table>
<tr><td>コマンド</td><td>GetAssemblyLineType</td></tr>
<tr><td>送信例</td><td>GetAssemblyLineType;;</td></tr>
<tr><td>返信例</td><td>0;;</td></tr>
</table>

<div class="annotation">
0：エンコーダ / 1：固定ライン速度 / 2：静的マーク
</div>
</div>

<!-- Original ID: 11 -->
<div class="no-break">
<div class="command">
11. ライン動作方式の設定 - SetAssemblyLineType
</div>

ライン動作方式（エンコーダ、固定ライン速度、静的マーク）を設定します。

<table>
<tr><td>コマンド</td><td>SetAssemblyLineType</td></tr>
<tr><td>送信例</td><td>SetAssemblyLineType,0;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
0：エンコーダ / 1：固定ライン速度 / 2：静的マーク<br>
設定は次回のマーキングから有効になります。
</div>
</div>

<!-- Original ID: 12 -->
<div class="no-break">
<div class="command">
12. パルス間距離パラメータの取得 - GetEncodeParam
</div>

現在のエンコーダのパルス間距離を取得します。この設定は、ライン動作方式が「エンコーダ」の場合のみ有効です。

<table>
<tr><td>コマンド</td><td>GetEncodeParam</td></tr>
<tr><td>送信例</td><td>GetEncodeParam;;</td></tr>
<tr><td>返信例</td><td>20.00;;</td></tr>
</table>

<div class="annotation">
返信例の20.00は、現在設定されているパルス間距離を示します（単位：µm/p）。
</div>
</div>

<!-- Original ID: 13 -->
<div class="no-break">
<div class="command">
13. パルス間距離パラメータの設定 - SetEncodeParam
</div>

エンコーダのパルス間距離を設定します。この設定は、ライン動作方式が「エンコーダ」の場合のみ有効です。

<table>
<tr><td>コマンド</td><td>SetEncodeParam</td></tr>
<tr><td>送信例</td><td>SetEncodeParam,20.0;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
設定は次回のマーキングから有効になります。
</div>
</div>

<!-- Original ID: 14 -->
<div class="no-break">
<div class="command">
14. 固定ライン速度の取得 - GetFixSpeed
</div>

現在の固定ライン速度を取得します。この設定は、ライン動作方式が「固定ライン速度」の場合のみ有効です。

<table>
<tr><td>コマンド</td><td>GetFixSpeed</td></tr>
<tr><td>送信例</td><td>GetFixSpeed;;</td></tr>
<tr><td>返信例</td><td>20.00;;</td></tr>
</table>

<div class="annotation">
返信例の20.00は、現在設定されている固定ライン速度を示します（単位：m/min）。
</div>
</div>

<!-- Original ID: 15 -->
<div class="no-break">
<div class="command">
15. 固定ライン速度の設定 - SetFixSpeed
</div>

固定ライン速度を設定します。この設定は、ライン動作方式が「固定ライン速度」の場合のみ有効です。

<table>
<tr><td>コマンド</td><td>SetFixSpeed</td></tr>
<tr><td>送信例</td><td>SetFixSpeed,20.0;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
設定は次回のマーキングから有効になります。
</div>
</div>

<!-- Original ID: 16 -->
<div class="no-break">
<div class="command">
16. トリガー遅延パラメータの取得 - GetTriggerDelay
</div>

現在のトリガー遅延設定（遅延方式と遅延値）を取得します。

<table>
<tr><td>コマンド</td><td>GetTriggerDelay</td></tr>
<tr><td>送信例</td><td>GetTriggerDelay;;</td></tr>
<tr><td>返信例</td><td>1,100;;</td></tr>
</table>

<div class="annotation">
1番目の値は遅延方式を示します（0：オフ / 1：距離 / 2：時間）。<br>
2番目の値は遅延値を示します。遅延方式が1の場合は距離（単位：mm）、2の場合は時間（単位：ms）です。
</div>
</div>

<!-- Original ID: 17 -->
<div class="no-break">
<div class="command">
17. トリガー遅延パラメータの設定 - SetTriggerDelay
</div>

トリガー遅延設定（遅延方式と遅延値）を設定します。

<table>
<tr><td>コマンド</td><td>SetTriggerDelay</td></tr>
<tr><td>送信例</td><td>SetTriggerDelay,1,100;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
1番目の値は遅延方式を示します（0：オフ / 1：距離 / 2：時間）。<br>
2番目の値は遅延値を示します。遅延方式が1の場合は距離（単位：mm）、2の場合は時間（単位：ms）です。<br>
設定は次回のマーキングから有効になります。
</div>
</div>

<!-- Original ID: 18 -->
<div class="no-break">
<div class="command">
18. ラインパイプトリガー間隔パラメータの取得 - GetPipIntveralDistance
</div>

現在のトリガー間隔距離を取得します。

<table>
<tr><td>コマンド</td><td>GetPipIntveralDistance</td></tr>
<tr><td>送信例</td><td>GetPipIntveralDistance;;</td></tr>
<tr><td>返信例</td><td>100;;</td></tr>
</table>

<div class="annotation">
返信例の100は、現在設定されているトリガー間隔を示します（単位：mm）。
</div>
</div>

<!-- Original ID: 19 -->
<div class="no-break">
<div class="command">
19. ラインパイプトリガー間隔パラメータの設定 - SetPipIntveralDistance
</div>

トリガー間隔距離を設定します。

<table>
<tr><td>コマンド</td><td>SetPipIntveralDistance</td></tr>
<tr><td>送信例</td><td>SetPipIntveralDistance,100;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
マーキング中に設定した場合は、即時に反映されます。
</div>
</div>

<!-- Original ID: 20 -->
<div class="no-break">
<div class="command">
20. テンプレートリストの取得 - GetDocList
</div>

システム内のドキュメントフォルダに保存されているテンプレートリストを取得します。

<table>
<tr><td>コマンド</td><td>GetDocList</td></tr>
<tr><td>送信例</td><td>GetDocList;;</td></tr>
<tr><td>返信例</td><td>1.bpd;2.bpd;;</td></tr>
</table>

<div class="annotation">
返信例の1.bpd、2.bpdはテンプレート名を示します。サブフォルダ内のテンプレートは取得されません。
</div>
</div>

<!-- Original ID: 21 -->
<div class="no-break">
<div class="command">
21. 指定テンプレートを開く - OpenDoc
</div>

指定したテンプレートを開きます。このコマンドは編集状態でのみ使用できます。

<table>
<tr><td>コマンド</td><td>OpenDoc</td></tr>
<tr><td>送信例</td><td>OpenDoc,sample.bpd;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
拡張子（.bpd）を含むファイル名を指定します（例：01.bpd）。<br>
サブフォルダ内のテンプレートを指定する場合は、フォルダ名/ファイル名.bpdの形式で指定します（例：OpenDoc,mydir/03.bpd;;）。
</div>
</div>

<!-- Original ID: 22 -->
<div class="no-break">
<div class="command">
22. テンプレートの切り替え - SwitchDoc
</div>

マーキングに使用するテンプレートを切り替えます。このコマンドはマーキング状態でのみ使用できます。マーキング中に実行した場合は、現在のマーキング完了後、次回のマーキングから切り替わります。待機中に実行した場合は、次回のマーキングから切り替わります。
加工パラメータの変更を反映する場合は、一度マーキング状態を終了し、再度開始する必要があります。

<table>
<tr><td>コマンド</td><td>SwitchDoc</td></tr>
<tr><td>送信例</td><td>SwitchDoc,sample.bpd;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
拡張子（.bpd）を含むファイル名を指定します（例：01.bpd）。<br>
サブフォルダ内のテンプレートを指定する場合は、フォルダ名/ファイル名.bpdの形式で指定します（例：SwitchDoc,mydir/03.bpd;;）。
</div>
</div>

<!-- Original ID: 23 -->
<div class="no-break">
<div class="command">
23. テンプレートの保存 - SaveCurrentDoc
</div>

現在のテンプレートを保存します。このコマンドはマーキング状態以外でのみ使用できます。

<table>
<tr><td>コマンド</td><td>SaveCurrentDoc</td></tr>
<tr><td>送信例</td><td>SaveCurrentDoc;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 24 -->
<div class="no-break">
<div class="command">
24. テンプレートを名前を付けて保存 - SaveDocAs
</div>

現在のテンプレートを指定したファイル名でローカルディレクトリに保存します。

<table>
<tr><td>コマンド</td><td>SaveDocAs</td></tr>
<tr><td>送信例</td><td>SaveDocAs,sample2.bpd;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
拡張子（.bpd）を含むファイル名を指定します。
</div>
</div>

<!-- Original ID: 25 -->
<div class="no-break">
<div class="command">
25. テンプレートの図形リストの取得 - GetShapeList
</div>

現在のテンプレートに含まれる図形オブジェクトの一覧を取得します。図形名はテンプレート内の並び順で返されます。

<table>
<tr><td>コマンド</td><td>GetShapeList</td></tr>
<tr><td>送信例</td><td>GetShapeList;;</td></tr>
<tr><td>返信例</td><td>Shape1;Shape2;;</td></tr>
</table>

<div class="annotation">
返信例では、Shape1が1番目、Shape2が2番目の図形名を示します。<br>
図形名（オブジェクト名）は、「編集」タブのリストからも確認できます。
</div>
</div>

<!-- Original ID: 26 -->
<div class="no-break">
<div class="command">
26. 指定図形のテキスト内容の取得 - GetShapeData
</div>

指定した図形のテキスト内容を取得します（複数指定可）。テキスト、QRコード、バーコードにのみ使用できます。編集状態では現在の内容、マーキング状態では前回マーキングした内容を取得します。

<table>
<tr><td>コマンド</td><td>GetShapeData</td></tr>
<tr><td>送信例</td><td>GetShapeData,Shape1,Shape2;;</td></tr>
<tr><td>返信例</td><td>text1;text2;;</td></tr>
</table>

<div class="annotation">
返信例では、text1が1番目、text2が2番目に指定した図形のテキスト内容を示します。
</div>
</div>

<!-- Original ID: 27 -->
<div class="no-break">
<div class="command">
27. 指定図形の位置の取得 - GetShapePos
</div>

指定した図形の位置を取得します（複数指定可）。位置は Rect(x, y, w, h) 形式で、図形の左下座標（x, y）と幅（w）、高さ（h）が返されます。

<table>
<tr><td>コマンド</td><td>GetShapePos</td></tr>
<tr><td>送信例</td><td>GetShapePos,Shape1,Shape2;;</td></tr>
<tr><td>返信例</td><td>Shape1,x1,y1,w1,h1;Shape2,x2,y2,w2,h2;;</td></tr>
</table>

<div class="annotation">
Shape1、Shape2は指定した図形名を示します。<br>
x、yは図形の左下座標、wは幅、hは高さを示します。<br>
テキスト、QRコード、バーコード、図形にのみ使用できます。
</div>
</div>

<!-- Original ID: 28 -->
<div class="no-break">
<div class="command">
28. 指定図形の位置の設定 - SetShapePos
</div>

指定した図形の位置を設定します（複数指定可）。位置は Rect(x, y, w, h) 形式で、x、yに図形の左下座標、wに幅、hに高さを指定します。

<table>
<tr><td>コマンド</td><td>SetShapePos</td></tr>
<tr><td>送信例</td><td>SetShapePos,Shape1,x1,y1,w1,h1;Shape2,x2,y2,w2,h2;;</td></tr>
<tr><td>返信例</td><td>ok;;</td></tr>
</table>

<div class="annotation">
Shape1、Shape2は指定する図形名を示します。<br>
x、yは図形の左下座標、wは幅、hは高さを指定します。<br>
設定に失敗した場合は Failed,ErrorInfo が返されます。ErrorInfoにはエラーの詳細が含まれます。<br>
テキスト、QRコード、バーコード、図形にのみ使用できます。
</div>
</div>

<!-- Original ID: 29 -->
<div class="no-break">
<div class="command">
29. 指定図形のテキスト内容、位置、角度の設定 - SetShapeData
</div>

指定した図形のテキスト内容、位置、回転角度を設定します（複数指定可）。位置と回転を同時に指定した場合は、「移動→回転」の順に処理されます。
テキスト内容の設定は、テキスト、QRコード、バーコードにのみ使用でき、対象の図形に固定テキストが1つ設定されている場合に限ります。

<table>
<tr><td>コマンド</td><td>SetShapeData</td></tr>
<tr><td>送信例</td><td>SetShapeData,Shape1,text1,posx1,posy1,postype1,angle1,cx1,cy1,rottype1;Shape2,text2,posx2,posy2,postype2,angle2,cx2,cy2,rottype2;;</td></tr>
<tr><td>返信例</td><td>ok;;</td></tr>
</table>

<div class="annotation">
Shape1：対象の図形名を指定します。空の場合は、すべての図形が対象となります。この場合、テキスト内容は設定できません。<br>
text1：図形のテキスト内容を指定します。<br>
posx1：相対移動の場合はX方向の移動量、絶対移動の場合は図形中心のX座標を指定します。<br>
posy1：相対移動の場合はY方向の移動量、絶対移動の場合は図形中心のY座標を指定します。<br>
postype1：移動方式を指定します（0：相対移動 / 1：絶対移動）。<br>
angle1：回転角度を指定します。<br>
cx1：回転中心のX座標を指定します。空の場合は図形自体の中心を基準に回転します。<br>
cy1：回転中心のY座標を指定します。空の場合は図形自体の中心を基準に回転します。<br>
rottype1：回転方式を指定します（0：相対回転 / 1：絶対回転）。相対回転を行った場合、回転後の角度が0°として扱われます。<br>
<br>
各パラメータは省略できます。例えば、テキスト内容のみを変更する場合は、text1より後のパラメータを省略できます。<br>
<br>
例1：Shape1の内容をtext1、Shape2の内容をtext2に変更する場合<br>
SetShapeData,Shape1,text1;Shape2,text2;;<br>
<br>
例2：すべての図形をひとまとまりとして中心点（0, 0）へ移動する場合<br>
SetShapeData,,,0,0,1;;
</div>
</div>

<!-- Original ID: 30 -->
<div class="no-break">
<div class="command">
30. キャッシュデータを送信して指定図形のテキスト、位置、角度を変更 - PushShapeData
</div>

キャッシュデータを使用して、指定した図形のテキスト内容、位置、回転角度を変更します（複数指定可）。カメラを使用した位置補正システムとの連携などに使用できます。
このコマンドは、システムがマーキング状態で、外部通信の「キャッシュモード」が有効な場合のみ使用できます。
位置と回転角度の変更は元データには反映されず、キャッシュデータにのみ適用されます。テキスト内容を変更した場合は、文字列のみ元データにも反映されます。
テキスト内容の変更は、テキスト、QRコード、バーコードにのみ使用でき、対象の図形に固定テキストが1つ設定されている場合に限ります。

<table>
<tr><td>コマンド</td><td>PushShapeData</td></tr>
<tr><td>送信例</td><td>PushShapeData,Shape1,text1,posx1,posy1,postype1,angle1,cx1,cy1,0;Shape2,text2,posx2,posy2,postype2,angle2,cx2,cy2,0;;</td></tr>
</table>

<div class="annotation">
各パラメータについては、SetShapeDataを参照してください。<br>
変更したテキスト内容がプレビュー画面に反映されるまでに時間がかかる場合は、「パラメータ > 高度な設定 > リアルタイム更新」を有効にしてください。位置および回転角度の変更は、プレビュー画面には反映されません。<br>
キャッシュサイズは「パラメータ > マーキング方法 > その他」で設定します。<br>
<br>
例：すべての図形をX方向に10、Y方向に20相対移動し、その後、すべての図形の中心を基準に90°回転する場合<br>
PushShapeData,,,10,20,0,,,90;;
</div>
</div>

<!-- Original ID: 31 -->
<div class="no-break">
<div class="command">
31. キャッシュデータのクリア - ClearCache
</div>

PushShapeDataで送信されたすべてのキャッシュデータをクリアします。

<table>
<tr><td>コマンド</td><td>ClearCache</td></tr>
<tr><td>送信例</td><td>ClearCache;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 32 -->
<div class="no-break">
<div class="command">
32. 指定ベクター図形の変更 - SetVectorgraphData
</div>

指定したベクター図形の内容を変更します。このコマンドは編集状態でのみ使用できます。

<table>
<tr><td>コマンド</td><td>SetVectorgraphData</td></tr>
<tr><td>送信例</td><td>SetVectorgraphData,Shape1,plt,data;;</td></tr>
</table>

<div class="annotation">
Shape1：変更するベクター図形名を指定します。<br>
plt：ベクターファイル形式を指定します（plt / dxf / ai）。<br>
data：ベクターファイルのデータストリームを指定します。<br>
通信速度が遅い場合、データの送信中にタイムアウトが発生することがあります。
</div>
</div>

<!-- Original ID: 33 -->
<div class="no-break">
<div class="command">
33. ペンパラメータの取得 - GetPen
</div>

指定したペン番号のパラメータを取得します。

<table>
<tr><td>コマンド</td><td>GetPen</td></tr>
<tr><td>送信例</td><td>GetPen,0,MarkSpeed,Power;;</td></tr>
<tr><td>返信例</td><td>4000,80;;</td></tr>
</table>

<div class="annotation">
送信例の0はペン番号を示します（0～15）。<br>
MarkSpeed（加工速度）、JumpSpeed（ジャンプ速度）、Power（パワー）、PW（パルス幅）、MopaPW（Mopaパルス幅）、Freq（周波数）、PointTime（ドット時間）などのパラメータを取得できます。<br>
返信例では、4000が加工速度、80がパワーを示します。
</div>
</div>

<!-- Original ID: 34 -->
<div class="no-break">
<div class="command">
34. ペンパラメータの設定 - SetPen
</div>

指定したペン番号のパラメータを設定します。設定は、次回マーキング状態に移行したときに有効になります。

<table>
<tr><td>コマンド</td><td>SetPen</td></tr>
<tr><td>送信例</td><td>SetPen,ID,0;MarkSpeed,4000;Power,80;;</td></tr>
</table>

<div class="annotation">
ID,0：ペン番号0を指定します。<br>
MarkSpeed,4000：加工速度を4000に設定します。<br>
Power,80：パワーを80に設定します。
</div>
</div>

<!-- Original ID: 35 -->
<div class="no-break">
<div class="command">
35. マーキング対象図形の指定 - MarkShape
</div>

マーキング対象の図形を指定します（複数指定可）。指定できる図形は、テキスト、QRコード、バーコードに限ります。
このコマンドはマーキング状態でのみ使用でき、設定は次回のマーキングから有効になります。

<table>
<tr><td>コマンド</td><td>MarkShape</td></tr>
<tr><td>送信例</td><td>MarkShape,Shape1,Shape2;;</td></tr>
</table>

<div class="annotation">
Shape1、Shape2：マーキング対象の図形名を指定します。<br>
テンプレート内のすべての図形をマーキングする場合は、MarkShape;;を送信します。
</div>
</div>

<!-- Original ID: 36 -->
<div class="no-break">
<div class="command">
36. マーキング状態の開始 - StartMark
</div>

システムをマーキング状態に移行します。

<table>
<tr><td>コマンド</td><td>StartMark</td></tr>
<tr><td>送信例</td><td>StartMark;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 37 -->
<div class="no-break">
<div class="command">
37. マーキング状態の終了 - StopMark
</div>

システムをアイドル状態に移行します。

<table>
<tr><td>コマンド</td><td>StopMark</td></tr>
<tr><td>送信例</td><td>StopMark;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 38 -->
<div class="no-break">
<div class="command">
38. プレビューの開始 - StartRedMark
</div>

システムをプレビュー状態に移行します。

<table>
<tr><td>コマンド</td><td>StartRedMark</td></tr>
<tr><td>送信例</td><td>StartRedMark;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 39 -->
<div class="no-break">
<div class="command">
39. 手動トリガーの入力 - ManualTrgger
</div>

トリガー待ち状態のときに、マーキングを手動で開始します。このコマンドはマーキング状態でのみ使用できます。

<table>
<tr><td>コマンド</td><td>ManualTrgger</td></tr>
<tr><td>送信例</td><td>ManualTrgger;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 40 -->
<div class="no-break">
<div class="command">
40. シリアル番号のリセット - ClearSN
</div>

テンプレート内のすべてのシリアル番号を初期値にリセットします。マーキング中に実行した場合は、次回のマーキングから有効になります。

<table>
<tr><td>コマンド</td><td>ClearSN</td></tr>
<tr><td>送信例</td><td>ClearSN;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 45 -->
<div class="no-break">
<div class="command">
41. テンプレート名の取得 - GetCurDoc
</div>

現在のテンプレート名を取得します。

<table>
<tr><td>コマンド</td><td>GetCurDoc</td></tr>
<tr><td>送信例</td><td>GetCurDoc;;</td></tr>
<tr><td>返信例</td><td>1.bpd;;</td></tr>
</table>
</div>

<!-- Original ID: 53 -->
<div class="no-break">
<div class="command">
42. テンプレートを開いてマーキング状態に移行 - OpenDocMark
</div>

指定したテンプレートを開き、そのままマーキング状態に移行します。

<table>
<tr><td>コマンド</td><td>OpenDocMark</td></tr>
<tr><td>送信例</td><td>OpenDocMark,file;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
拡張子（.bpd）を含むファイル名を指定します（例：01.bpd）。<br>
加工設定によってはそのままレーザー照射が始まります。
</div>
</div>

<!-- Original ID: 56 -->
<div class="no-break">
<div class="command">
43. 指定図形の選択状態の設定 - SetShapeSelectState
</div>

指定した図形の選択／非選択を設定します。

<table>
<tr><td>コマンド</td><td>SetShapeSelectState</td></tr>
<tr><td>送信例</td><td>SetShapeSelectState,shapeName,mode;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
shapeName：対象の図形名を指定します。<br>
mode：選択状態を指定します（0：非選択 / 1：選択）。
</div>
</div>

<!-- Original ID: 57 -->
<div class="no-break">
<div class="command">
44. 選択図形のみフラグの設定 - SetSelectMark
</div>

選択した図形のみをマーキング対象にするかどうかを設定します。

<table>
<tr><td>コマンド</td><td>SetSelectMark</td></tr>
<tr><td>送信例</td><td>SetSelectMark,mode;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
mode：選択図形のみの有効／無効を指定します（0：無効 / 1：有効）。
</div>
</div>

<!-- Original ID: 58 -->
<div class="no-break">
<div class="command">
45. 連続マーキングの設定 - SetContinueMark
</div>

連続マーキング機能の有効／無効を設定します。

<table>
<tr><td>コマンド</td><td>SetContinueMark</td></tr>
<tr><td>送信例</td><td>SetContinueMark,mode;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
mode：連続マーキングの有効／無効を指定します（0：無効 / 1：有効）。
</div>
</div>

<!-- Original ID: 59 -->
<div class="no-break">
<div class="command">
46. 指定図形のテキストサイズ設定 - SetShapeFont
</div>

指定したテキストオブジェクトの文字高さと文字間隔を設定します。

<table>
<tr><td>コマンド</td><td>SetShapeFont</td></tr>
<tr><td>送信例</td><td>SetShapeFont,shapeName,height,width;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
shapeName：対象の図形名を指定します。<br>
height：文字の高さを指定します。<br>
width：文字間隔を指定します。
</div>
</div>






</div>