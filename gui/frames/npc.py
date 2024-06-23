import tkinter
from ..components import labels


class NpcFrame(tkinter.Frame):
    def __init__(self, parent):
        self.bg = "blue"
        super().__init__(parent, bg=self.bg)
        self.parent = parent

        self.label = labels.FrameLabel(self, "NPC")

    def render(self):
        self.label.grid(row=0, column=0)
