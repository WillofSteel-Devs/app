import tkinter
from gui.sidebar import Sidebar
from gui.frames.attack import AttackFrame
from gui.frames.lookup import LookupFrame
from gui.frames.npc import NpcFrame
from gui.frames.recruitment import RecruitmentFrame
from gui.frames.construction import ConstructionFrame
from gui.frames.settings import SettingsFrame

class App(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("My App")
        self.geometry("400x200")
        
        self.sidebar = Sidebar(self)

        self.attack_frame = AttackFrame(self)
        self.lookup_frame = LookupFrame(self)
        self.npc_frame = NpcFrame(self)
        self.recruitment_frame = RecruitmentFrame(self)
        self.construction_frame = ConstructionFrame(self)
        self.settings_frame = SettingsFrame(self)

        self.current_frame = self.lookup_frame

        self.sidebar.grid(row=0, column=0)



    def change_frame(self, frame):
        self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.grid(row=0, column=1)
        self.current_frame.render()


if __name__ == "__main__":
    app = App()
    app.mainloop()