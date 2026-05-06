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
            availability = "not available"
        print(f"The book '{self.title}' by {self.author} is {availability}.")

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


book1 = Book("The Little Prince", "Antoine de Saint-Exupery", False)
book2 = Book("1984", "George Orwell")
# ==== Tests ====
book1.display_info()
book2.display_info()
print("==== tests borrow(), return_book() and display_info() =====")
book1.borrow()
book1.return_book()
book2.return_book()

book1.display_info()
book2.display_info()

print("=== test library name change ===")
print(Book.library_name)
Book.change_library_name("Bibliotheque de Vieux Saint-Laurent")
print("Library name changed to:", Book.library_name)

print("=== test static method ===")
book3 = Book("", "Any Author")
book3 = Book("Clean Code", "Robert C.")
print(f"Book3 has been created with the title: '{book3.title}', and the author: {book3.author}")