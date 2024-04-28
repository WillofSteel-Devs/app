import tkinter

class LookupFrame(tkinter.Frame):
    
        def __init__(self, parent):
            super().__init__(parent)

            self.label = tkinter.Label(self, text="Lookup")

        def render(self):
              self.label.grid(row=0, column=0)