class Book:
    library_name = "Central Library"
    count = 0

    def __init__(self, title, author, genre = "not specified", available = True):
        if(self.is_valid(title)):
            self.title = title
        else:
            print("Please, enter a valid title.")
            return
        self.author = author
        self.genre = genre
        self.available = available
        self.increment_count()

    def display_info(self):
        if (self.available):
            availability = "available"
        else:
            availability = "borrowed"
        print(f"The book: '{self.title}' is written by the author: {self.author}, genre of the book is: {self.genre}. This book is {availability}.")

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

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def show_count(cls):
        print(f"There are {cls.count} books in the {cls.library_name}.")

    @classmethod
    def from_string(cls, data):
        title, author, genre = data.split(",")
        return cls(title, author, genre)

    @staticmethod
    def is_valid(title):
        if(len(title.strip()) > 0):
            return True
        else:
            return False