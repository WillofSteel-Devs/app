import tkinter

from backend.api import API
from gui.sidebar import Sidebar
from gui.frames.attack import AttackFrame
from gui.frames.lookup import LookupFrame
from gui.frames.npc import NpcFrame
from gui.frames.recruitment import RecruitmentFrame
from gui.frames.construction import ConstructionFrame
from gui.frames.alliance import AllianceFrame
from gui.frames.settings import SettingsFrame
from gui.frames.api_key import APIKeyFrame


class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Will of Steel")
        self.geometry("800x600")
        self.resizable(False, False)

        # init sidebar
        self.sidebar = Sidebar(self)

        self.api_key = self.verify_api()
        if not self.api_key:
            self.api_key_frame = APIKeyFrame(self)
            self.current_frame = self.api_key_frame
            self.current_frame.place(x=0, y=0, height=600, width=800)
            self.current_frame.render()
        else:
            self.sidebar.place(x=0, y=0, height=600, width=150)
            self.current_frame = LookupFrame(self)
            self.build_main_frame()

        # init frames
        self.attack_frame = AttackFrame(self)
        self.lookup_frame = LookupFrame(self)
        self.npc_frame = NpcFrame(self)
        self.recruitment_frame = RecruitmentFrame(self)
        self.construction_frame = ConstructionFrame(self)
        self.alliance_frame = AllianceFrame(self)
        self.settings_frame = SettingsFrame(self)
        self.api_key_frame = APIKeyFrame(self)

    def build_main_frame(self):
        if self.current_frame:
            self.current_frame.place_forget()
        self.sidebar.place(x=0, y=0, height=600, width=150)
        self.current_frame = LookupFrame(self)
        self.current_frame.place(x=150, y=0, height=600, width=650)
        self.current_frame.render()

    def change_frame(self, frame):
        self.current_frame.place_forget()
        self.current_frame = frame
        self.current_frame.place(x=150, y=0, height=600, width=650)
        self.current_frame.render()

    def verify_api(self) -> str | bool:
        try:
            with open("API_KEY.txt", "r") as f:
                api_key = f.read()
                self.backend = API(api_key)
                valid = self.backend.verify_key()
                return api_key if valid else False
        except FileNotFoundError:
            return False


if __name__ == "__main__":
    app = App()
    app.mainloop()
