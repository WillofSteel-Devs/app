import tkinter
from ..components import labels, buttons

class NpcFrame(tkinter.Frame):
    
    def __init__(self, parent):
        super().__init__(parent, bg="blue")
        self.parent = parent

        self.label = labels.FrameLabel(self, "NPC")


    def render(self):
        self.label.grid(row=0, column=0)