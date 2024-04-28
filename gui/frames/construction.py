import tkinter
from ..components import labels, buttons

class ConstructionFrame(tkinter.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.label = labels.FrameLabel(self, "Construction")

    def render(self):
        self.label.grid(row=0, column=0)