import tkinter


class SidebarLabel(tkinter.Label):
    def __init__(self, parent, text):
        super().__init__(
            parent,
            text=text,
            width=151,
            height=5,
            bg="#413E36",
            foreground="white",
            font=("Helvetica", 10, "bold"),
        )


class FrameLabel(tkinter.Label):
    def __init__(self, parent, text):
        super().__init__(parent, text=text, width=151, height=3)


class InputLabel(tkinter.Label):
    def __init__(self, parent, text):
        super().__init__(parent, text=text, bg="#ffffff")
