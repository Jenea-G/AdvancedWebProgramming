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

    def display_book(self):
        if (self.available):
            availability = "available"
        else:
            availability = "not available"
        print(f"The book {self.title} by {self.author} is {availability}.")

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
book1.display_book()
book2.display_book()

print("=== test library name change ===")
print(Book.library_name)
Book.change_library_name("Bibliotheque de Vieux Saint-Laurent")
print("Library name changed to:", Book.library_name)

print("=== test static method ===")
book3 = Book("", "Any Author")
book3 = Book("Clean Code", "Robert C.")
print(f"Book3 has been created with the title: '{book3.title}', and the author: {book3.author}")
