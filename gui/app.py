import tkinter
from attack_frame import AttackFrame
from lookup_frame import LookupFrame
from npc_frame import NpcFrame
from recruitment_frame import RecruitmentFrame
from construction_frame import ConstructionFrame

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


    def change_frame(self, frame):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()