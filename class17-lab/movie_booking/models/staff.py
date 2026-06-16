class Staff:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def display_info(self):
        print(f"Employee name: {self.name} | function: {self.function}")