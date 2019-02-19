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
    #
    # Move head down:
    #   s.send(b'Cozmo117AE;-25.0;0')
    # 
    # Move head up:
    #   s.send(b'Cozmo117AE;45.0;0')
    #      
    # Move lift up:
    #   s.send(b'Cozmo117AE;0;1.0')
    #
    # Move lift down:
    #   s.send(b'Cozmo117AE;0;0.0')
    #
    # 360:
    #   s.send(b'Cozmo117AE;TS;0')
    #
    # Reverse:
    #   s.send(b'Cozmo117AE;F;-55')
    #
    #

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect(("10.0.1.10", 5000))
    except socket.error as msg:
        print('Socket failed to bind')
        exit(1)

    print('Connected to socket')

    # s.send(b'Cozmo117AE;56.4;20.3')
    # time.sleep(0.5)
    # s.send(b'Cozmo117AE;F;L;300;200')
    # time.sleep(0.5)
    # s.send(b'Cozmo117AE;20.8;45.2')

    # Start
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.1)
    s.send(b'Cozmo117AE;-25.0;0')
    time.sleep(7.5)
    s.send(b'Cozmo117AE;0.0;0')
    s.send(b'Cozmo117AE;F;L;-55;0')
    time.sleep(1)
    # 10 seconds in
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;TS;0')
    s.send(b'Cozmo117AE;TS;0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;F;L;25;0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;F;L;-25;0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;F;L;25;0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;F;L;-25;0')
    time.sleep(0.25)
    # 20 seconds in
    s.send(b'Cozmo117AE;F;L;0;200')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    # 30 seconds in
    s.send(b'Cozmo117AE;F;B;0;400')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    # 40 seconds in
    s.send(b'Cozmo117AE;F;B;0;200')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;0;1.0')
    s.send(b'Cozmo117AE;45.0;0')
    s.send(b'Cozmo117AE;RTS;0')
    s.send(b'Cozmo117AE;TS;0')
    s.send(b'Cozmo117AE;0.0;0')
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;F;L;-25;0')
    s.send(b'Cozmo117AE;0;1.0')
    s.send(b'Cozmo117AE;F;L;25;0')
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;TS;0')
    s.send(b'Cozmo117AE;TS;0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;F;L;25;0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;F;L;-25;0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;F;L;25;0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;F;L;-25;0')
    time.sleep(0.25)

    s.send(b'Cozmo117AE;F;L;0;200')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')

    s.send(b'Cozmo117AE;F;B;0;400')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')

    s.send(b'Cozmo117AE;F;B;0;200')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;1.0')
    time.sleep(0.25)
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;0;1.0')
    s.send(b'Cozmo117AE;45.0;0')
    s.send(b'Cozmo117AE;RTS;0')
    s.send(b'Cozmo117AE;TS;0')
    s.send(b'Cozmo117AE;0.0;0')
    s.send(b'Cozmo117AE;0;0.0')
    time.sleep(0.5)
    s.send(b'Cozmo117AE;F;L;-25;0')
    s.send(b'Cozmo117AE;0;1.0')
    s.send(b'Cozmo117AE;F;L;25;0')
    s.send(b'Cozmo117AE;0;0.0')


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
    send_instructions_socket()
