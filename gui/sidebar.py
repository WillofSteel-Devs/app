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

        self.lookup_button = buttons.Sidebarbutton(
            self,
            text="Lookup",
            command=lambda: self.switch_frame(self.parent.lookup_frame),
        )
        self.lookup_button.pack()

    def switch_frame(self, frame):
        self.master.change_frame(frame)  # type: ignore # this seems to be right? I'm not sure why it's throwing an error with pyright
