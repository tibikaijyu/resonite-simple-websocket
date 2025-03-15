# Resonite WebSocket Simple Server

This project provides a sample WebSocket server implemented in Python that can send and receive messages from **Resonite**.  
Using **ProtoFlux** within Resonite, you can communicate with an external WebSocket server.

## Requirements
- Python 3.8 or later
- `websockets` library
- Resonite

## Installation

### 1. Set up the Python environment
If Python is not installed, download and install it from the [official website](https://www.python.org/downloads/).

### 2. Install the required library
Run the following command in your terminal (or command prompt):

```sh
pip install websockets
```

## Running the WebSocket Server

### 1. Start the server
Run the following command to start the WebSocket server at `ws://localhost:5000`:

```sh
python sample_websocket.py
```

If the server starts successfully, you should see the following message:

```
WebSocket server started: ws://localhost:5000
```

### 2. Connecting from Resonite
Use the following **Resonite sample item** to connect to the WebSocket server.

Sample folder URL:
```
resrec:///U-1bCJumeOF28/R-4FD0749534DDE8159846B923E56AF1251ADC4340D3B6F48D062FFFE8BE7B2B41
```

- Executing **Websocket Connect** will establish a connection to the server.  
- Executing **Websocket Text Message Sender** will send a message to the server.

## WebSocket Behavior

### Messages sent from the client (Resonite)
- If a **JSON-formatted** message is sent, the server will echo back the data.
- If a **plain text message** is sent, the server will echo it back as is.

### Server response
| Sent Data | Server Response |
|------------|--------------|
| `{"name": "Alice"}` | `{"echo": {"name": "Alice"}, "status": "success"}` |
| `Hello WebSocket!` | `Echo: Hello WebSocket!` |

## Stopping the Server
To stop the server, press **Ctrl + C**.

```
^C
Server stopped
```

## Disclaimer
This project is provided for educational purposes only.  
The developer assumes no responsibility for any damages or issues resulting from the use of this software.  
Additionally, if you use this software without official support from Resonite, you do so **at your own risk**.

## References
- [Python WebSockets Library](https://websockets.readthedocs.io/)
- [Resonite Official Website](https://resonite.com/)

Use this project to learn how to integrate Resonite with external programs via WebSocket.