import tkinter

class Sidebar(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.npc_button = tkinter.Button(self, text="NPC")
        self.npc_button.pack()

        self.attack_button = tkinter.Button(self, text="Attack")
        self.attack_button.pack()

        self.construction_button = tkinter.Button(self, text="Construction")
        self.construction_button.pack()

        self.recruitment_button = tkinter.Button(self, text="Recruitment")
        self.recruitment_button.pack()

        self.pack(side=tkinter.LEFT)