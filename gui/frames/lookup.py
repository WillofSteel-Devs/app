import tkinter
from ..components.labels import FrameLabel

class LookupFrame(tkinter.Frame):
    
    def __init__(self, parent):
        super().__init__(parent, width=650, height=600, bg="red")

        self.label = FrameLabel(self, text="Lookup")

    def render(self):
            self.label.grid(row=0, column=0)
            self.configure(width=650, height=600, bg="red")