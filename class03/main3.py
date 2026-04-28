# method-writing practice 

class Book:
    def __init__ (self, title, author, available = True):
        self.title = title #string
        self.author = author #string
        self.available = available #boolean --> True or False

    # lend a book (borrow to someone)
    def borrow(self):
        if(self.available == False):
            print(f"{self.title} is already borrowed.")
        else:
            self.available = False
            print(f"{self.title} has been borrowed.")


    # return the book (get it back)
    def return_book(self):
        if(self.available == False):
            self.available = True
            print(f"{self.title} has been returned")
        else:
            print(f"I don't think that's my copy! I already have {self.title}.")


    # show the status
    def show_status(self):
        print(f"{self.title} availability: {self.available}")

book1 = Book("Game of Thrones", "George R.R. Martin")
book2 = Book("Another book", "Another Autor")

book1.borrow()
book1.borrow()
book1.return_book()
book1.return_book()
book2.borrow()

book1.show_status()
book2.show_status()
