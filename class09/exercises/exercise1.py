# Ex.1

# Create a class with:
#   name
#   private __gpa
# Requirements:
#   property gpa
#   setter only accepts values between 0.0 and 4.0
print("=== Ex.1 ===")
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa

    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if 0.0 < value <= 4:
            self.__gpa = value
        else: print("Provide a value between 0.0 and 4.0")

s1 = Student("Sam", 3)
print(f"{s1.name}'s gpa equals to {s1.gpa}")
s1.gpa = 5
s1.gpa = 3.8
print(f"{s1.name}'s gpa equals to {s1.gpa}")


# Ex.2

# Create a class with:
#   name
#   internal _price
# Requirements:
#   property price

# setter must reject negative values
print("=== Ex.2 ===")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else: print("Price should be more than 0")

product1 = Product("Apple", 5)
print(product1.price)
product1.price = -1
product1.price = 3
print(product1.price)


# Ex.3 

# Create a class with:
#   radius

# Requirements:
# a read-only property area

# You should not store area directly; you should compute it.
print("=== Ex.3 ===")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.radius * 3.14
    
c1 = Circle(3)
print(c1.area)


# Ex.4 

# Create a class with:
#   first_name
#   last_name
# Requirements:
#   read-only property full_name
print("=== Ex.4 ===")
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
p1 = Person("Sam", "Collins")
print(p1.full_name)

# Ex.5
# Create a class with:
#   owner
#   private __balance
# Requirements:
#   property balance
#   setter prevents negative values
#   method deposit(amount)
#   method withdraw(amount)
print("====== Ex.5 =====")
class Account:
    def __init__(self, acc_n, balance):
        self.acc_n = acc_n
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else: print("Balance couldn't be less than 0")

    def deposit(self, amount):
        if amount > 0:
            self.__balance = amount
        else: "The amount should be more than 0"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else: print(f"Impossible to withdraw the amount {amount}")

acc1 = Account(13, 100)
print(f"The account #{acc1.acc_n} balance is {acc1.balance}")
acc1.balance = -10
acc1.balance = 0
print(f"The account #{acc1.acc_n} balance was set to {acc1.balance}")
acc1.withdraw(10)
acc1.deposit(500)
print(f"The account #{acc1.acc_n} balance is {acc1.balance}")



# Ex.6

# Create a class with:
#   name
#   private __price
#   quantity
# Requirements:
#   property price
#   setter prevents negative values
#   read-only property inventory_value
print("====== Ex.6 =====")
class ProductStock:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @property
    def inventory_value(self):
        return self.__price * self.quantity
    
    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else: print("Price should be more than 0")

product1 = ProductStock("Pinata", 3, 10)
print(f"The inventory value of '{product1.name}' is {product1.inventory_value}")
product1.price = -1
product1.price = 15
print(f"The inventory value of '{product1.name}' is {product1.inventory_value}")

# Ex.7

# Create a class with:
#   title
#   private __rating
# Requirements:
#   property rating
#   setter only accepts values between 0 and 10
print("=== Ex.7 ===")
class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.__rating = rating

    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, value):
        if 0 <= value <= 10:
            self.__rating = value
        else: print("The rating could only be between 0 and 10")

m1 = Movie("Interstellar", 6)
print(f"The movie '{m1.name}' has rating: {m1.rating}.")
m1.rating = 15
m1.rating = -1
m1.rating = 10
print(f"The movie '{m1.name}' has rating: {m1.rating}.")