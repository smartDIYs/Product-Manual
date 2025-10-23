# 外部通信

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
※プラグインの数字はバージョンによって異なります

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
1. 「通信プラグイン」の設定を開き、シリアルポートを「ttyS2」に設定します。必要に応じてビットレート等を適宜設定します。
1. 「解析プラグイン」に「stdParser 0.0※」を設定します。<br>
※プラグインの数字はバージョンによって異なります

**[2] テスト**
1. 「パラメータ」タブ→システム設定→外部通信を開きます。
2. 「起動」ボタンをタップします。
3. PC デバイスのターミナルで上記に接続します。
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
1. 文字列が「TEST」に置き換


<div style="page-break-before:always"></div>

## コマンド制御

コマンド制御機能を有効にすることで、シリアル通信（RS232）およびTCP通信からコマンドによる加工データの編集が可能です。

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
プロトコルの内容は、コマンド制御タイプとデータタイプの2種類に分かれます。


### プロトコルコマンド制御内容
プラグインインターフェースで「コマンド制御」にチェックを入れると有効になります。
送信されたコマンド形式が正しくない場合、システムは自動的にデータ内容とみなし、「 receive;; 」を直接返します。

以下の送信例は、開始記号を「」（空文字）、終了記号を「;;」に設定している場合の例です。


<div class="commandcontrol">






<div class="no-break">
<div class="command">
1. ボードカード接続状態の取得 - GetLinkStatus
</div>

コントロールボードの現在の接続状態を取得します。

<table>
<tr><td>コマンド</td><td>GetLinkStatus</td></tr>
<tr><td>送信例</td><td>GetLinkStatus;;</td></tr>
<tr><td>返信例</td><td>1;;</td></tr>
</table>

<div class="annotation">
返信1は接続済み、0は未接続を意味します。
</div>
</div>

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
0: アイドル（待機） / 1: シミュレーション中 / 2: マーキング中 / 3: プレビュー中 / 4: レーザー校正テスト中 / 5: 赤色ガイド光校正テスト中 / 6: レーザー強制出力中 / 7: 回転マーキング中 / 8: 赤色ガイド光フォーカス中
</div>
</div>

<div class="no-break">
<div class="command">
3. マーキングカウントの取得 - GetCount
</div>

現在のシステムのマーキングカウントを取得します。総マーキング数、連続マーキング数、マーキング漏れ回数、単回所要時間(ms)などが含まれます。

<table>
<tr><td>コマンド</td><td>GetCount</td></tr>
<tr><td>送信例</td><td>GetCount;;</td></tr>
<tr><td>返信例</td><td>2,1,0,100;;</td></tr>
</table>

<div class="annotation">
返信例の 2 は総マーキング数、1 は連続マーキング数、0 はマーキング漏れ回数、100 は今回の単回所要時間100msを意味します。<br>
なお、取得前にレーザーテストまたはプレビューを実行している場合は、そのテスト/プレビューの所要時間などのパラメータが返されます。
</div>
</div>

<div class="no-break">
<div class="command">
4. 総マーキング数の取得 - GetMarkedCount
</div>

現在の総マーキング数を取得します。

<table>
<tr><td>コマンド</td><td>GetMarkedCount</td></tr>
<tr><td>送信例</td><td>GetMarkedCount;;</td></tr>
<tr><td>返信例</td><td>2;;</td></tr>
</table>

<div class="annotation">
返信例の 2 は総マーキング数を意味します。
</div>
</div>

<div class="no-break">
<div class="command">
5. マーキング漏れ回数の取得 - GetMissedCount
</div>

現在のマーキング漏れ回数を取得します。

<table>
<tr><td>コマンド</td><td>GetMissedCount</td></tr>
<tr><td>送信例</td><td>GetMissedCount;;</td></tr>
<tr><td>返信例</td><td>0;;</td></tr>
</table>

<div class="annotation">
返信例の 0 はマーキング漏れ回数を意味します。
</div>
</div>

<div class="no-break">
<div class="command">
6. カウントのクリア - ClearCount
</div>

現在の各マーキング数をクリアします。

<table>
<tr><td>コマンド</td><td>ClearCount</td></tr>
<tr><td>送信例</td><td>ClearCount;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
クリアに失敗した場合は Failed,ErrorInfo が表示されます。ErrorInfo は具体的な失敗ログで、例えば「 is marking; 」はマーキング中であり、カウントのクリアが禁止されていることを示します。
</div>
</div>

<div class="no-break">
<div class="command">
7. 現在ドキュメント内容の取得 - GetMarkData
</div>

現在のドキュメント内のすべてのテキスト、QRコード、バーコードの文字列内容を取得します。

<table>
<tr><td>コマンド</td><td>GetMarkData</td></tr>
<tr><td>送信例</td><td>GetMarkData;;</td></tr>
<tr><td>返信例</td><td>DATA1DATA2;;</td></tr>
</table>

<div class="annotation">
DATA1 は最初の図形の内容、DATA2 は2番目の図形の内容、と続きます。該当するタイプの図形がない場合は空になります。<br>
 DATA は、その図形が前回マーキングされた内容を示します。
</div>
</div>

<div class="no-break">
<div class="command">
8. 生産ライン方向の取得 - GetAssemblyLineDir
</div>

現在のシステムパラメータにおける生産ライン方向の設定を取得します。

<table>
<tr><td>コマンド</td><td>GetAssemblyLineDir</td></tr>
<tr><td>送信例</td><td>GetAssemblyLineDir;;</td></tr>
<tr><td>返信例</td><td>0;;</td></tr>
</table>

<div class="annotation">
0 は右から左、1 は左から右を意味します。
</div>
</div>

<div class="no-break">
<div class="command">
9. 生産ライン方向の設定 - SetAssemblyLineDir
</div>

現在のシステムパラメータにおける生産ライン方向を設定します。

<table>
<tr><td>コマンド</td><td>SetAssemblyLineDir</td></tr>
<tr><td>送信例</td><td>SetAssemblyLineDir,1;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
0 は右から左、1 は左から右を意味します。 設定は次回のマーキングから有効になります。
</div>
</div>

<div class="no-break">
<div class="command">
10. 運動補償方式の取得 - GetAssemblyLineType
</div>

現在の運動補償方式（静止、エンコーダ、アナログ速度）を取得します。

<table>
<tr><td>コマンド</td><td>GetAssemblyLineType</td></tr>
<tr><td>送信例</td><td>GetAssemblyLineType;;</td></tr>
<tr><td>返信例</td><td>0;;</td></tr>
</table>

<div class="annotation">
0 はエンコーダ、1 はアナログ速度、2は静止を意味します。
</div>
</div>

<div class="no-break">
<div class="command">
11. 運動補償方式の設定 - SetAssemblyLineType
</div>

現在の運動補償方式（静止、エンコーダ、アナログ速度）を設定します。

<table>
<tr><td>コマンド</td><td>SetAssemblyLineType</td></tr>
<tr><td>送信例</td><td>SetAssemblyLineType,0;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
0 はエンコーダ、1 はアナログ速度、2は静止を意味します。 設定は次回のマーキングから有効になります。
</div>
</div>

<div class="no-break">
<div class="command">
12. エンコーダパルス距離パラメータの取得 - GetEncodeParam
</div>

現在のエンコーダパルス距離パラメータ値を取得します。この値は運動補償方式がエンコーダの場合のみ有効です。

<table>
<tr><td>コマンド</td><td>GetEncodeParam</td></tr>
<tr><td>送信例</td><td>GetEncodeParam;;</td></tr>
<tr><td>返信例</td><td>21.0;;</td></tr>
</table>

<div class="annotation">
返信例の 21.0 はパルス距離値を意味し、単位はum/pです。
</div>
</div>

<div class="no-break">
<div class="command">
13. エンコーダパルス距離パラメータの設定 - SetEncodeParam
</div>

現在のエンコーダパルス距離パラメータ値を設定します。この値は運動補償方式がエンコーダの場合のみ有効です。

<table>
<tr><td>コマンド</td><td>SetEncodeParam</td></tr>
<tr><td>送信例</td><td>SetEncodeParam,21.0;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
設定は次回のマーキングから有効になります。
</div>
</div>

<div class="no-break">
<div class="command">
14. アナログ速度の取得 - GetFixSpeed
</div>

現在のアナログ速度を取得します。この値は運動補償方式がアナログ速度の場合のみ有効です。

<table>
<tr><td>コマンド</td><td>GetFixSpeed</td></tr>
<tr><td>送信例</td><td>GetFixSpeed;;</td></tr>
<tr><td>返信例</td><td>21.0;;</td></tr>
</table>

<div class="annotation">
返信例の 21.0 はアナログ速度値を意味し、単位はm/minです。
</div>
</div>

<div class="no-break">
<div class="command">
15. アナログ速度の設定 - SetFixSpeed
</div>

現在のアナログ速度を設定します。この値は運動補償方式がアナログ速度の場合のみ有効です。

<table>
<tr><td>コマンド</td><td>SetFixSpeed</td></tr>
<tr><td>送信例</td><td>SetFixSpeed,21.0;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
設定は次回のマーキングから有効になります。
</div>
</div>

<div class="no-break">
<div class="command">
16. トリガー遅延パラメータの取得 - GetTriggerDelay
</div>

現在のトリガー遅延パラメータ（遅延方式と遅延パラメータ）を取得します。

<table>
<tr><td>コマンド</td><td>GetTriggerDelay</td></tr>
<tr><td>送信例</td><td>GetTriggerDelay;;</td></tr>
<tr><td>返信例</td><td>1,100;;</td></tr>
</table>

<div class="annotation">
返信例の1番め値は遅延方式です（0:オフ / 1:距離 / 2:時間）。<br>
2番目の値は対応する遅延パラメータです。方式が1の場合は遅延距離（単位:mm）、方式が2の場合は遅延時間（単位:ms）を意味します。
</div>
</div>

<div class="no-break">
<div class="command">
17. トリガー遅延パラメータの設定 - SetTriggerDelay
</div>

現在のトリガー遅延パラメータ（遅延方式と遅延パラメータ）を設定します。

<table>
<tr><td>コマンド</td><td>SetTriggerDelay</td></tr>
<tr><td>送信例</td><td>SetTriggerDelay,1,100;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
送信例の1番目の値は遅延方式です（0:オフ、1:距離、2:時間）。2番目の値は遅延パラメータです。<br>
方式が1の場合は遅延距離（単位:mm）、方式が2の場合は遅延時間（単位:ms）です。<br>
設定は次回のマーキングから有効になります。
</div>
</div>

<div class="no-break">
<div class="command">
18. ラインパイプトリガー間隔パラメータの取得 - GetPipIntveralDistance
</div>

現在のラインパイプトリガー間隔距離を取得します。

<table>
<tr><td>コマンド</td><td>GetPipIntveralDistance</td></tr>
<tr><td>送信例</td><td>GetPipIntveralDistance;;</td></tr>
<tr><td>返信例</td><td>100;;</td></tr>
</table>

<div class="annotation">
返信例の 100 は間隔距離を意味し、単位はmmです。
</div>
</div>

<div class="no-break">
<div class="command">
19. ラインパイプトリガー間隔パラメータの設定 - SetPipIntveralDistance
</div>

現在のラインパイプトリガー間隔距離を設定します。

<table>
<tr><td>コマンド</td><td>SetPipIntveralDistance</td></tr>
<tr><td>送信例</td><td>SetPipIntveralDistance,100;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
マーキングプロセス中に設定した場合、即時に有効になります。
</div>
</div>

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
1.bpd、2.bpd はテンプレート名を意味します。サブフォルダ内のファイルは取得されません。
</div>
</div>

<div class="no-break">
<div class="command">
21. 編集状態で指定テンプレートを開く - OpenDoc
</div>

指定されたテンプレートを開きます。このコマンドは編集状態でのみ有効です。

<table>
<tr><td>コマンド</td><td>OpenDoc</td></tr>
<tr><td>送信例</td><td>OpenDoc,sample.bpd;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
拡張子（.bpd）も入力します（例: 01.bpd）。サブフォルダ内のテンプレートを指定する場合は、フォルダ名/ファイル名.bpd と指定します。（例: OpenDoc,mydir/03.bpd）
</div>
</div>

<div class="no-break">
<div class="command">
22. マーキング状態で指定テンプレートを切り替え - SwitchDoc
</div>

指定されたテンプレートに切り替えます。このコマンドはマーキング状態でのみ有効です。実行後、現在加工中の場合は加工完了後に次のマーキングから有効になり、待機中の場合は次のマーキングから有効になります。

<table>
<tr><td>コマンド</td><td>SwitchDoc</td></tr>
<tr><td>送信例</td><td>SwitchDoc,sample.bpd;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
拡張子（.bpd）も入力します（例: 01.bpd）。サブフォルダ内のテンプレートを指定する場合は、フォルダ名/ファイル名.bpd と指定します。（例: SwitchDoc,mydir/03.bpd）
</div>
</div>

<div class="no-break">
<div class="command">
23. テンプレートの保存 - SaveCurrentDoc
</div>

現在のテンプレートを保存します。このコマンドは非マーキング状態でのみ有効です。

<table>
<tr><td>コマンド</td><td>SaveCurrentDoc</td></tr>
<tr><td>送信例</td><td>SaveCurrentDoc;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

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
拡張子（.bpd）も入力します。
</div>
</div>

<div class="no-break">
<div class="command">
25. テンプレートの図形リストの取得 - GetShapeList
</div>

現在のテンプレートの図形オブジェクトリストを取得します。テンプレート内の図形の並び順で図形名が返されます。

<table>
<tr><td>コマンド</td><td>GetShapeList</td></tr>
<tr><td>送信例</td><td>GetShapeList;;</td></tr>
<tr><td>返信例</td><td>Shape1;Shape2;;</td></tr>
</table>

<div class="annotation">
Shape1 は最初の図形名、Shape2 は2番目の図形名を意味します。
</div>
</div>

<div class="no-break">
<div class="command">
26. 指定図形のテキスト内容の取得 - GetShapeData
</div>

指定した図形のテキスト内容を取得します（複数可）。この命令はテキスト、QRコード、バーコードにのみ有効です。編集状態では現在の内容、マーキング状態では前回マーキングされた内容が取得されます。

<table>
<tr><td>コマンド</td><td>GetShapeData</td></tr>
<tr><td>送信例</td><td>GetShapeData,Shape1,Shape2;;</td></tr>
<tr><td>返信例</td><td>text1;text2;;</td></tr>
</table>

<div class="annotation">
text1 は1番目の図形のテキスト内容、text2 は2番目の図形のテキスト内容を意味します。
</div>
</div>

<div class="no-break">
<div class="command">
27. 指定図形の位置の取得 - GetShapePos
</div>

指定した図形の位置を取得します（複数可）。図形のRect(x, y, w, h)、つまり左下座標と幅、高さを返します。

<table>
<tr><td>コマンド</td><td>GetShapePos</td></tr>
<tr><td>送信例</td><td>GetShapePos,Shape1,Shape2;;</td></tr>
<tr><td>返信例</td><td>Shape1,x1,y1,w1,h1;Shape2,x2,y2,w2,h2;;</td></tr>
</table>

<div class="annotation">
Shape1 は最初の図形名、Shape2 は2番目の図形名を表しています。<br>
x1,y1,w1,h1 は最初の図形の位置、x2,y2,w2,h2 は2番目のテキストオブジェクトの位置を表しています。<br>
テキスト、QRコード、バーコード、図形のみをサポートしています。
</div>
</div>

<div class="no-break">
<div class="command">
28. 指定図形の位置の設定 - SetShapePos
</div>

指定した図形の位置を設定します（複数可）。Rect(x,y,w,h) は図元の左下座標 x,y と幅 w、高さ h を指します。

<table>
<tr><td>コマンド</td><td>SetShapePos</td></tr>
<tr><td>送信例</td><td>SetShapePos,Shape1,x1,y1,w1,h1;Shape2,x2,y2,w2,h2;;</td></tr>
<tr><td>返信例</td><td>ok;;</td></tr>
</table>

<div class="annotation">
Shape1 は最初の図形名、Shape2 は2番目の図形名を表しています。<br>
x1,y1,w1,h1 は最初の図形の位置、x2,y2,w2,h2 は2番目のテキストオブジェクトの位置を表しています。<br>
Failed,ErrorInfo は設定失敗を表し、ErrorInfo は具体的な失敗ログを表します。<br>
テキスト、QRコード、バーコード、図形のみをサポートしています。
</div>
</div>

<div class="no-break">
<div class="command">
29. 指定図形のテキスト内容、位置、角度の設定 - SetShapeData
</div>

図形のテキスト内容、位置、角度を設定します。
テキスト設定は「文字・QRコード・バーコード」にのみ有効で、該当オブジェクトに固定テキストが1つある場合に限られます。

<table>
<tr><td>コマンド</td><td>SetShapeData</td></tr>
<tr><td>送信例</td><td>SetShapeData,Shape1,text1,posx1,posy1,postype1,angle1,cx1,cy1,0;Shape2,text2,posx2,posy2,postype2,angle2,cx2,cy2,0;;</td></tr>
<tr><td>返信例</td><td>ok;;</td></tr>
</table>

<div class="annotation">
Shape1: 対象の図形名。空の場合はすべての図形が対象となります（その場合、図形のテキスト内容は設定不可）<br>
text1: 図形のテキスト内容を指定します。<br>
posx1: 相対移動時のX方向のオフセット値、絶対移動時の図形中心点のX座標を指定します。<br>
posy1: は相対移動時のY方向のオフセット値、絶対移動時の図形中心点のY座標を指定します。<br>
postype1: 0 が相対移動、1 が絶対移動を指定します。<br>
angle1: 相対回転角度を指定します。<br>
cx1: 回転中心点のX座標を表し、空の場合は図形自体を中心に回転します。<br>
cy1: 回転中心点のY座標を表し、空の場合は図形自体を中心に回転します。<br>
0: 相対回転を表す固定値であり、省略可能です。<br>
<br>
パラメータは省略可能です。例えば、テキスト内容のみを変更したい場合、text1以降のデータはすべて送信しなくても構いません。<br>
例1: Shape1 の内容を text1 に、Shape2 の内容を text2 に変更するには、以下のコマンドを使用します。<br>
SetShapeData,Shape1,text1;Shape2,text2;;<br>
例2: すべての図形を全体として中心点に移動するには、以下のコマンドを使用します。<br>
SetShapeData,,,0,0,1;;
</div>
</div>

<div class="no-break">
<div class="command">
30. キャッシュデータを送信して指定図形のテキスト、位置、角度を変更（典型的なビジョンマーキング通信応用） - PushShapeData
</div>

キャッシュデータを送信して指定図形のテキスト、位置、角度を変更します。このコマンドは、システムがマーキング状態に入り、かつ外部通信キャッシュモードが有効な場合のみ使用できます。
テキスト設定は「文字・QRコード・バーコード」にのみ有効で、該当オブジェクトに固定テキストが1つある場合に限られます。

<table>
<tr><td>コマンド</td><td>PushShapeData</td></tr>
<tr><td>送信例</td><td>PushShapeData,Shape1,text1,posx1,posy1,postype1,angle1,cx1,cy1,0;Shape2,text2,posx2,posy2,postype2,angle2,cx2,cy2,0;;</td></tr>
</table>

<div class="annotation">
各パラメータの概要は上記を参照してください。<br>
位置オフセットと角度回転は、図形の基本状態に対して毎回加算的に適用されます（前回の操作結果は失われます）。処理順序は「並行移動→回転」です。<br>
例: ビジョンマーキングで、まず全図形を相対移動(10,20)し、その後全図形の中心を基準に90°回転させる: PushShapeData,,,10,20,0,,,90;;
</div>
</div>

<div class="no-break">
<div class="command">
31. キャッシュデータのクリア - ClearCache
</div>

PushShapeDataで送信されたすべてのデータをクリアします。

<table>
<tr><td>コマンド</td><td>ClearCache</td></tr>
<tr><td>送信例</td><td>ClearCache;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<div class="no-break">
<div class="command">
32. 指定ベクターグラフィックファイルの変更 - SetVectorgraphData
</div>

指定したベクターグラフィック図形の内容を変更します。このコマンドは編集状態でのみ有効です。

<table>
<tr><td>コマンド</td><td>SetVectorgraphData</td></tr>
<tr><td>送信例</td><td>SetVectorgraphData,Shape1,plt,data;;</td></tr>
</table>

<div class="annotation">
Shape1: 変更対象のベクター図形名<br>
plt: ベクターファイル形式（plt, dxf, aiをサポート）<br>
data: ベクターファイルのデータストリーム
</div>
</div>

<div class="no-break">
<div class="command">
33. 指定ペン番号のペンパラメータ内容の取得 - GetPen
</div>

指定したペン番号のパラメータ内容を取得します。

<table>
<tr><td>コマンド</td><td>GetPen</td></tr>
<tr><td>送信例</td><td>GetPen,0,MarkSpeed,Power;;</td></tr>
<tr><td>返信例</td><td>4000,80;;</td></tr>
</table>

<div class="annotation">
送信例の 0 はペン番号0（0～15まで対応）を表します。<br>
MarkSpeed(マーキング速度)、JumpSpeed(ジャンプ速度)、Power(パワー)、PW(パルス幅)、Freq(周波数)、PointTime(ドット時間)などのパラメータを取得できます。<br>
返信例の 4000 はマーキング速度、80 はパワーを意味します。
</div>
</div>

<div class="no-break">
<div class="command">
34. 指定ペン番号のペンパラメータ内容の設定 - SetPen
</div>

指定したペン番号のパラメータ内容を設定します。設定は次にマーキング状態に入る時に有効になります。

<table>
<tr><td>コマンド</td><td>SetPen</td></tr>
<tr><td>送信例</td><td>SetPen,ID,0;MarkSpeed,4000;Power,80;;</td></tr>
</table>

<div class="annotation">
ID,0: ペン番号 0 を指定<br>
MarkSpeed,4000: マーキング速度を 4000 に設定<br>
Power,80: パワーを 80 に設定
</div>
</div>

<div class="no-break">
<div class="command">
35. マーキングする図形オブジェクトの指定 - MarkShape
</div>

マーキングプロセス中に、マーキング対象のテキストオブジェクトを指定します。（指定対象はテキスト・QRコード・バーコードに限ります）
このコマンドはマーキング状態でのみ有効で、次のマーキングから即時有効になります。

<table>
<tr><td>コマンド</td><td>MarkShape</td></tr>
<tr><td>送信例</td><td>MarkShape,Shape1,Shape2;;</td></tr>
</table>

<div class="annotation">
Shape1、Shape2 はマーキングしたい図形名を指定します。<br>
テンプレート内の全図形をマーキングする場合は、MarkShape;; と送信します。
</div>
</div>

<div class="no-break">
<div class="command">
36. マーキング状態の開始 - StartMark
</div>

システムをマーキング状態モードに移行させます。

<table>
<tr><td>コマンド</td><td>StartMark</td></tr>
<tr><td>送信例</td><td>StartMark;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<div class="no-break">
<div class="command">
37. マーキング状態の終了 - StopMark
</div>

システムをアイドル状態モードに移行させます。

<table>
<tr><td>コマンド</td><td>StopMark</td></tr>
<tr><td>送信例</td><td>StopMark;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<div class="no-break">
<div class="command">
38. 赤色光プレビュー状態の開始 - StartRedMark
</div>

システムを赤色光プレビュー状態モードに移行させます。

<table>
<tr><td>コマンド</td><td>StartRedMark</td></tr>
<tr><td>送信例</td><td>StartRedMark;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<div class="no-break">
<div class="command">
39. 手動トリガー（光電トリガーシミュレーション） - ManualTrgger
</div>

システムがトリガー待ち状態の時に、このコマンドでマーキングをトリガーできます。マーキング状態でのみ有効です。

<table>
<tr><td>コマンド</td><td>ManualTrgger</td></tr>
<tr><td>送信例</td><td>ManualTrgger;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<div class="no-break">
<div class="command">
40. シリアル番号のリセット - ClearSN
</div>

テンプレート内のすべてのシリアル番号を初期値にリセットします。マーキング中にリセットした場合、次のマーキングから有効になります。

<table>
<tr><td>コマンド</td><td>ClearSN</td></tr>
<tr><td>送信例</td><td>ClearSN;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<div class="no-break">
<div class="command">
41. システム状態の返信 - MarkStatus
</div>

システム状態が変化した際に、能動的に状態変化をフィードバックします。システムインターフェースでこの機能を有効にする必要があります。

<table>
<tr><td>コマンド</td><td>MarkStatus</td></tr>
<tr><td>返信例</td><td>MarkStatus:2;;</td></tr>
</table>

<div class="annotation">
返信例の 2 はマーキング状態を意味します。(0:アイドル / 1:シミュレーション / 2:マーキング / 3:赤色光プレビュー / 4:補正テスト / 5:赤色光補正テスト / 6:強制出光 / 7:回転マーキング)
</div>
</div>

<div class="no-break">
<div class="command">
42. システムマーキング完了回数の返信 - MarkCount
</div>

システムが1回のマーキングを完了した後、能動的に総マーキング回数をフィードバックします。

<table>
<tr><td>コマンド</td><td>MarkCount</td></tr>
<tr><td>返信例</td><td>MarkCount:2;;</td></tr>
</table>

<div class="annotation">
返信例の 2 は総マーキング回数を意味します。
</div>
</div>

<div class="no-break">
<div class="command">
43. システムマーキング内容の返信 - MarkData
</div>

システムが1回のマーキングを完了した後、能動的に現在のマーキング内容をフィードバックします。

<table>
<tr><td>コマンド</td><td>MarkData</td></tr>
<tr><td>返信例</td><td>MarkData:text1text2;;</td></tr>
</table>

<div class="annotation">
返信例の text1text2 は図形1、図形2のテキスト内容を意味します。
</div>
</div>

<div class="no-break">
<div class="command">
44. システムマーキング漏れ回数の返信 - MissCount
</div>

システムがマーキング漏れを検出した後、能動的に漏れ回数をフィードバックします。

<table>
<tr><td>コマンド</td><td>MissCount</td></tr>
<tr><td>返信例</td><td>MissCount:1;;</td></tr>
</table>

<div class="annotation">
返信例の 1 は総マーキング漏れ回数を意味します。
</div>
</div>

<div class="no-break">
<div class="command">
45. システム現在テンプレート名の取得 - GetCurDoc
</div>

システムの現在のテンプレート名を取得します。

<table>
<tr><td>コマンド</td><td>GetCurDoc</td></tr>
<tr><td>送信例</td><td>GetCurDoc;;</td></tr>
<tr><td>返信例</td><td>1.bpd;;</td></tr>
</table>
</div>

<div class="no-break">
<div class="command">
46. 指定図形のシリアル番号インデックスと現在シリアル番号リストの取得 - GetShapeSnIndex
</div>

指定した図形のシリアル番号インデックスとその現在のシリアル番号リストを取得します。

<table>
<tr><td>コマンド</td><td>GetShapeSnIndex</td></tr>
<tr><td>送信例</td><td>GetShapeSnIndex,ShapeName;;</td></tr>
<tr><td>返信例</td><td>1,3;2,4;;</td></tr>
</table>

<div class="annotation">
ShapeName は取得したい図形名です。1,3;2,4;;は、この図形に2つのシリアル番号があり、1つ目のインデックスは1で現在の番号は3、2つ目のインデックスは2で現在の番号は4であることを示します。
</div>
</div>

<div class="no-break">
<div class="command">
47. 指定図形の指定シリアル番号インデックスの現在シリアル番号を変更 - SetShapeSnCurNum
</div>

指定した図形の指定したシリアル番号インデックスの現在のシリアル番号を変更します。

<table>
<tr><td>コマンド</td><td>SetShapeSnCurNum</td></tr>
<tr><td>送信例</td><td>SetShapeSnCurNum,shapeName,index,num;;</td></tr>
</table>

<div class="annotation">
shapeName は図形名、index はシリアル番号インデックス、num は設定する現在のシリアル番号です。
</div>
</div>

<div class="no-break">
<div class="command">
48. システム時間の変更（試用期間中は変更不可） - SetSystemTime
</div>

システムの設定時刻を変更します。

<table>
<tr><td>コマンド</td><td>SetSystemTime</td></tr>
<tr><td>送信例</td><td>SetSystemTime,strTime;;</td></tr>
</table>

<div class="annotation">
strTime は時間文字列で、例は 2024-09-11 11:33:33 です（中間は半角スペース1つ）。
</div>
</div>

<div class="no-break">
<div class="command">
49. フォントリストの取得 - GetFontList
</div>

システムのフォントリストを取得します。

<table>
<tr><td>コマンド</td><td>GetFontList</td></tr>
<tr><td>送信例</td><td>GetFontList;;</td></tr>
<tr><td>返信例</td><td>0,1:xxx,xxx;2:xxx,xxx;3:xxx,xxx;4:xxx,xxx;;;</td></tr>
</table>

<div class="annotation">
返信例の 0 は成功を意味します。<br>
1:シングルラインフォント、2:ダブルラインフォント、3:ドットマトリックスフォント、4:TTFフォント、はフォントタイプを意味します。<br>
xxx,xxxはカンマ区切りのフォント名リストです。
</div>
</div>

<div class="no-break">
<div class="command">
50. テキストフォントの設定 - SetTextFont
</div>

テンプレート内のテキストのフォントタイプを設定します。

<table>
<tr><td>コマンド</td><td>SetTextFont</td></tr>
<tr><td>送信例</td><td>SetTextFont,shapeName,fontType,fontName;;</td></tr>
</table>

<div class="annotation">
shapeName はテキスト図形名、fontType は上記のフォントタイプ（1,2,3,4）のいずれか、fontName はフォント名です。
</div>
</div>

<div class="no-break">
<div class="command">
51. シリアル番号の設定 - SetShapeSnData
</div>

シリアル番号の属性（開始番号、終了番号、現在番号、増分、リピート回数、達成回数など）を変更します。

<table>
<tr><td>コマンド</td><td>SetShapeSnData</td></tr>
<tr><td>送信例</td><td>SetShapeSnData,shapeName,snIndex,startNum,endNum,curNum,stepNum,repeatNum,repeatIndex;;</td></tr>
</table>

<div class="annotation">
パラメータをすべて変更する必要がない場合は、カンマ区切り記号を残してください。例：SetShapeSnData,textT3,1,,,80,,,;; は、シリアル番号の現在番号を80に変更します。
</div>
</div>

<div class="no-break">
<div class="command">
52. シリアル番号のリセット - ResetShapeSn
</div>

シリアル番号（現在番号、達成回数）をリセットします。

<table>
<tr><td>コマンド</td><td>ResetShapeSn</td></tr>
<tr><td>送信例</td><td>ResetShapeSn,shapeName,snIndex,curNum,repeatIndex;;</td></tr>
</table>

<div class="annotation">
shapeName はシリアル番号を含む図形名、snIndex はその図形内のシリアル番号変数のインデックス（1から）、curNum は現在番号、repeatIndex は達成回数です。
</div>
</div>

<div class="no-break">
<div class="command">
53. 編集状態で指定テンプレートを開いて刻印 - OpenDocMark
</div>

指定したテンプレートを開いた後、そのままマーキングを開始します。

<table>
<tr><td>コマンド</td><td>OpenDocMark</td></tr>
<tr><td>送信例</td><td>OpenDocMark,file;;</td></tr>
<tr><td>返信例</td><td>1.bpd;2.bpd;;</td></tr>
</table>
</div>

<div class="no-break">
<div class="command">
54. マーキング後に入力欄に刻印文字列を表示 - GetMarkCountStr
</div>

「打刻完了上報文字」を有効にし、後ろに文字列を入力すると、毎回の打刻完了後にその文字列を上報します。

</div>

<div class="no-break">
<div class="command">
55. キャッシュモードの設定 - SetDataEffectiveMode
</div>

キャッシュモードの有効／無効を切り替えます。（編集状態でのみ変更可）

<table>
<tr><td>コマンド</td><td>SetDataEffectiveMode</td></tr>
<tr><td>送信例</td><td>SetDataEffectiveMode,mode;;</td></tr>
<tr><td>返信例</td><td>ok;;</td></tr>
</table>

<div class="annotation">
mode はオン／オフを表します（0: オン / 1: オフ）。
</div>
</div>

<div class="no-break">
<div class="command">
56. ID オブジェクトの選択状態を設定 - SetShapeSelectState
</div>

指定した図形（ID を持つオブジェクト）の選択／非選択を切り替えます。

<table>
<tr><td>コマンド</td><td>SetShapeSelectState</td></tr>
<tr><td>送信例</td><td>SetShapeSelectState,shapeName,mode;;</td></tr>
<tr><td>返信例</td><td>ok;;</td></tr>
</table>

<div class="annotation">
shapeName はIDを持つ図形名、mode は選択状態を表します（0: 非選択/1: 選択）。
</div>
</div>

<div class="no-break">
<div class="command">
57. オブジェクトのマーキング可否を設定 - SetSelectMark
</div>

ID オブジェクトに対して、マーキングするかどうかを切り替えます。

<table>
<tr><td>コマンド</td><td>SetSelectMark</td></tr>
<tr><td>送信例</td><td>SetSelectMark,mode;;</td></tr>
<tr><td>返信例</td><td>ok;;</td></tr>
</table>

<div class="annotation">
mode はマーキングの有無を表します（0: 無効 / 1: 有効）。
</div>
</div>

<div class="no-break">
<div class="command">
58. 連続マーキングの設定 - SetContinueMark
</div>

ID オブジェクトに対して、連続して打刻するかどうかを切り替えます。

<table>
<tr><td>コマンド</td><td>SetContinueMark</td></tr>
<tr><td>送信例</td><td>SetContinueMark,mode;;</td></tr>
<tr><td>返信例</td><td>ok;;</td></tr>
</table>

<div class="annotation">
mode は連続マーキングの有無を表します（0: 無効 / 1: 有効）。
</div>
</div>

<div class="no-break">
<div class="command">
59. 指定テキストオブジェクトのフォントパラメータ設定 - SetShapeFont
</div>

テキストオブジェクトの文字高と字間を設定します。

<table>
<tr><td>コマンド</td><td>SetShapeFont</td></tr>
<tr><td>送信例</td><td>SetShapeFont,shapeName,height,width;;</td></tr>
<tr><td>返信例</td><td>ok;;</td></tr>
</table>

<div class="annotation">
shapeName はIDオブジェクトの図形名、height は文字の高さ、width は文字間隔を表します。
</div>
</div>

<div class="no-break">
<div class="command">
60. 外部データのテキスト内容を設定 - SetVD
</div>

外部データのテキスト内容を設定します。編集中に送ると即時反映。打刻中に送る場合、刻印動作中なら終了後の次回から、待機中なら次回から即時反映されます。

<table>
<tr><td>コマンド</td><td>SetVD</td></tr>
<tr><td>送信例</td><td>SetVD,text1,text2,text3...textN;;</td></tr>
<tr><td>返信例</td><td>SetVD,Ok;;</td></tr>
</table>

<div class="annotation">
text1 はチャネル1の外部テキスト、text2 はチャネル2の外部テキストです。<br>

</div>
</div>

<div class="no-break">
<div class="command">
61. 外部データのテキスト内容をキャッシュ方式で設定 - PushVD
</div>

外部データのテキスト内容を設定します。打刻中のみ有効で、データは送信順に順次実行されます。

<table>
<tr><td>コマンド</td><td>PushVD</td></tr>
<tr><td>送信例</td><td>PushVD,text1,text2,text3...textN;;</td></tr>
<tr><td>返信例</td><td>PushVD,Ok;;</td></tr>
</table>

<div class="annotation">
text1 はチャネル1の外部テキスト、text2 はチャネル2の外部テキストです。<br>

</div>
</div>





</div>