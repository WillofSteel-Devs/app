import tkinter
from gui.sidebar import Sidebar
from gui.frames.attack import AttackFrame
from gui.frames.lookup import LookupFrame
from gui.frames.npc import NpcFrame
from gui.frames.recruitment import RecruitmentFrame
from gui.frames.construction import ConstructionFrame
from gui.frames.settings import SettingsFrame
from gui.frames.api_key_submit import APIKeyFrame


class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Will of Steel")
        self.geometry("800x600")
        self.resizable(False, False)

        self.sidebar = Sidebar(self)

        self.attack_frame = AttackFrame(self)
        self.lookup_frame = LookupFrame(self)
        self.npc_frame = NpcFrame(self)
        self.recruitment_frame = RecruitmentFrame(self)
        self.construction_frame = ConstructionFrame(self)
        self.settings_frame = SettingsFrame(self)
        self.api_key_frame = APIKeyFrame(self)

        self.current_frame = self.api_key_frame
        self.change_frame(self.current_frame)

        self.sidebar.place(x=0, y=0, height=600, width=150)

    def change_frame(self, frame):
        self.current_frame.place_forget()
        self.current_frame = frame
        self.current_frame.place(x=150, y=0, height=600, width=650)
        self.current_frame.render()


if __name__ == "__main__":
    app = App()
    app.mainloop()
