import asyncio
from websocket_interface import WebsocketInterface
import socket
import time

async def send_instructions_ws():
    s = WebsocketInterface(url='ws://10.0.1.10:5000')
    s.init()

    s.ws.send('Cozmo117AE;56.4;20.3')
    await asyncio.sleep(0.5)
    s.ws.send('Cozmo117AE;F;L;300;200')
    await asyncio.sleep(0.5)
    s.ws.send('Cozmo117AE;20.8;45.2')

def send_instructions_socket():
    s = socket.socket()
    s.connect(("10.0.1.10", 5000))

    s.send(b'Cozmo117AE;56.4;20.3')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;F;L;300;200')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;20.8;45.2')

if __name__ == "__main__":
    send_instructions_socket()