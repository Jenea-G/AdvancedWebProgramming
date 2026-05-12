# Interfaces / Abstraction

# so far we've built concrete classes

class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Book name is {self.name}")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product name is {self.name}")

# let's move one level higher than just concrete classes.
# instead of asking what one object does, we ask what a whole ctegory of objects should be able to do.

#
# but!! a credit card pays one way ---- payPal pays anothre way -- back transfer works differently, etc.

# in the examples above, we see that our classes might behave in a similar way and we want to think of abstraction as a way that allows up to design our code.

# the shared idea for the above: is the abstraction "a payment method can make a payment"

# abstraction allows to have :
# 1. clearer design
# 2. less duplication
# 3. easier extension
# 4. more consistent behaviour
# 5. in case of larger code bases: better teamwork and mainanability

# PRACTICE !

# the common approach to use interfaces in python is:
# abstract base classes using the abs module

# 1. import interfaces module
from abc import ABC, abstractmethod

# ABSTRACT CLASS Shape
class Shape(ABC): # ABC means this class is abstract
    @abstractmethod # we mark a method that subclasses must implement
    def area(self):
        pass

# VERY IMPORTANT: Shape on its own cannot and must not be instantiated directly.

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius

    def area(self): # we cannot create a Circle class without defining area method as it is present in a shape abstract class
        return 3.14 * self.radius * self.radius

# Here we see that both classes implement the avstract class shape ind its methods, but in their own way.
# every shape must provide an area() method

rectangle = Rectangle(2, 4)
circle = Circle(3)

print(f"Rectangle area is: {rectangle.area()}")
print(f"Circle area is: {circle.area()}")

print("=============")
# this could be the coe that interacts with our classes
def print_area(shape):
    print(shape.area())

print_area(rectangle)
print_area(circle)


# another example

# This is our CONTRACT
class FinancialInstitution(ABC):
    @abstractmethod
    def payment(self, amount):
        pass

class Visa(FinancialInstitution):
    def __init__(self, card_number):
        self.card_number = card_number
        self.balance = 0

    def payment(self, amount):
        self.balance += amount
        print(f"{amount} withdrawn! by Visa")

    def show_balance(self):
        print(self.balance)

class PayPal(FinancialInstitution):
    def __init__(self, card_number, debit_balance):
        self.card_number = card_number
        self.debit_balance = debit_balance

    def payment(self, amount):
        self.debit_balance -= amount
        print(f"{amount} paid by Paypal!")

    def donate(self):
        pass

visa_card = Visa("123")
paypal_account = PayPal("456", 100)

print("===========")
def checkout(amount, fi):
    print(f"You owe ${amount}")

    fi.payment(amount)

checkout(50, paypal_account)
checkout(60, visa_card)