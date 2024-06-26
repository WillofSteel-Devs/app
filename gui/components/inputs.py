import tkinter


class TextInput(tkinter.Entry):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(
            parent,
            width=50,
            *args,
            **kwargs,
        )


class IntergerOnlyEntry(tkinter.Entry):
    def __init__(self, parent, minNumber=None, maxNumber=None, width=50, *args, **kwargs):
        self.minNumber = minNumber
        self.maxNumber = maxNumber

        self.var = tkinter.StringVar()

        super().__init__(parent, width=width, textvariable=self.var, *args, **kwargs)

        self.validate_command = (self.register(self.validate_input), "%P")

        self.config(validate="key", validatecommand=self.validate_command)

    def validate_input(self, new_value):
        if new_value.isdigit():
            check_value = int(new_value)
            # check if number within range, if range specified
            if self.maxNumber is not None:
                if not (check_value > self.maxNumber):
                    self.var = self.maxNumber  # force value to max
            if self.minNumber is not None:
                if not (check_value < self.minNumber):
                    self.var = self.minNumber  # force value to min

            return True

        return False
