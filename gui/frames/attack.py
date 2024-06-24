import tkinter
from ..components import labels, inputs, buttons


class AttackFrame(tkinter.Frame):
    def __init__(self, parent):
        self.bg = "orange"
        super().__init__(parent, bg=self.bg)
        self.parent = parent

        self.label = labels.FrameLabel(self, "Attack")

        self.targetLabel = labels.InputLabel(self, "Enter Target Discord ID")
        self.targetInput = inputs.TextInput(self)
        self.targetSubmit = buttons.SubmitButton(self, text="Submit")

    def render(self):
        self.label.grid(row=0, column=0)
