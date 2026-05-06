class Book:
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

    def borrow(self):
        if(self.available):
            self.available = False
            print(f"The book {self.title} by {self.author} has been borrowed successfully")
        else: 
            print(f"The book {self.title} by {self.author} has already been borrowed. Try another one.")

book1 = Book("The Little Prince", "Antoine de Saint-Exupery", False)
book2 = Book("1984", "George Orwell")
book1.display_book()
book2.display_book()

book1.borrow()