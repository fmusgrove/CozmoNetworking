import time
from queue import Queue
from threading import Thread
import socket
import json


class WebsocketInterface:
    """
    Uses a WebSocketApp with callbacks to process and store server messages
    """

    def __init__(self, ip_address='10.0.1.10', port=5000, name='CozmoRobot'):
        self.ip_address = ip_address
        self.port = port
        self.name = name
        self.command_queue = Queue()
        self.last_message_time = time.time()
        self.socket: socket.socket = None
        self.thread = Thread(target=self._listen_on_socket, name='socket_thread', daemon=True)
        self.should_keep_alive = True
        self.file = open('messages.txt', 'w')

    def start(self):
        self.thread.start()

    def _listen_on_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.ip_address, self.port))
            print('Connected to socket')
        except socket.error as msg:
            print('Socket failed to bind')

        while self.should_keep_alive:
            data = self.socket.recv(4048).decode('utf-8')

            print(f'Preparsed message: {data}')

            if data == b'Cozmo117AE;done':
                self.should_keep_alive = False
                self.file.close()
                print('Closed file')

            command = WebsocketInterface.parse_message(data)
            self.file.write(json.dumps(command) + '\n')

            self.last_message_time = time.time()
            # Sometimes the command object will be None due to a set frame buffer size
            if command is not None:
                if self.name in command:
                    self.command_queue.put(command)

    @classmethod
    def parse_message(cls, message: str):
        """
        Parse the string message from the network into a Python readable object
        :param message: message string
        :return: parsed message object with the initial key being the instruction type
        """
        message_list = message.split(';')

        # Movement
        if len(message_list) == 5:
            keys = ['name', 'FB', 'LR', 'dist_x', 'dist_y']

            message_obj = dict(zip(keys, message_list))

            message_obj['dist_x'] = int(message_obj['dist_x'])
            message_obj['dist_y'] = int(message_obj['dist_y'])

            return {'movement': message_obj}
        # Head/lift positions
        elif len(message_list) == 3:
            keys = ['name', 'head_pos', 'lift_pos']

            message_obj = dict(zip(keys, message_list))

            message_obj['head_pos'] = float(message_obj['head_pos'])
            message_obj['lift_pos'] = float(message_obj['lift_pos'])

            return {'head_lift': message_obj}

    def close(self):
        print('Joining threads and exiting')
        self.socket.close()
        self.should_keep_alive = False
        self.thread.join()
