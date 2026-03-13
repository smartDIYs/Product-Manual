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
0: アイドル（待機） / 1: シミュレーション中 / 2: マーキング中 / 3: プレビュー中 / 4: レーザー校正テスト中 / 5: 赤色ガイド光校正テスト中 / 6: レーザー強制出力中 / 7: 回転マーキング中 / 8: 赤色ガイド光フォーカス中
</div>
</div>

<!-- Original ID: 3 -->
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

<!-- Original ID: 4 -->
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

<!-- Original ID: 5 -->
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

<!-- Original ID: 6 -->
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

<!-- Original ID: 7 -->
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

<!-- Original ID: 20 -->
<div class="no-break">
<div class="command">
8. テンプレートリストの取得 - GetDocList
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

<!-- Original ID: 21 -->
<div class="no-break">
<div class="command">
9. 編集状態で指定テンプレートを開く - OpenDoc
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

<!-- Original ID: 22 -->
<div class="no-break">
<div class="command">
10. マーキング状態で指定テンプレートを切り替え - SwitchDoc
</div>

指定されたテンプレートに切り替えます。このコマンドはマーキング状態でのみ有効です。実行後、現在加工中の場合は加工完了後に次のマーキングから有効になり、待機中の場合は次のマーキングから有効になります。パラメータの変更を含む場合は一度マーキング状態を終了し、再度開始する必要があります。

<table>
<tr><td>コマンド</td><td>SwitchDoc</td></tr>
<tr><td>送信例</td><td>SwitchDoc,sample.bpd;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>

<div class="annotation">
拡張子（.bpd）も入力します（例: 01.bpd）。サブフォルダ内のテンプレートを指定する場合は、フォルダ名/ファイル名.bpd と指定します。（例: SwitchDoc,mydir/03.bpd）
</div>
</div>

<!-- Original ID: 23 -->
<div class="no-break">
<div class="command">
11. テンプレートの保存 - SaveCurrentDoc
</div>

現在のテンプレートを保存します。このコマンドは非マーキング状態でのみ有効です。

<table>
<tr><td>コマンド</td><td>SaveCurrentDoc</td></tr>
<tr><td>送信例</td><td>SaveCurrentDoc;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 24 -->
<div class="no-break">
<div class="command">
12. テンプレートを名前を付けて保存 - SaveDocAs
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

<!-- Original ID: 25 -->
<div class="no-break">
<div class="command">
13. テンプレートの図形リストの取得 - GetShapeList
</div>

現在のテンプレートの図形オブジェクトリストを取得します。テンプレート内の図形の並び順で図形名が返されます。

<table>
<tr><td>コマンド</td><td>GetShapeList</td></tr>
<tr><td>送信例</td><td>GetShapeList;;</td></tr>
<tr><td>返信例</td><td>Shape1;Shape2;;</td></tr>
</table>

<div class="annotation">
Shape1 は最初の図形名、Shape2 は2番目の図形名を意味します。<br>
図形名（オブジェクト名）は「編集」タブの リスト からも確認できます。
</div>
</div>

<!-- Original ID: 26 -->
<div class="no-break">
<div class="command">
14. 指定図形のテキスト内容の取得 - GetShapeData
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

<!-- Original ID: 27 -->
<div class="no-break">
<div class="command">
15. 指定図形の位置の取得 - GetShapePos
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

<!-- Original ID: 28 -->
<div class="no-break">
<div class="command">
16. 指定図形の位置の設定 - SetShapePos
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

<!-- Original ID: 29 -->
<div class="no-break">
<div class="command">
17. 指定図形のテキスト内容、位置、角度の設定 - SetShapeData
</div>

図形のテキスト内容、位置、角度を設定します。位置設定の処理順序は「移動→回転」です。
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

<!-- Original ID: 30 -->
<div class="no-break">
<div class="command">
18. キャッシュデータを送信して指定図形のテキスト、位置、角度を変更 - PushShapeData
</div>

カメラを使用した位置補正システムとの連携に有効です。
このコマンドは、システムがマーキング状態に入り、かつ外部通信の「キャッシュモード」が有効な場合のみ使用できます。
基本的に元ファイルには変更を加えず、キャッシュデータを使用して指定図形の位置、角度を変更します。
テキスト設定は「文字・QRコード・バーコード」にのみ有効で、該当オブジェクトに固定テキストが1つある場合に限られます。
なお、テキスト内容を変更した場合は文字列のみ元データへ反映されます。

<table>
<tr><td>コマンド</td><td>PushShapeData</td></tr>
<tr><td>送信例</td><td>PushShapeData,Shape1,text1,posx1,posy1,postype1,angle1,cx1,cy1,0;Shape2,text2,posx2,posy2,postype2,angle2,cx2,cy2,0;;</td></tr>
</table>

<div class="annotation">
各パラメータの概要は上記を参照してください。<br>
刻印文字列がプレビュー画面に反映されるタイミングが遅い場合は、「パラメータ > 高度な設定 > リアルタイム更新」を有効にしてください。なお、位置や回転の変更はプレビュー画面へ反映されません。<br>
キャッシュサイズは「パラメータ > マーキング方法 > その他」にて設定します。<br>
例: 全図形を相対移動(10,20)し、その後全図形の中心を基準に90°回転させる場合<br>
PushShapeData,,,10,20,0,,,90;;
</div>
</div>

<!-- Original ID: 31 -->
<div class="no-break">
<div class="command">
19. キャッシュデータのクリア - ClearCache
</div>

PushShapeDataで送信されたすべてのデータをクリアします。

<table>
<tr><td>コマンド</td><td>ClearCache</td></tr>
<tr><td>送信例</td><td>ClearCache;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 32 -->
<div class="no-break">
<div class="command">
20. 指定ベクターグラフィックファイルの変更 - SetVectorgraphData
</div>

指定したベクターオブジェクトの内容を変更します。このコマンドは編集状態でのみ有効です。

<table>
<tr><td>コマンド</td><td>SetVectorgraphData</td></tr>
<tr><td>送信例</td><td>SetVectorgraphData,Shape1,plt,data;;</td></tr>
</table>

<div class="annotation">
Shape1: 変更対象のベクター図形名<br>
plt: ベクターファイル形式（plt, dxf, aiをサポート）<br>
data: ベクターファイルのデータストリーム<br>
通信速度が遅いとデータ送信中にタイムアウトになる可能があります。
</div>
</div>

<!-- Original ID: 33 -->
<div class="no-break">
<div class="command">
21. 指定ペン番号のペンパラメータ内容の取得 - GetPen
</div>

指定したペン番号のパラメータ内容を取得します。

<table>
<tr><td>コマンド</td><td>GetPen</td></tr>
<tr><td>送信例</td><td>GetPen,0,MarkSpeed,Power;;</td></tr>
<tr><td>返信例</td><td>4000,80;;</td></tr>
</table>

<div class="annotation">
送信例の 0 はペン番号 0（0～15まで対応）を表します。<br>
MarkSpeed(マーキング速度)、JumpSpeed(ジャンプ速度)、Power(パワー)、PW(パルス幅)、Freq(周波数)、PointTime(ドット時間)などのパラメータを取得できます。<br>
返信例の 4000 はマーキング速度、80 はパワーを意味します。
</div>
</div>

<!-- Original ID: 34 -->
<div class="no-break">
<div class="command">
22. 指定ペン番号のペンパラメータ内容の設定 - SetPen
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

<!-- Original ID: 35 -->
<div class="no-break">
<div class="command">
23. マーキングする図形オブジェクトの指定 - MarkShape
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

<!-- Original ID: 36 -->
<div class="no-break">
<div class="command">
24. マーキング状態の開始 - StartMark
</div>

システムをマーキング状態に移行させます。

<table>
<tr><td>コマンド</td><td>StartMark</td></tr>
<tr><td>送信例</td><td>StartMark;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 37 -->
<div class="no-break">
<div class="command">
25. マーキング状態の終了 - StopMark
</div>

システムをアイドル状態に移行させます。

<table>
<tr><td>コマンド</td><td>StopMark</td></tr>
<tr><td>送信例</td><td>StopMark;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 38 -->
<div class="no-break">
<div class="command">
26. プレビューの開始 - StartRedMark
</div>

システムをプレビュー状態に移行させます。

<table>
<tr><td>コマンド</td><td>StartRedMark</td></tr>
<tr><td>送信例</td><td>StartRedMark;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 39 -->
<div class="no-break">
<div class="command">
27. 手動トリガーの入力 - ManualTrgger
</div>

システムがトリガー待ち状態の時に、このコマンドでマーキングをトリガーできます。マーキング状態でのみ有効です。

<table>
<tr><td>コマンド</td><td>ManualTrgger</td></tr>
<tr><td>送信例</td><td>ManualTrgger;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 40 -->
<div class="no-break">
<div class="command">
28. シリアル番号のリセット - ClearSN
</div>

テンプレート内のすべてのシリアル番号を初期値にリセットします。マーキング中にリセットした場合、次のマーキングから有効になります。

<table>
<tr><td>コマンド</td><td>ClearSN</td></tr>
<tr><td>送信例</td><td>ClearSN;;</td></tr>
<tr><td>返信例</td><td>Ok;;</td></tr>
</table>
</div>

<!-- Original ID: 45 -->
<div class="no-break">
<div class="command">
29. 現在のテンプレート名の取得 - GetCurDoc
</div>

現在のテンプレート名を取得します。

<table>
<tr><td>コマンド</td><td>GetCurDoc</td></tr>
<tr><td>送信例</td><td>GetCurDoc;;</td></tr>
<tr><td>返信例</td><td>1.bpd;;</td></tr>
</table>
</div>






</div>