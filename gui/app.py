import tkinter
from gui.attack_frame import AttackFrame
from gui.lookup_frame import LookupFrame
from gui.npc_frame import NpcFrame
from gui.recruitment_frame import RecruitmentFrame
from gui.construction_frame import ConstructionFrame

class App(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("My App")
        self.geometry("400x200")
        self.label = tkinter.Label(self, text="Hello, world!")
        self.label.pack()

        self.attack_frame = AttackFrame(self)
        self.lookup_frame = LookupFrame(self)
        self.npc_frame = NpcFrame(self)
        self.recruitment_frame = RecruitmentFrame(self)
        self.construction_frame = ConstructionFrame(self)

        self.current_frame = self.lookup_frame


    def change_frame(self, frame):
        self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()