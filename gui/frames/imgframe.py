import tkinter
from ..components import labels
import os
import sys

def resource_path(*args) -> str:
    try:
        base_path = sys._MEIPASS2  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, *args)

class ImageFrame(tkinter.Frame):
    def __init__(self, parent):
        self.bg = "black"
        super().__init__(parent)
        self.parent = parent

        self.resource_bar = tkinter.PhotoImage(file=resource_path("assets", "img", "resource_bar.png"))
        self.resource_bar_label = tkinter.Label(self, image=self.resource_bar)

    def render(self):
        self.resource_bar_label.place(x=0, y=0, height=600, width=1500)
        print("rendering image frame")