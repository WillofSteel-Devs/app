import tkinter
from ..components.labels import FrameLabel


class LookupFrame(tkinter.Frame):
    def __init__(self, parent):
        self.bg = "red"
        super().__init__(parent, width=650, height=600, bg=self.bg)
        self.parent = parent

        self.label = FrameLabel(self, text="Lookup")

    def render(self):
        self.label.grid(row=0, column=0)
