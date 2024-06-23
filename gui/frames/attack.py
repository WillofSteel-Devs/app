import tkinter
from ..components import labels


class AttackFrame(tkinter.Frame):
    def __init__(self, parent):
        self.bg = "orange"
        super().__init__(parent, bg=self.bg)
        self.parent = parent

        self.label = labels.FrameLabel(self, "Attack")

    def render(self):
        self.label.grid(row=0, column=0)
