import tkinter
import sys
import os
from ..components import labels, inputs, buttons
from backend.api import API


def resource_path(*args) -> str:
    try:
        base_path = sys._MEIPASS2  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, *args)


class APIKeyFrame(tkinter.Frame):
    def __init__(self, parent, sidebar=False):
        self.sidebar = sidebar

        self.bg = "yellow"
        super().__init__(parent, bg=self.bg)
        self.parent = parent

        if self.sidebar:
            self.label = labels.FrameLabel(self, "API Key")
        else:
            self.label = labels.FullWidthLabel(self, "API Key")

        self.apikeyentrylabel = labels.InputLabel(self, "Enter API Key:")
        self.apikeyentry = inputs.TextInput(self)

        self.apikeysubmit = buttons.SubmitButton(
            self, text="Submit", width=10, height=1, command=self.submit_api_key
        )

    def submit_api_key(self):
        try:
            api_key = self.apikeyentry.get()
            backend = API(api_key)
            valid = backend.verify_key()
            if valid:
                with open(resource_path("API_KEY.txt"), "w") as f:
                    f.write(self.apikeyentry.get())
                self.parent.backend = backend
                self.parent.build_app(True)
            else:
                self.apikeyentry.delete(0, "end")
                self.apikeyentry.insert(0, "Invalid API Key")
        except Exception as e:
            self.show_error(str(e))

    def show_error(self, error: str):
        label = labels.PopUpLabel(
            self, error, bg="red", fg="white", relief=tkinter.SUNKEN
        )
        label.place(x=200, y=50, anchor="center")

    def render(self):
        self.label.grid(row=0, column=0)

        # API key feild stuff
        self.apikeyentrylabel.place(x=300, y=100)
        self.apikeyentry.place(x=190, y=125)
        self.apikeysubmit.place(x=300, y=150)
