import tkinter
from ..components import labels, buttons


class ConstructionFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="purple")
        self.parent = parent

        self.label = labels.FrameLabel(self, "Construction")

        self.buildingLevels = self.parent.backend.get_buildings()
        self.displayBuildingLevels = labels.InputLabel(self, "Buildings")

        self.farmhouseUpgradeLabel = labels.InputLabel(
            self, f'Farmhouse Level: {self.buildingLevels["farmhouse_level"]}'
        )
        self.farmhouseUpgradeButton = buttons.SubmitButton(
            self, text="Upgrade", height=1, command=self.upgrade_building("farmhouse")
        )

        self.bakeryUpgradeLabel = labels.InputLabel(
            self, f'Bakery Level: {self.buildingLevels["bakery_level"]}'
        )
        self.bakeryUpgradeButton = buttons.SubmitButton(
            self, text="Upgrade", height=1, command=self.upgrade_building("bakery")
        )

        self.storehouseUpgradeLabel = labels.InputLabel(
            self, f'Storehouse Level: {self.buildingLevels["storehouse_level"]}'
        )
        self.storehouseUpgradeButton = buttons.SubmitButton(
            self, text="Upgrade", height=1, command=self.upgrade_building("storehouse")
        )

        self.productionAmount = labels.InputLabel(
            self, f'Food Production: {self.buildingLevels["production"]}'
        )

    def upgrade_building(self, buildingtype):
        self.parent.backend.upgrade_building(buildingtype)

        self.parent.change_frame(
            ConstructionFrame(self.parent)
        )  # TODO instead of initialising a new frame, update the current frame

    def render(self):
        self.label.grid(row=0, column=0)

        self.displayBuildingLevels.place(x=300, y=125)

        self.farmhouseUpgradeLabel.place(x=150, y=200)
        self.farmhouseUpgradeButton.place(x=143, y=225)

        self.bakeryUpgradeLabel.place(x=325, y=200)
        self.bakeryUpgradeButton.place(x=308, y=225)

        self.storehouseUpgradeLabel.place(x=450, y=200)
        self.storehouseUpgradeButton.place(x=443, y=225)

        self.productionAmount.place(x=300, y=275)
