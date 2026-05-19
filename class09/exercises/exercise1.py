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

# Ex.5

# Create a class with:
#   owner
#   private __balance
# Requirements:
#   property balance
#   setter prevents negative values
#   method deposit(amount)
#   method withdraw(amount)


# Ex.6

# Create a class with:
#   name
#   private __price
#   quantity
# Requirements:
#   property price
#   setter prevents negative values
#   read-only property inventory_value

# Ex.7

# Create a class with:
#   title
#   private __rating
# Requirements:
#   property rating
#   setter only accepts values between 0 and 10