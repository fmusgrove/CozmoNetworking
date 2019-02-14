import asyncio
from websocket_interface import WebsocketInterface

async def send_instructions():
    s = WebsocketInterface(url='ws://10.0.1.10:5000')
    s.init()

    s.ws.send('Cozmo117AE;56.4;20.3')
    await asyncio.sleep(0.5)
    s.ws.send('Cozmo117AE;F;L;300;200')
    await asyncio.sleep(0.5)
    s.ws.send('Cozmo117AE;20.8;45.2')