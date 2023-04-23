class MenuOption:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def execute(self):
        if self.function is not None:
            self.function()