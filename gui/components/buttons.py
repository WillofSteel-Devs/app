import tkinter

class Sidebarbutton(tkinter.Button):
    
    def __init__(self, parent, text="", command=None):
        super().__init__(parent, text=text, command=command, width=151, height=3, bg="#6E6A5E")

class FrameButton(tkinter.Button):
        
    def __init__(self, parent, text="", command=None):
        super().__init__(parent, text=text, command=command, width=151, height=3)