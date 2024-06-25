import tkinter
from ..components import labels


class EmptyFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=650, height=600)
        self.parent = parent

        self.label = labels.FrameLabel(self, "Welcome to the Will of Steel Client!")

    def render(self):
        self.label.place(x=10, y=200)
