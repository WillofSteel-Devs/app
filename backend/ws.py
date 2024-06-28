import json
import socket
import threading

from . import events

class Websocket:
    def __init__(self, uri) -> None:
        self.uri = uri
        self._ws = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listeners = {}

    def send(self, message: str):
        self._ws.send(message.encode())

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
        func = self.listeners.get(event)
        if func: func(args)

    def listen(self):
        while True:
            try:
                message = self._ws.recv(1024).decode()
                print(message)
                if message: self.handle_message(message)
            except Exception as e:
                print(e)
                break

    def connect(self):
        self._ws.connect(self.get_host())
        thread = threading.Thread(target=self.listen)
        thread.start()
        print(f"connected to {self.get_host()}")

    def get_host(self):
        host =  self.uri.split("//")[1].split("/")[0]
        if ":" in host:
            host, port = host.split(":")
            return (host, int(port))
        else:
            return host

    # Helper functions
    def get_alliance(self, callback):
        self.on(events.AllianceEvent, callback)
        self.send(json.dumps({"event": events.GetAllianceEvent, "args": []}))