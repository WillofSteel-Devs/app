import tkinter
import os
import sys
import asyncio
import threading
import atexit

from backend.api import API
from backend.ws import Websocket
from gui.sidebar import Sidebar
from gui.frames.attack import AttackFrame
from gui.frames.lookup import LookupFrame
from gui.frames.npc import NpcFrame
from gui.frames.recruitment import RecruitmentFrame
from gui.frames.construction import ConstructionFrame
from gui.frames.alliance import AllianceFrame
from gui.frames.settings import SettingsFrame
from gui.frames.api_key import APIKeyFrame
from gui.frames.empty_frame import EmptyFrame
from gui.frames.outposts import OutpostsFrame
from gui.frames.market import MarketFrame


def resource_path(*args) -> str:
    try:
        base_path = sys._MEIPASS2  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, *args)


class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Will of Steel")
        self.geometry("800x600")
        self.resizable(False, False)
        self.resource_path = resource_path
        icon_path = resource_path("assets", "img", "logo.png")
        photo_image = tkinter.PhotoImage(file=icon_path)
        self.iconphoto(True, photo_image)

        # self._ws = Websocket("wss://api.willofsteel.me/ws")
        self._ws = Websocket("ws://localhost:8765/")
        self._ws.connect()

        self.api_key = self.verify_api()
        if not self.api_key:
            self.api_key_frame = APIKeyFrame(self)
            self.current_frame = self.api_key_frame
            self.current_frame.place(x=0, y=0, height=600, width=800)
            self.current_frame.render()
        else:
            self.build_app()

    def build_app(self, destroy: bool = False) -> None:
        if destroy:
            self.current_frame.place_forget()

        self.sidebar = Sidebar(self)
        self.sidebar.place(x=0, y=0, height=600, width=150)
        # self.attack_frame = AttackFrame(self)
        # self.lookup_frame = LookupFrame(self)
        # self.npc_frame = NpcFrame(self)
        # self.recruitment_frame = RecruitmentFrame(self)
        # self.construction_frame = ConstructionFrame(self)
        self.alliance_frame = AllianceFrame(self)
        # self.settings_frame = SettingsFrame(self)
        # self.api_key_frame = APIKeyFrame(self, sidebar=True)
        # self.outposts_frame = OutpostsFrame(self)
        # self.market_frame = MarketFrame(self)
        self.current_frame = EmptyFrame(self)
        self.current_frame.place(x=150, y=0, height=600, width=650)
        self.current_frame.render()

    def change_frame(self, frame):
        self.current_frame.place_forget()
        self.current_frame = frame
        self.current_frame.place(x=150, y=0, height=600, width=650)
        self.current_frame.render()

    def verify_api(self) -> str | bool:
        try:
            with open(resource_path("API_KEY.txt"), "r") as f:
                api_key = f.read()
                self.backend = API(api_key)
                valid = self.backend.verify_key()
                if valid:
                    return api_key
                else:
                    return False
        except FileNotFoundError:
            return False


if __name__ == "__main__":
    app = App()
    app.mainloop()
