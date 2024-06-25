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


class FullWidthLabel(tkinter.Label):
    def __init__(self, parent, text):
        super().__init__(parent, text=text, width=50, height=2, font=("Helvetica", 20))


class FrameLabel(tkinter.Label):
    def __init__(self, parent, text):
        super().__init__(parent, text=text, width=42, height=2, font=("Helvetica", 20))


class InputLabel(tkinter.Label):
    def __init__(self, parent, text, bg=None, *args, **kwargs):
        if bg is None:
            bg = parent.bg
        super().__init__(parent, text=text, bg=bg, *args, **kwargs)


class PopUpLabel(tkinter.Label):
    def __init__(
        self,
        parent,
        text: str,
        *,
        bg: str = "green",
        fg: str = "black",
        wraplength: int = 100,
        **kwargs,
    ):
        super().__init__(
            parent, text=text, bg=bg, fg=fg, wraplength=wraplength, **kwargs
        )
