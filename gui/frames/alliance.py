# pyright: reportOptionalMemberAccess=false
# TODO for neil fix later

import tkinter
from ..components import labels, inputs, buttons


class AllianceFrame(tkinter.Frame):
    def __init__(self, parent):
        self.bg = "orange"
        super().__init__(parent, width=650, height=600, bg=self.bg)
        self.parent = parent

        self.allianceData = self.parent.backend.get_alliance()
        if self.allianceData is None:
            self.parent.sidebar.disable_option("alliance")
            return

        self.label = labels.FrameLabel(self, text="Alliance")

        # alliance info
        self.allianceNameLabel = labels.InputLabel(
            self, f"Alliance: {self.allianceData.name}"
        )
        self.allianceOwnerLabel = labels.InputLabel(
            self, f"Owner (Discord ID): {self.allianceData.owner}"
        )
        self.allianceUserLimitLabel = labels.InputLabel(
            self, f'User Limit: {"{:,}".format(self.allianceData.user_limit)}'
        )  # includes formating number with commas
        self.allianceBankBalanceLabel = labels.InputLabel(
            self, f'Bank Balance: {"{:,}".format(self.allianceData.bank)}'
        )  # includes formating number with commas
        self.allianceCreationTimestamp = labels.InputLabel(
            self, f"Alliance Creation Timestamp: {self.allianceData.created_at}"
        )

        # update section
        self.allianceUpdateLabel = labels.InputLabel(self, "Update Alliance Info")

        self.allianceNameUpdateLabel = labels.InputLabel(self, "Update Name:")
        self.allianceNameUpdateField = inputs.TextInput(self)
        self.allianceNameUpdateSubmit = buttons.SubmitButton(
            self, text="Submit", width=10, height=1, command=self.update_alliance_name
        )

        self.allianceUserLimitUpdateLabel = labels.InputLabel(
            self, "Update User Limit:"
        )
        self.allianceUserLimitUpdateField = inputs.IntergerOnlyEntry(self)
        self.allianceUserLimitUpdateSubmit = buttons.SubmitButton(
            self,
            text="Submit",
            width=10,
            height=1,
            command=self.update_alliance_user_limit,
        )

    def update_data(self):
        self.allianceData = self.parent.backend.get_alliance()
        self.allianceNameLabel.config(text=f"Alliance: {self.allianceData.name}")
        self.allianceOwnerLabel.config(text=f"Owner (Discord ID): {self.allianceData.owner}")
        self.allianceUserLimitLabel.config(text=f'User Limit: {"{:,}".format(self.allianceData.user_limit)}')
        self.allianceBankBalanceLabel.config(text=f'Bank Balance: {"{:,}".format(self.allianceData.bank)}')
        self.allianceCreationTimestamp.config(text=f"Alliance Creation Timestamp: {self.allianceData.created_at}")

    def update_alliance_name(self):
        name = self.allianceNameUpdateField.get()

        self.parent.backend.update_alliance_name(name)

        self.update_data()

    def update_alliance_user_limit(self):
        user_limit = self.allianceUserLimitUpdateField.get()

        self.parent.backend.update_alliance_user_limit(int(user_limit))

        self.update_data()

    def render(self):
        self.label.grid(row=0, column=0)

        # render alliance info
        self.allianceNameLabel.place(x=245, y=100)
        self.allianceOwnerLabel.place(x=245, y=125)
        self.allianceUserLimitLabel.place(x=310, y=150)
        self.allianceBankBalanceLabel.place(x=280, y=175)

        # render alliance updating
        self.allianceUpdateLabel.place(x=295, y=225)

        self.allianceNameUpdateLabel.place(x=100, y=250)
        self.allianceNameUpdateField.place(x=190, y=250)
        self.allianceNameUpdateSubmit.place(x=500, y=247)

        self.allianceUserLimitUpdateLabel.place(x=80, y=275)
        self.allianceUserLimitUpdateField.place(x=190, y=275)
        self.allianceUserLimitUpdateSubmit.place(x=500, y=272)
