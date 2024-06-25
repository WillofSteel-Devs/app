import tkinter
from ..components import labels, containers, buttons, popups


class OutpostsFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=650, height=600, bg="pink")
        self.parent = parent

        self.outpostsList = self.get_outposts()
        self.label = labels.FrameLabel(self, text="Outposts")
        self.label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        self.create_outpost_containers()

    def get_outposts(self):
        response = self.parent.backend.get_outposts()
        return response["outposts"]

    def capture_outpost(self, number):
        self.popup = popups.ConfirmPopup(
            self, bg="lightblue", confirmLabelText="Confirm Capture?"
        )

        self.wait_window(self.popup)
        if self.popup.result == "confirmed":
            print(
                f"Capture of Outpost {number} Confirmed"
            )  # TODO implement capture (requires API support)

    def create_outpost_containers(self):
        container_width = 183
        container_height = 60
        container_padx = 5

        for i, outpost in enumerate(self.outpostsList):
            x = 30 + (i % 3) * (container_width + container_padx)
            y = 100 + (i // 3) * (container_height + 10)

            container = containers.SubContainer(
                self, width=container_width, height=container_height, bg="white"
            )
            label = labels.InputLabel(
                container, text=f'{i + 1}: {outpost["name"]}', bg="light grey"
            )
            button = buttons.SubmitButton(
                container,
                text="Capture",
                width=10,
                height=1,
                bg="light grey",
                command=lambda n=i + 1: self.capture_outpost(n),
            )

            container.place(x=x, y=y)
            label.place(x=5, y=5)
            button.place(x=5, y=30)

    def render(self):
        pass
