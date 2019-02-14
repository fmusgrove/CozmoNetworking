import asyncio
import cozmo
from websocket_interface import WebsocketInterface
from colors import Colors
from cozmo.util import distance_mm, speed_mmps, degrees


# region CubeAction Class
class CozmoDance:
    def __init__(self, robot: cozmo.robot.Robot, name: str):
        self.robot = robot
        self.name = name

    async def move_to_cube(self, cube):
        await self.robot.go_to_object(cube, distance_mm(100.0)).wait_for_completed()
        await self.robot_say(f'Moved to cube {cube.cube_id}')

    async def robot_say(self, text):
        await self.robot.say_text(text, duration_scalar=0.6).wait_for_completed()

    async def move_forward(self, distance):
        await self.robot.drive_straight(distance_mm(distance), speed_mmps(150)).wait_for_completed()

    async def turn_in_place(self):
        await self.robot.turn_in_place(degrees(180)).wait_for_completed()

    async def turn_clockwise(self):
        """
        Turn clockwise in place (right)
        """
        await self.robot.turn_in_place(degrees(-90)).wait_for_completed()

    async def turn_counterclockwise(self):
        """
        Turn counterclockwise in place (left)
        """
        await self.robot.turn_in_place(degrees(90)).wait_for_completed()

    async def run_command(self, instructions):
        """
        Run the command on Cozmo set in the instructions param
        :param instructions: instruction dictionary object to tell Cozmo how to move
        """
        if 'movement' in instructions:
            if self.name == instructions['movement']['name']:
                print(f'Received Message: {instructions}')
                move_instructions = instructions['movement']

                if move_instructions['dist_x'] > 0:
                    if move_instructions['FB'] == 'F':
                        await self.move_forward(move_instructions['dist_x'])
                    elif move_instructions['FB'] == 'B':
                        await self.turn_in_place()
                        await self.move_forward(move_instructions['dist_x'])

                if move_instructions['dist_y'] > 0:
                    if move_instructions['LR'] == 'L':
                        await self.turn_counterclockwise()
                        await self.move_forward(move_instructions['dist_y'])
                    elif move_instructions['LR'] == 'R':
                        await self.turn_clockwise()
                        await self.move_forward(move_instructions['dist_y'])

        elif 'head_lift' in instructions:
            if self.name == instructions['head_lift']['name']:
                print(f'Received Message: {instructions}')
                head_lift_instructions = instructions['head_lift']

                if head_lift_instructions['head_pos'] > 0:
                    head_angle = max(-25.0, min(head_lift_instructions['head_pos'], 44.5))
                    self.robot.set_head_angle(degrees(head_angle), in_parallel=True)

                if head_lift_instructions['lift_pos'] > 0:
                    lift_height = max(0.0, min(head_lift_instructions['lift_pos'], 1.0))
                    self.robot.set_lift_height(lift_height, in_parallel=True)

    async def run(self):
        self.robot.set_all_backpack_lights(Colors.GREEN)
        await self.robot_say('Program running')


# endregion


async def cozmo_program(robot: cozmo.robot.Robot):
    cozmo_dance = CozmoDance(robot, name='Cozmo117AE')
    websocket = WebsocketInterface(ip_address='127.0.0.1', port=5000, name='Cozmo117AE')
    websocket.start()

    # Wait to receive keyboard interrupt command to exit (CTRL-C)
    while True:
        # Grab commands off queue and run them on Cozmo
        command = websocket.command_queue.get()
        await cozmo_dance.run_command(command)
        await asyncio.sleep(0.5)


cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
