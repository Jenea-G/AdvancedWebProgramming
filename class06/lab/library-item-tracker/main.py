class Book:
    library_name = "Central Library"

    def __init__(self, title, author, available = True):
        self.title = title
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

    


book1 = Book("The Little Prince", "Antoine de Saint-Exupery", False)
book2 = Book("1984", "George Orwell")
book1.display_book()
book2.display_book()

print("=== test library name change ===")
print(Book.library_name)
Book.change_library_name("Bibliotheque de Vieux Saint-Laurent")
print("Library name changed to:", Book.library_name)