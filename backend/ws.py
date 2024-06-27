import json
from websockets.sync.client import connect


class Websocket:
    def __init__(self, uri: str) -> None:
        self.uri = uri
        self.listeners = {}

    def send(self, message: str):
        self._ws.send(message)

    def on(self, event: str, callback):
        self.listeners[event] = callback

    def remove_listener(self, event: str):
        del self.listeners[event]

    def handle_message(self, message: str):
        message = json.loads(message)
        event = message["event"]
        args = message["args"]
        func = self.listeners.get(event)
        if func: func(args)

    def connect(self):
        with connect(self.uri) as ws:
            self._ws = ws
            while True:
                message = ws.recv()
                self.handle_message(message)