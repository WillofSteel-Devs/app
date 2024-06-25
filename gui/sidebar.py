import tkinter
from gui.components import labels, buttons


class Sidebar(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=150, height=600, bg="#BEB7A4")
        self.parent = parent

        self.title = labels.SidebarLabel(self, text="Sidebar")
        self.title.pack()

        self.npc_button = buttons.Sidebarbutton(
            self, text="NPC", command=lambda: self.switch_frame(self.parent.npc_frame)
        )
        self.npc_button.pack()

        self.attack_button = buttons.Sidebarbutton(
            self,
            text="Attack",
            command=lambda: self.switch_frame(self.parent.attack_frame),
        )
        self.attack_button.pack()

        self.construction_button = buttons.Sidebarbutton(
            self,
            text="Construction",
            command=lambda: self.switch_frame(self.parent.construction_frame),
        )
        self.construction_button.pack()

        self.recruitment_button = buttons.Sidebarbutton(
            self,
            text="Recruitment",
            command=lambda: self.switch_frame(self.parent.recruitment_frame),
        )
        self.recruitment_button.pack()

        self.alliance_button = buttons.Sidebarbutton(
            self,
            text="Alliance",
            command=lambda: self.switch_frame(self.parent.alliance_frame),
        )
        self.alliance_button.pack()

        self.lookup_button = buttons.Sidebarbutton(
            self,
            text="Lookup",
            command=lambda: self.switch_frame(self.parent.lookup_frame),
        )
        self.lookup_button.pack()

        self.outposts_button = buttons.Sidebarbutton(
            self,
            text="Outposts",
            command=lambda: self.switch_frame(self.parent.outposts_frame),
        )
        self.outposts_button.pack()

        self.apiKey_button = buttons.Sidebarbutton(
            self,
            text="API Key",
            command=lambda: self.switch_frame(self.parent.api_key_frame),
        )
        self.apiKey_button.pack()

    def disable_option(self, button: str) -> None:
        if button == "npc":
            button = self.npc_button
        elif button == "attack":
            button = self.attack_button
        elif button == "construction":
            button = self.construction_button
        elif button == "recruitment":
            button = self.recruitment_button
        elif button == "alliance":
            button = self.alliance_button
        elif button == "lookup":
            button = self.lookup_button
        elif button == "outposts":
            button = self.outposts_button
        elif button == "apiKey":
            button = self.apiKey_button

        if button:
            button.pack_forget()


    def switch_frame(self, frame):
        self.master.change_frame(frame)  # type: ignore # this seems to be right? I'm not sure why it's throwing an error with pyright
