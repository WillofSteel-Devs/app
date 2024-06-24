# pyright: reportArgumentType=false
# Argument of type "Unknown | None" cannot be assigned to parameter "command" of type "_ButtonCommand" in function "__init__"
# there needs to be a default for both of these buttons
import tkinter


class Sidebarbutton(tkinter.Button):
    def __init__(self, parent, text="", command=None):
        super().__init__(
            parent, text=text, command=command, width=151, height=3, bg="#6E6A5E"
        )


class FrameButton(tkinter.Button):
    def __init__(self, parent, text="", command=None):
        super().__init__(parent, text=text, command=command, width=151, height=3)


class SubmitButton(tkinter.Button):
    def __init__(self, parent, text="", command=None, width=10, height=5, bg=None):
        if bg is None:
            bg = parent.bg
        super().__init__(
            parent, text=text, command=command, width=width, height=height, bg=bg
        )
