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
    # Command Bank:
    # Move head down:
    # s.send(b'Cozmo117AE; )
    #
    #
    #
    #
    #
    #

    s = socket.socket()
    s.connect(("10.0.1.10", 5000))

    s.send(b'Cozmo117AE;56.4;20.3')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;F;L;300;200')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;20.8;45.2')


def p2p_network_commands():
    host = '127.0.0.1'
    port = 5000

    p2p_socket = socket.socket()
    p2p_socket.connect((host, port))

    messages = [b'Cozmo117AE;56.4;20.3', b'Cozmo117AE;F;L;300;200', b'Cozmo117AE;20.8;45.2']

    for message in messages:
        p2p_socket.send(message)
        # data = p2p_socket.recv(1024).decode()
        # print('Received from server: ' + data)

    p2p_socket.close()


if __name__ == "__main__":
    p2p_network_commands()
