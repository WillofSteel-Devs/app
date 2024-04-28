import tkinter
from gui.components import labels, buttons

class Sidebar(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=150, height=600, bg='#000000')

        self.title = tkinter.Label(self, text="Sidebar")
        self.title.pack()
        
        self.npc_button = buttons.Sidebarbutton(self, text="NPC")
        self.npc_button.pack()

        self.attack_button = buttons.Sidebarbutton(self, text="Attack")
        self.attack_button.pack()

        self.construction_button = buttons.Sidebarbutton(self, text="Construction")
        self.construction_button.pack()

        self.recruitment_button = buttons.Sidebarbutton(self, text="Recruitment")
        self.recruitment_button.pack()

        self.lookup_button = buttons.Sidebarbutton(self, text="Lookup")
        self.lookup_button.pack()