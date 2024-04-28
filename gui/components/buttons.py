import tkinter

class Sidebarbutton(tkinter.Button):
    
    def __init__(self, parent, text):
        super().__init__(parent, text=text)

class FrameButton(tkinter.Button):
        
    def __init__(self, parent, text):
        super().__init__(parent, text=text)