import tkinter


class Dropdown(tkinter.OptionMenu):
    def __init__(self, parent, options=[], default=None, *args, **kwargs):
        self.selected_value = tkinter.StringVar(parent)

        if default:
            self.selected_value.set(default)
        else:
            self.selected_value.set(options[0] if options else "")
        self.selected_value.get()

        super().__init__(parent, self.selected_value, *options, *args, **kwargs)

    def get_selection(self):
        return self.selected_value
