import tkinter
from ..components import labels, buttons, inputs
from models import UnitType


class NpcFrame(tkinter.Frame):
    def __init__(self, parent):
        self.bg = "blue"
        super().__init__(parent, bg=self.bg)
        self.parent = parent

        self.label = labels.FrameLabel(self, "NPC")

        self.player = self.parent.backend.get_player()
        self.npcLevelLabel = labels.InputLabel(self, f"Last NPC Level Defeated: {self.player.npc_level}")

        self.troopSelectorLabel = labels.InputLabel(self, 'Select Troops:')
        self.infantryLabel = labels.InputLabel(self, 'Infantry:')
        self.infantryQuantity = inputs.IntergerOnlyEntry(self, minNumber=1, maxNumber=self.player.units[UnitType.INFANTRY])
        self.cavalryLabel = labels.InputLabel(self, 'Cavalry:')
        self.cavalryQuantity = inputs.IntergerOnlyEntry(self, minNumber=1, maxNumber=self.player.units[UnitType.CAVALRY])
        self.artilleryLabel = labels.InputLabel(self, 'Artillery:')
        self.artilleryQuantity = inputs.IntergerOnlyEntry(self, minNumber=1, maxNumber=self.player.units[UnitType.ARTILLERY])
        self.assassinLabel = labels.InputLabel(self, 'Assassins:')
        self.assassinsQuantity = inputs.IntergerOnlyEntry(self, minNumber=1, maxNumber=self.player.units[UnitType.ASSASSINS])
        self.bowmenLabel = labels.InputLabel(self, 'Bowmen:')
        self.bowmenQuantity = inputs.IntergerOnlyEntry(self, minNumber=1, maxNumber=self.player.units[UnitType.BOWMEN])
        self.bigBowmenLabel = labels.InputLabel(self, 'Big Bowmen:')
        self.bigBowmenQuantity = inputs.IntergerOnlyEntry(self, minNumber=1, maxNumber=self.player.units[UnitType.BIG_BOWMEN])
        self.heavyMenLabel = labels.InputLabel(self, 'Heavy Men:')
        self.heavyMenQuantity = inputs.IntergerOnlyEntry(self, minNumber=1, maxNumber=self.player.units[UnitType.HEAVY_MEN])
        self.kingGuardsLabel = labels.InputLabel(self, 'King Guards:')
        self.kingGuardsQuantity = inputs.IntergerOnlyEntry(self, minNumber=1, maxNumber=self.player.units[UnitType.KINGS_GUARDS])

        self.npcAttackButton = buttons.SubmitButton(self, text='Attack', height=2, width=6)


    def render(self):
        self.label.grid(row=0, column=0)

        self.npcLevelLabel.place(x=300, y=125)

        self.troopSelectorLabel.place(x=300, y=150)
        self.infantryLabel.place(x=200, y=175)
        self.infantryQuantity.place(x=260, y=175)
        self.cavalryLabel.place(x=200, y=200)
        self.cavalryQuantity.place(x=260, y=200)
        self.artilleryLabel.place(x=200, y=225)
        self.artilleryQuantity.place(x=260, y=225)
        self.assassinLabel.place(x=200, y=250)
        self.assassinsQuantity.place(x=260, y=250)
        self.bowmenLabel.place(x=200, y=275)
        self.bowmenQuantity.place(x=260, y=275)
        self.bigBowmenLabel.place(x=185, y=300)
        self.bigBowmenQuantity.place(x=260, y=300)
        self.heavyMenLabel.place(x=190, y=325)
        self.heavyMenQuantity.place(x=260, y=325)
        self.kingGuardsLabel.place(x=185, y=350)
        self.kingGuardsQuantity.place(x=260, y=350)

        self.npcAttackButton.place(x=300, y=400)
