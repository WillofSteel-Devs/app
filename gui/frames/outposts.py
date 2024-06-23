import tkinter
from ..components import labels, containers, buttons


class OutpostsFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=650, height=600, bg="pink")
        self.parent = parent

        self.outpostsList = self.get_outposts()

        self.label = labels.FrameLabel(self, text="Outposts")

        self.outpost1Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost1ContainerLabel = labels.InputLabel(
            self, text=f'1: {self.outpostsList[0]["name"]}', bg="light grey"
        )
        self.outpost1ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(1),
        )

        self.outpost2Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost2ContainerLabel = labels.InputLabel(
            self, text=f'2: {self.outpostsList[1]["name"]}', bg="light grey"
        )
        self.outpost2ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(2),
        )

        self.outpost3Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost3ContainerLabel = labels.InputLabel(
            self, text=f'3: {self.outpostsList[2]["name"]}', bg="light grey"
        )
        self.outpost3ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(3),
        )

        self.outpost4Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost4ContainerLabel = labels.InputLabel(
            self, text=f'4: {self.outpostsList[3]["name"]}', bg="light grey"
        )
        self.outpost4ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(4),
        )

        self.outpost5Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost5ContainerLabel = labels.InputLabel(
            self, text=f'5: {self.outpostsList[4]["name"]}', bg="light grey"
        )
        self.outpost5ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(5),
        )

        self.outpost6Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost6ContainerLabel = labels.InputLabel(
            self, text=f'6: {self.outpostsList[5]["name"]}', bg="light grey"
        )
        self.outpost6ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(6),
        )

        self.outpost7Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost7ContainerLabel = labels.InputLabel(
            self, text=f'7: {self.outpostsList[6]["name"]}', bg="light grey"
        )
        self.outpost7ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(7),
        )

        self.outpost8Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost8ContainerLabel = labels.InputLabel(
            self, text=f'8: {self.outpostsList[7]["name"]}', bg="light grey"
        )
        self.outpost8ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(8),
        )

        self.outpost9Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost9ContainerLabel = labels.InputLabel(
            self, text=f'9: {self.outpostsList[8]["name"]}', bg="light grey"
        )
        self.outpost9ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(9),
        )

        self.outpost10Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost10ContainerLabel = labels.InputLabel(
            self, text=f'10: {self.outpostsList[9]["name"]}', bg="light grey"
        )
        self.outpost10ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(10),
        )

        self.outpost11Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost11ContainerLabel = labels.InputLabel(
            self, text=f'11: {self.outpostsList[10]["name"]}', bg="light grey"
        )
        self.outpost11ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(11),
        )

        self.outpost12Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost12ContainerLabel = labels.InputLabel(
            self, text=f'12: {self.outpostsList[11]["name"]}', bg="light grey"
        )
        self.outpost12ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(12),
        )

        self.outpost13Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost13ContainerLabel = labels.InputLabel(
            self, text=f'13: {self.outpostsList[12]["name"]}', bg="light grey"
        )
        self.outpost13ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(13),
        )

        self.outpost14Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost14ContainerLabel = labels.InputLabel(
            self, text=f'14: {self.outpostsList[13]["name"]}', bg="light grey"
        )
        self.outpost14ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(14),
        )

        self.outpost15Container = containers.SubContainer(
            self, width=183, height=60, bg="white"
        )
        self.outpost15ContainerLabel = labels.InputLabel(
            self, text=f'15: {self.outpostsList[14]["name"]}', bg="light grey"
        )
        self.outpost15ContainerCapture = buttons.SubmitButton(
            self,
            text="Capture",
            width=10,
            height=1,
            bg="light grey",
            command=self.capture_outpost(15),
        )

    def get_outposts(self):
        response = self.parent.backend.get_outposts()
        return response["outposts"]

    def capture_outpost(self, number):
        # TODO implement capture (requires API support)
        pass

    def render(self):
        self.label.grid(row=0, column=0)

        self.outpost1Container.place(x=30, y=125)
        self.outpost1ContainerLabel.place(x=35, y=130)
        self.outpost1ContainerCapture.place(x=35, y=155)

        self.outpost2Container.place(x=30, y=195)
        self.outpost2ContainerLabel.place(x=35, y=200)
        self.outpost2ContainerCapture.place(x=35, y=225)

        self.outpost3Container.place(x=30, y=265)
        self.outpost3ContainerLabel.place(x=35, y=270)
        self.outpost3ContainerCapture.place(x=35, y=295)

        self.outpost4Container.place(x=30, y=335)
        self.outpost4ContainerLabel.place(x=35, y=340)
        self.outpost4ContainerCapture.place(x=35, y=365)

        self.outpost5Container.place(x=30, y=405)
        self.outpost5ContainerLabel.place(x=35, y=410)
        self.outpost5ContainerCapture.place(x=35, y=435)

        self.outpost6Container.place(x=223, y=125)
        self.outpost6ContainerLabel.place(x=228, y=130)
        self.outpost6ContainerCapture.place(x=228, y=155)

        self.outpost7Container.place(x=223, y=195)
        self.outpost7ContainerLabel.place(x=228, y=200)
        self.outpost7ContainerCapture.place(x=228, y=225)

        self.outpost8Container.place(x=223, y=265)
        self.outpost8ContainerLabel.place(x=228, y=270)
        self.outpost8ContainerCapture.place(x=228, y=295)  #

        self.outpost9Container.place(x=223, y=335)
        self.outpost9ContainerLabel.place(x=228, y=340)
        self.outpost9ContainerCapture.place(x=228, y=365)

        self.outpost10Container.place(x=223, y=405)
        self.outpost10ContainerLabel.place(x=228, y=410)
        self.outpost10ContainerCapture.place(x=228, y=435)

        self.outpost11Container.place(x=416, y=125)
        self.outpost11ContainerLabel.place(x=421, y=130)
        self.outpost11ContainerCapture.place(x=421, y=155)

        self.outpost12Container.place(x=416, y=195)
        self.outpost12ContainerLabel.place(x=421, y=200)
        self.outpost12ContainerCapture.place(x=421, y=225)

        self.outpost13Container.place(x=416, y=265)
        self.outpost13ContainerLabel.place(x=421, y=270)
        self.outpost13ContainerCapture.place(x=421, y=295)

        self.outpost14Container.place(x=416, y=335)
        self.outpost14ContainerLabel.place(x=421, y=340)
        self.outpost14ContainerCapture.place(x=421, y=365)

        self.outpost15Container.place(x=416, y=405)
        self.outpost15ContainerLabel.place(x=421, y=410)
        self.outpost15ContainerCapture.place(x=421, y=435)
