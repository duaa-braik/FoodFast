from flask import Flask
from flask_sock import Sock
import threading, time, websocket

app = Flask(__name__)
sock = Sock(app)

peerSocket = None

port = 5001
peerPort = 5000

def connectToPeer(peerPort):
    global peerSocket
    url = f"ws://localhost:{peerPort}/ws"
    while True:
        try:
            print(f"Trying to connect to peer at {url}")
            peerSocket = websocket.WebSocket()
            peerSocket.connect(url)
            print(f"Connected to peer at {url}")
            break
        except Exception as e:
            print("Retrying...", e)
            time.sleep(2)

@sock.route('/ws')
def onMessageReceive(ws):
    while True:
        message = ws.receive()
        if message is None:
            break

        if message.startswith(str(peerPort)):
            print(message)
            continue
        else:
            print(f"{port} - me: {message}")

        if peerSocket:
            peerSocket.send(f"{port}: {message}")

if __name__ == "__main__":
    thread = threading.Thread(target=connectToPeer, args=(peerPort,), daemon=True)
    thread.start()

    app.run(host="0.0.0.0", port=port)
