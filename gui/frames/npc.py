import tkinter
from ..components import labels, buttons, inputs
from models import UnitType, NPCResult


class NPCResultFrame(tkinter.Frame):
    def __init__(self, parent, result: NPCResult):
        self.bg = "orange"
        super().__init__(parent, bg=self.bg)
        self.parent = parent

        self.label = labels.FrameLabel(self, "NPC Result")

        self.result = result

        self.resultLabel = labels.InputLabel(self, f"Won: {self.result.won}")
        # display lost troops & gained resources etc

    def render(self):
        self.label.grid(row=0, column=0)

        self.resultLabel.place(x=300, y=150)


class NpcFrame(tkinter.Frame):
    def __init__(self, parent):
        self.bg = "orange"
        super().__init__(parent, bg=self.bg)
        self.parent = parent

        self.label = labels.FrameLabel(self, "NPC")

        self.player = self.parent.backend.get_player()
        infantry = self.player.units[UnitType.INFANTRY]
        cavalry = self.player.units[UnitType.CAVALRY]
        artillery = self.player.units[UnitType.ARTILLERY]
        assassins = self.player.units[UnitType.ASSASSINS]
        bowmen = self.player.units[UnitType.BOWMEN]
        big_bowmen = self.player.units[UnitType.BIG_BOWMEN]
        heavy_men = self.player.units[UnitType.HEAVY_MEN]
        king_guards = self.player.units[UnitType.KINGS_GUARDS]
        self.npcLevelLabel = labels.InputLabel(
            self, f"Last NPC Level Defeated: {self.player.npc_level}"
        )

        self.troopSelectorLabel = labels.InputLabel(self, "Select Troops:")
        self.infantryLabel = labels.InputLabel(self, f"Infantry ({infantry}):")
        self.cavalryLabel = labels.InputLabel(self, f"Cavalry ({cavalry}):")
        self.artilleryLabel = labels.InputLabel(self, f"Artillery ({artillery}):")
        self.assassinLabel = labels.InputLabel(self, f"Assassins ({assassins}):")
        self.bowmenLabel = labels.InputLabel(self, f"Bowmen ({bowmen}):")
        self.bigBowmenLabel = labels.InputLabel(self, f"Big Bowmen ({big_bowmen}):")
        self.heavyMenLabel = labels.InputLabel(self, f"Heavy Men ({heavy_men}):")
        self.kingGuardsLabel = labels.InputLabel(self, f"King Guards ({king_guards}):")

        self.infantryQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=infantry
        )
        self.cavalryQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=cavalry
        )
        self.artilleryQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=artillery
        )
        self.assassinsQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=assassins
        )
        self.bowmenQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=bowmen
        )
        self.bigBowmenQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=big_bowmen
        )
        self.heavyMenQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=heavy_men
        )
        self.kingGuardsQuantity = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=king_guards
        )

        self.npcAttackButton = buttons.SubmitButton(
            self, text="Attack", height=2, width=6, command=self.attack_npc
        )

    def attack_npc(self):
        infantry = self.infantryQuantity.get()
        cavalry = self.cavalryQuantity.get()
        artillery = self.artilleryQuantity.get()
        assassins = self.assassinsQuantity.get()
        bowmen = self.bowmenQuantity.get()
        big_bowmen = self.bigBowmenQuantity.get()
        heavy_men = self.heavyMenQuantity.get()
        king_guards = self.kingGuardsQuantity.get()
        troops = {
            "infantry": int(infantry) if infantry else 0,
            "cavalry": int(cavalry) if cavalry else 0,
            "artillery": int(artillery) if artillery else 0,
            "assassins": int(assassins) if assassins else 0,
            "bowmen": int(bowmen) if bowmen else 0,
            "big_bowmen": int(big_bowmen) if big_bowmen else 0,
            "heavy_men": int(heavy_men) if heavy_men else 0,
            "king_guards": int(king_guards) if king_guards else 0,
        }
        result = self.parent.backend.attack_npc(troops)
        npc_result_frame = NPCResultFrame(self.parent, result)
        self.parent.change_frame(npc_result_frame)

    def render(self):
        self.label.grid(row=0, column=0)

        self.npcLevelLabel.place(x=300, y=125)

        self.troopSelectorLabel.place(x=300, y=150)
        self.infantryLabel.place(x=193, y=175)
        self.cavalryLabel.place(x=195, y=200)
        self.artilleryLabel.place(x=193, y=225)
        self.assassinLabel.place(x=185, y=250)
        self.bowmenLabel.place(x=187, y=275)
        self.bigBowmenLabel.place(x=167, y=300)
        self.heavyMenLabel.place(x=174, y=325)
        self.kingGuardsLabel.place(x=170, y=350)

        self.infantryQuantity.place(x=260, y=175)
        self.cavalryQuantity.place(x=260, y=200)
        self.artilleryQuantity.place(x=260, y=225)
        self.assassinsQuantity.place(x=260, y=250)
        self.bowmenQuantity.place(x=260, y=275)
        self.bigBowmenQuantity.place(x=260, y=300)
        self.heavyMenQuantity.place(x=260, y=325)
        self.kingGuardsQuantity.place(x=260, y=350)

        self.npcAttackButton.place(x=300, y=400)
