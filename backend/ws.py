import json
import threading
from websockets.sync import client

from . import events

class Websocket:
    def __init__(self, uri) -> None:
        self.uri = uri
        self.listeners = {}

    def send(self, message: str):
        self._ws.send(json.dumps(message))

    def on(self, event: str, callback):
        if not self.listeners.get(event):
            self.listeners[event] = []
        self.listeners[event].append(callback)

    def remove_listener(self, callback):
        for event in self.listeners:
            if callback in self.listeners[event]:
                self.listeners[event].remove(callback)

    def handle_message(self, message: str):
        print("got", message)
        message = json.loads(message)
        event = message["event"]
        args = message["args"]
        for func in self.listeners.get(event): func(*args)

    def connect(self):
        with client.connect(self.uri) as ws:
            self._ws = ws
            for message in ws:
                self.handle_message(message)

    # Helper functions
    def get_alliance(self, callback):
        self.on(events.AllianceEvent, callback)
        self.send(json.dumps({"event": events.GetAllianceEvent, "args": []}))