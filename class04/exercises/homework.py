# Exercise 1 -- Implement a Book class

class Book:
    book_counter = 0; # class attribute

    def __init__ (self, name, author):
        self.name = name # instance attribute
        self.author = author # instance attribute
        self.increment_counter()

    
    def increment_counter(self):
        Book.book_counter += 1

book1 = Book("The Little Prince", "Antoine de Saint-Exupery")
print(book1.name)
print(Book.book_counter)
book2 = Book("1984", "George Orwell")
book3 = Book("World Without End", "Ken Follett")
print(Book.book_counter)

# Exercise 2 -- Create a class called Student.