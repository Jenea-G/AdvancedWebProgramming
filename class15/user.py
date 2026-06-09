class User:
    def __init__(self, name, email):
        if(len(name.strip()) > 0):
            self.name = name
        else: raise ValueError("The username shouldn't be empty")
        self.email = email

    def display_info(self):
        print(f"User's name: {self.name}. Email: {self.email}")

    