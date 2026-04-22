# a class for a book

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


book1 = Book("100 years of solitude", "Gabriel Garcia Marquez", 10.23)
book2 = Book("Clean Code", "Robert C. Martin", 20.99)

print(book1.price)

# we can overwrite the property
book1.price = 100.99

print(book1.price) # we should see 100.99

class Product:
    def __init__(self, name, price = 0, stock = 0): # giving a default value if there will be no input value
        self.name = name
        self.price = price
        self.stock = stock

p1 = Product('Keyboard', 20, 10)
p2 = Product('Mouse', stock = 5) # will use the default value for the price and create an object with that
# we either define the property or it will use the order from the constructor to define the given property

print(p2.stock)

p2.stock = 100 # we add the quantity
print(p2.stock)

