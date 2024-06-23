import tkinter
from ..components import buttons, labels

class ConfirmPopup(tkinter.Toplevel):
    def __init__(self, parent, bg=None, confirmLabelText='Confirm?', confirmLabelBg=None, confirmButtonBg="white", cancelButtonBg="white"):
        if bg is None:
            bg = parent.bg
        if confirmLabelBg is None:
            confirmLabelBg = bg
        super().__init__(parent, width=300, height=100, bg=bg)

        self.transient(parent)
        self.grab_set()
        self.attributes("-topmost", True)

        self.confirmLabel = labels.InputLabel(self, text=confirmLabelText, bg=confirmLabelBg)

        self.confirmButton = buttons.SubmitButton(self, text='Confirm', bg=confirmButtonBg, height=1, width=7, command=self.confirm)
        self.cancelButton = buttons.SubmitButton(self, text='Cancel', bg=cancelButtonBg, height=1, width=7, command=self.cancel)

        self.confirmLabel.place(x=10, y=25)
        self.confirmButton.place(x=10, y=60)
        self.cancelButton.place(x=80, y=60)

    def confirm(self):
        self.result = "confirmed"
        self.destroy()
    def cancel(self):
        self.result = "cancelled"
        self.destroy()