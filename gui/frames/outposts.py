import tkinter
from ..components import labels


class OutpostsFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=650, height=600, bg="pink")
        self.parent = parent

        self.outpostsList = self.get_outposts()
        print(self.outpostsList)

        self.label = labels.FrameLabel(self, text="Outposts")

        self.outpostsTitleLabel = labels.InputLabel(self, text="Outposts", bg="pink")

        self.outpost1Label = labels.InputLabel(
            self, text=f"1: {self.outpostsList[0]['name']}", bg="pink"
        )
        self.outpost2Label = labels.InputLabel(
            self, text=f"2: {self.outpostsList[1]['name']}", bg="pink"
        )
        self.outpost3Label = labels.InputLabel(
            self, text=f"3: {self.outpostsList[2]['name']}", bg="pink"
        )
        self.outpost4Label = labels.InputLabel(
            self, text=f"4: {self.outpostsList[3]['name']}", bg="pink"
        )
        self.outpost5Label = labels.InputLabel(
            self, text=f"5: {self.outpostsList[4]['name']}", bg="pink"
        )
        self.outpost6Label = labels.InputLabel(
            self, text=f"6: {self.outpostsList[5]['name']}", bg="pink"
        )
        self.outpost7Label = labels.InputLabel(
            self, text=f"7: {self.outpostsList[6]['name']}", bg="pink"
        )
        self.outpost8Label = labels.InputLabel(
            self, text=f"8: {self.outpostsList[7]['name']}", bg="pink"
        )
        self.outpost9Label = labels.InputLabel(
            self, text=f"9: {self.outpostsList[8]['name']}", bg="pink"
        )
        self.outpost10Label = labels.InputLabel(
            self, text=f"10: {self.outpostsList[9]['name']}", bg="pink"
        )
        self.outpost11Label = labels.InputLabel(
            self, text=f"11: {self.outpostsList[10]['name']}", bg="pink"
        )
        self.outpost12Label = labels.InputLabel(
            self, text=f"12: {self.outpostsList[11]['name']}", bg="pink"
        )
        self.outpost13Label = labels.InputLabel(
            self, text=f"13: {self.outpostsList[12]['name']}", bg="pink"
        )
        self.outpost14Label = labels.InputLabel(
            self, text=f"14: {self.outpostsList[13]['name']}", bg="pink"
        )
        self.outpost15Label = labels.InputLabel(
            self, text=f"15: {self.outpostsList[14]['name']}", bg="pink"
        )

    def get_outposts(self):
        response = self.parent.backend.get_outposts()
        return response["outposts"]

    def render(self):
        self.label.grid(row=0, column=0)

        self.outpostsTitleLabel.place(x=300, y=75)

        self.outpost1Label.place(x=100, y=125)
        self.outpost2Label.place(x=100, y=150)
        self.outpost3Label.place(x=100, y=175)
        self.outpost4Label.place(x=100, y=200)
        self.outpost5Label.place(x=100, y=225)
        self.outpost6Label.place(x=100, y=250)
        self.outpost7Label.place(x=100, y=275)
        self.outpost8Label.place(x=100, y=300)
        self.outpost9Label.place(x=100, y=325)
        self.outpost10Label.place(x=100, y=350)
        self.outpost11Label.place(x=100, y=375)
        self.outpost12Label.place(x=100, y=400)
        self.outpost13Label.place(x=100, y=425)
        self.outpost14Label.place(x=100, y=450)
        self.outpost15Label.place(x=100, y=475)
