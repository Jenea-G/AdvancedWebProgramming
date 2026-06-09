from helper import Helper
class User:
    def __init__(self, name, email):
        if(Helper.isValidString(name)):
            self.name = name
        else: raise ValueError("The username shouldn't be empty")
        if(Helper.isValidString(email)):
            self.email = email
        else: raise ValueError("The email shouldn't be empty")

    def display_info(self):
        print(f"Name: {self.name}. Email: {self.email}")