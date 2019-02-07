import asyncio
import cozmo
from websocket_interface import WebsocketInterface

from colors import Colors
from cozmo.util import distance_mm


# region CubeAction Class
class CozmoDance:
    def __init__(self, robot: cozmo.robot.Robot):
        self.robot = robot

    async def move_to_cube(self, cube):
        await self.robot.go_to_object(cube, distance_mm(100.0)).wait_for_completed()
        await self.robot_say(f'Moved to cube {cube.cube_id}')

    async def robot_say(self, text):
        await self.robot.say_text(text, duration_scalar=0.6).wait_for_completed()

    def on_cozmo_message(self, msg):
        # TODO: Handle message
        print(msg)

    async def run(self):
        self.robot.set_all_backpack_lights(Colors.GREEN)
        await self.robot_say('Program running')


# endregion


async def cozmo_program(robot: cozmo.robot.Robot):
    cozmo_dance = CozmoDance(robot)
    s = WebsocketInterface(url='10.0.1.10:5000', cozmo_message_callback=cozmo_dance.on_cozmo_message)
    s.init()
    await cozmo_dance.run()

    # Wait to receive keyboard interrupt command to exit (CTRL-C)
    while True:
        await asyncio.sleep(0.5)


cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
