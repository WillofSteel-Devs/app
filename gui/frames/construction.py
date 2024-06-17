import tkinter
from ..components import labels, buttons
from backend.api import API


class ConstructionFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="purple")
        self.parent = parent

        self.label = labels.FrameLabel(self, "Construction")

        self.buildingLevels = self.get_building_levels()
        self.displayBuildingLevels = labels.InputLabel(self, str(self.buildingLevels))

        self.farmhouseUpgradeLabel = labels.InputLabel(self, "Farmhouse")
        self.farmhouseUpgradeButton = buttons.SubmitButton(
            self, text="Upgrade", height=1
        )

        self.bakeryUpgradeLabel = labels.InputLabel(self, "Bakery")
        self.bakeryUpgradeButton = buttons.SubmitButton(self, text="Upgrade", height=1)

        self.storehouseUpgradeLabel = labels.InputLabel(self, "Storehouse")
        self.storehouseUpgradeButton = buttons.SubmitButton(
            self, text="Upgrade", height=1
        )

    def get_building_levels(self):
        with open("API_KEY.txt", "r") as f:
            apiKey = f.read()

        backend = API(apiKey)

        return backend.get_buildings()

    def render(self):
        self.label.grid(row=0, column=0)

        self.displayBuildingLevels.place(x=300, y=125)

        self.farmhouseUpgradeLabel.place(x=150, y=200)
        self.farmhouseUpgradeButton.place(x=143, y=225)

        self.bakeryUpgradeLabel.place(x=325, y=200)
        self.bakeryUpgradeButton.place(x=308, y=225)

        self.storehouseUpgradeLabel.place(x=450, y=200)
        self.storehouseUpgradeButton.place(x=443, y=225)
