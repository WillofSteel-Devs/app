import tkinter

class Sidebarbutton(tkinter.Button):
    
    def __init__(self, parent, text="", command=None):
        super().__init__(parent, text=text, command=command)

class FrameButton(tkinter.Button):
        
    def __init__(self, parent, text="", command=None):
        super().__init__(parent, text=text, command=command)