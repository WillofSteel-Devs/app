import tkinter
from ..components import labels, dropdowns, inputs, buttons


class RecruitmentFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="green")
        self.parent = parent

        self.label = labels.FrameLabel(self, "Recruitment")
        
        self.troopselectorlabel = labels.InputLabel(self, "Select Troop Type")
        self.troopselector = dropdowns.Dropdown(self, options=['Infantry', 'Cavalry', 'Artillery', 'Assassin', 'Bowmen', 'Big Bowmen', 'Heavy Men', 'King Guards'])
        self.troopquantityselectorlabel = labels.InputLabel(self, "Select Amount")
        self.troopquantityselector = inputs.IntergerOnlyEntry(self, minNumber=1, maxNumber=1000)
        self.recruitsubmit = buttons.SubmitButton(self, text='Submit', width=10, hight=1)

    def render(self):
        self.label.grid(row=0, column=0)
        
        self.troopselectorlabel.place(x=293, y=100)
        self.troopselector.place(x=300, y=125)
        self.troopquantityselectorlabel.place(x=300, y=160)
        self.troopquantityselector.place(x=282, y=185)
        self.recruitsubmit.place(x=300, y=210)
