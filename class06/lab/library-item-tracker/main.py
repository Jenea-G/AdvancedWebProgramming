class Book:
    def __init__(self, title, author, available = True):
        self.title = title
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

book1 = Book("The Little Prince", "Antoine de Saint-Exupery", False)
book2 = Book("1984", "George Orwell")
book1.display_info()
book2.display_info()

book1.borrow()
book1.return_book()
book2.return_book()