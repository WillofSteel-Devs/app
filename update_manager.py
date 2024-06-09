import tkinter


class UpdateManager(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("My App")
        self.geometry("400x200")
        self.label = tkinter.Label(self, text="Hello, world!")
        self.label.pack()


if __name__ == "__main__":
    app = UpdateManager()
    app.mainloop()
