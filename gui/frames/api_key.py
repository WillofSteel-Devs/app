import tkinter
from ..components import labels, inputs, buttons


class APIKeyFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="yellow")
        self.parent = parent

        self.label = labels.FrameLabel(self, "API Key")

        self.apikeyentrylabel = labels.InputLabel(self, "Enter API Key:")
        self.apikeyentry = inputs.TextInput(self)
        self.apikeysubmit = buttons.SubmitButton(self, text="Submit", width=10, hight=1)

    def render(self):
        self.label.grid(row=0, column=0)

        # API key feild stuff
        self.apikeyentrylabel.place(x=300, y=100)
        self.apikeyentry.place(x=190, y=125)
        self.apikeysubmit.place(x=300, y=150)
