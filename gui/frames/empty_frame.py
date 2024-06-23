import tkinter


class EmptyFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=650, height=600)
        self.parent = parent

    def render(self):
        pass
