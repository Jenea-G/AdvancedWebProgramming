class Book:
    library_name = "Central Library"

    def __init__(self, title, author, available = True):
        if(self.is_valid(title)):
            self.title = title
        else:
            print("Please, enter a valid title.")
            return
        self.author = author
        self.available = available

    def display_info(self):
        if (self.available):
            availability = "available"
        else:
            availability = "borrowed"
        print(f"The book: '{self.title}' by the author: {self.author} is {availability}.")

    def borrow(self):
        if(self.available):
            self.available = False
            print(f"The book '{self.title}' by {self.author} has been borrowed successfully.")
        else: 
            print(f"The book '{self.title}' by {self.author} has already been borrowed. Try another one.")
    
    def return_book(self):
        if(self.available == False):
            self.available = True
            print(f"The book '{self.title}' by {self.author} has been returned successfully.")
        else: 
            print(f"I already have '{self.title}' by {self.author}, this is not my copy.")

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

    @staticmethod
    def is_valid(title):
        if(len(title.strip()) > 0):
            return True
        else:
            return False