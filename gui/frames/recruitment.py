import tkinter
from ..components import labels, dropdowns, inputs, buttons
from backend.api import API


class RecruitmentFrame(tkinter.Frame):
    def __init__(self, parent):
        self.bg = "green"
        super().__init__(parent, bg=self.bg)
        self.parent = parent

        self.label = labels.FrameLabel(self, "Recruitment")

        self.troopselectorlabel = labels.InputLabel(self, "Select Troop Type")
        self.troopselector = dropdowns.Dropdown(
            self,
            options=[
                "Infantry",
                "Cavalry",
                "Artillery",
                "Assassins",
                "Bowmen",
                "Big Bowmen",
                "Heavy Men",
                "King Guards",
            ],
        )
        self.troopquantityselectorlabel = labels.InputLabel(self, "Select Amount")
        self.troopquantityselector = inputs.IntergerOnlyEntry(
            self, minNumber=1, maxNumber=1000
        )
        self.recruitsubmit = buttons.SubmitButton(
            self, text="Submit", width=10, height=1, command=self.submit_recruit
        )

    def submit_recruit(self):
        with open("API_KEY.txt", "r") as f:
            apiKey = f.read()

        backend = API(apiKey)
        result = backend.recruit_troop(
            self.troopselector.get_selection().get(),
            self.troopquantityselector.get(),
            "gold",
        )

        if result.status_code != 200:
            self.show_error(result.json()["message"])

    def show_error(self, error: str):
        label = labels.PopUpLabel(
            self, error, bg="red", fg="white", relief=tkinter.SUNKEN
        )
        label.place(x=200, y=50, anchor="center")

    def render(self):
        self.label.grid(row=0, column=0)

        self.troopselectorlabel.place(x=293, y=100)
        self.troopselector.place(x=300, y=125)
        self.troopquantityselectorlabel.place(x=300, y=160)
        self.troopquantityselector.place(x=282, y=185)
        self.recruitsubmit.place(x=300, y=210)
