import tkinter
from ..components import buttons, labels, inputs
from models import UnitType


class ConfirmPopup(tkinter.Toplevel):
    def __init__(
        self,
        parent,
        bg=None,
        confirmLabelText="Confirm?",
        confirmLabelBg=None,
        confirmButtonBg="white",
        cancelButtonBg="white",
    ):
        if bg is None:
            bg = parent.bg
        if confirmLabelBg is None:
            confirmLabelBg = bg
        super().__init__(parent, width=300, height=100, bg=bg)

        self.transient(parent)
        self.grab_set()
        self.attributes("-topmost", True)

        self.confirmLabel = labels.InputLabel(
            self, text=confirmLabelText, bg=confirmLabelBg
        )

        self.confirmButton = buttons.SubmitButton(
            self,
            text="Confirm",
            bg=confirmButtonBg,
            height=1,
            width=7,
            command=self.confirm,
        )
        self.cancelButton = buttons.SubmitButton(
            self,
            text="Cancel",
            bg=cancelButtonBg,
            height=1,
            width=7,
            command=self.cancel,
        )

        self.confirmLabel.place(x=10, y=25)
        self.confirmButton.place(x=10, y=60)
        self.cancelButton.place(x=80, y=60)

    def confirm(self):
        self.result = "confirmed"
        self.destroy()

    def cancel(self):
        self.result = "cancelled"
        self.destroy()


class SelectArmy(tkinter.Toplevel):
    def __init__(self, parent, bg=None):
        self.parent = parent
        if bg is None:
            bg = parent.bg
        self.bg = bg
        super().__init__(parent, width=300, height=400, bg=bg)

        self.transient(parent)
        self.grab_set()
        self.attributes("-topmost", True)

        self.select_label = labels.InputLabel(self, text="Select Army", bg=bg)

        self.player = self.parent.parent.backend.get_player()
        infantry = self.player.units[UnitType.INFANTRY]
        cavalry = self.player.units[UnitType.CAVALRY]
        artillery = self.player.units[UnitType.ARTILLERY]
        assassins = self.player.units[UnitType.ASSASSINS]
        bowmen = self.player.units[UnitType.BOWMEN]
        big_bowmen = self.player.units[UnitType.BIG_BOWMEN]
        heavy_men = self.player.units[UnitType.HEAVY_MEN]
        king_guards = self.player.units[UnitType.KINGS_GUARDS]

        self.infantryLabel = labels.InputLabel(
            self, f"Infantry ({'{:,}'.format(infantry)}):"
        )
        self.cavalryLabel = labels.InputLabel(
            self, f"Cavalry ({'{:,}'.format(cavalry)}):"
        )
        self.artilleryLabel = labels.InputLabel(
            self, f"Artillery ({'{:,}'.format(artillery)}):"
        )
        self.assassinLabel = labels.InputLabel(
            self, f"Assassins ({'{:,}'.format(assassins)}):"
        )
        self.bowmenLabel = labels.InputLabel(self, f"Bowmen ({'{:,}'.format(bowmen)}):")
        self.bigBowmenLabel = labels.InputLabel(
            self, f"Big Bowmen ({'{:,}'.format(big_bowmen)}):"
        )
        self.heavyMenLabel = labels.InputLabel(
            self, f"Heavy Men ({'{:,}'.format(heavy_men)}):"
        )
        self.kingGuardsLabel = labels.InputLabel(
            self, f"King Guards ({'{:,}'.format(king_guards)}):"
        )

        self.infantryQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=infantry, width=22
        )
        self.cavalryQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=cavalry, width=22
        )
        self.artilleryQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=artillery, width=22
        )
        self.assassinsQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=assassins, width=22
        )
        self.bowmenQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=bowmen, width=22
        )
        self.bigBowmenQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=big_bowmen, width=22
        )
        self.heavyMenQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=heavy_men, width=22
        )
        self.kingGuardsQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=king_guards, width=22
        )

        self.submit_button = buttons.SubmitButton(
            self, text="Capture", bg=bg, height=1, width=7, command=self.submit
        )

        # render
        self.select_label.place(x=120, y=25)

        self.infantryLabel.place(x=10, y=75)
        self.cavalryLabel.place(x=10, y=100)
        self.artilleryLabel.place(x=10, y=125)
        self.assassinLabel.place(x=10, y=150)
        self.bowmenLabel.place(x=10, y=175)
        self.bigBowmenLabel.place(x=10, y=200)
        self.heavyMenLabel.place(x=10, y=225)
        self.kingGuardsLabel.place(x=10, y=250)
        self.infantryQuantity.place(x=156, y=75)
        self.cavalryQuantity.place(x=156, y=100)
        self.artilleryQuantity.place(x=156, y=125)
        self.assassinsQuantity.place(x=156, y=150)
        self.bowmenQuantity.place(x=156, y=175)
        self.bigBowmenQuantity.place(x=156, y=200)
        self.heavyMenQuantity.place(x=156, y=225)
        self.kingGuardsQuantity.place(x=156, y=250)

        self.submit_button.place(x=130, y=300)

    def submit(self):
        self.result = {
            "troops": {
                "infantry": int(self.infantryQuantity.get()),
                "cavalry": int(self.cavalryQuantity.get()),
                "artillery": int(self.artilleryQuantity.get()),
                "assassins": int(self.infantryQuantity.get()),
                "bowmen": int(self.assassinsQuantity.get()),
                "big_bowmen": int(self.bigBowmenQuantity.get()),
                "heavy_men": int(self.heavyMenQuantity.get()),
                "king_guards": int(self.kingGuardsQuantity.get()),
            }
        }
        self.destroy()
