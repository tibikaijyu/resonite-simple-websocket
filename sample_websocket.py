import asyncio
import websockets
import json

# クライアントとの通信処理
async def handle_client(websocket):
    print("クライアントが接続しました")

    try:
        # クライアントからのメッセージを受信
        async for message in websocket:
            print(f"受信: {message}")

            try:
                # JSONデータとして解析
                data = json.loads(message)
                print(f"JSONデータ受信: {data}")

                # クライアントにJSON形式で返信
                response = {"echo": data, "status": "success"}
                await websocket.send(json.dumps(response))
                print(f"送信(JSON): {response}")

            except json.JSONDecodeError:
                # JSONでない場合はそのままエコー返信
                response = f"Echo: {message}"
                await websocket.send(response)
                print(f"送信(テキスト): {response}")

    except websockets.exceptions.ConnectionClosed as e:
        print(f"クライアントが切断されました (コード: {e.code}, 理由: {e.reason})")

# WebSocketサーバーを起動する関数
async def start_server():
    server = await websockets.serve(handle_client, "localhost", 5000)
    print("WebSocketサーバーが起動しました: ws://localhost:5000")
    await server.wait_closed()

# メイン処理
if __name__ == "__main__":
    try:
        asyncio.run(start_server())  # WebSocketサーバーを起動
    except KeyboardInterrupt:
        print("サーバーを終了しました")
