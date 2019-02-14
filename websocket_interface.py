import time
import websocket


class WebsocketInterface:
    """
    Uses a WebSocketApp with callbacks to process and store server messages
    """

    def __init__(self, url='10.0.1.10:5000', cozmo_message_callback=None):
        self.url = url
        self.ws = None
        self.should_exit = False
        self.last_message_time = time.time()
        self.cozmo_on_message = cozmo_message_callback

    def init(self):
        self.ws = websocket.WebSocketApp(url=self.url, on_open=self.on_open, on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.run_forever(ping_interval=30, ping_timeout=10)

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

    def on_open(self, ws):
        """
        Callback for WebSocketApp that triggers once the socket is open
        :param ws: WebSocket object
        """
        print('-- Listening on socket --')

        if self.url[-1] == '/':
            self.url = self.url[:-1]

    def on_close(self, ws):
        """
        Callback for WebSocketApp that triggers once the socket is closed. Also called after on_error()
        :param ws: WebSocket object
        """
        if self.should_exit:
            print('-- Socket connection closed --')
        else:
            if self.ws.sock:
                self.ws.sock.close()
                self.ws.sock = None
            self.ws = None
            self.init()

    def on_message(self, ws, msg):
        """
        Callback for WebSocketApp that triggers when the web socket receives a message from the server
        :param ws: WebSocket object
        :param msg: message from the remote server
        """
        self.last_message_time = time.time()
        self.cozmo_on_message(WebsocketInterface.parse_message(msg))

    def on_error(self, ws, error):
        """
        Callback for WebSocketApp that triggers when an error occurs with the web socket
        :param ws: WebSocket object
        :param error: error message
        """
        if type(error) not in (KeyboardInterrupt, SystemExit):
            print(error)
        else:
            # Necessary to avoid modifying WebSocketApp code if KeyboardInterrupt is raised
            self.should_exit = True
