import tkinter


class TextInput(tkinter.Entry):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(
            parent,
            width=50,
            *args,
            **kwargs,
        )
