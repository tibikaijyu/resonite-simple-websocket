# Resonite WebSocket シンプルサーバー

このプロジェクトは、PythonでWebSocketサーバーを作成し、Resoniteからメッセージを送受信するサンプルコードです。  
Resonite内で**ProtoFlux**を使用し、外部のWebSocketサーバーと通信する方法を学ぶことができます。

## 必要な環境
- Python 3.8 以上
- `websockets` ライブラリ
- Resonite

## インストール方法

### 1. Python環境をセットアップする
Pythonがインストールされていない場合は、[公式サイト](https://www.python.org/downloads/) からインストールしてください。

### 2. 必要なライブラリをインストールする
ターミナル（コマンドプロンプト）で、以下のコマンドを実行します。

```sh
pip install websockets
```

## WebSocketサーバーの実行

### 1. サーバーを起動
以下のコマンドを実行すると、WebSocketサーバーが `ws://localhost:5000` で起動します。

```sh
python sample_websocket.py
```

サーバーが正しく起動すると、以下のようなメッセージが表示されます。

```
WebSocketサーバーが起動しました: ws://localhost:5000
```

### 2. Resonite との接続
以下のResoniteのサンプルアイテムを使用してWebSocketに接続してください。

サンプルフォルダのURL:
```
resrec:///U-1bCJumeOF28/R-4FD0749534DDE8159846B923E56AF1251ADC4340D3B6F48D062FFFE8BE7B2B41
```

**Websocket Connect** を実行すると、サーバーと接続されます。  
**Websocket Text Message Sender** を実行すると、サーバーへメッセージが送信されます。

## WebSocketの動作

### クライアント（Resonite）が送るメッセージ
- JSON形式のデータを送信すると、サーバーがそのデータをエコー（返信）します。
- JSONでないテキストメッセージも、そのまま返信されます。

### サーバーのレスポンス
| 送信データ  | サーバーの応答 |
|------------|--------------|
| `{"name": "Alice"}` | `{"echo": {"name": "Alice"}, "status": "success"}` |
| `Hello WebSocket!` | `Echo: Hello WebSocket!` |

## サーバーの停止
サーバーを停止するには、Ctrl + C を押します。

```
^C
サーバーを終了しました
```

## 免責事項
本プロジェクトは学習目的で提供されるものです。  
本ソフトウェアを使用することによって生じたいかなる損害やトラブルについても、開発者は一切の責任を負いません。  
また、本ソフトウェアをResoniteの公式サポートなしに使用する場合、その影響については自己責任で行ってください。

## 参考情報
- [Python WebSockets ライブラリ](https://websockets.readthedocs.io/)
- [Resonite 公式サイト](https://resonite.com/)

このプロジェクトを活用して、Resoniteと外部プログラムを連携する方法を学んでください。