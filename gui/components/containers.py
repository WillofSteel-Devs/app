import tkinter

class SubContainer(tkinter.Frame):
    def __init__(self, parent, width=100, height=50, bg=None):
        if bg is None:
            bg = parent.bg
        super().__init__(parent, width=width, height=height, bg=bg)