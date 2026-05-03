# Class attributes vs instance attributes

class Student:
    def __init__(self, name, program):
        self.name = name
        self.program = program

student1 = Student("Alina", "Web Development")
student2 = Student("Karim", "Computer Science")

print(student1.name)
print(student2.name)


# what if all students were from the same school?

# the idea is:
    # Some data belongs to:
    #  each object individually
    # Other data belongs to:
    #  the whole class

# instance attribute --> per-object state
# class attribute --> shared class-level state

class Student:
    school_name = "Vanier College" # this is our shared attribute

    def __init__(self, name, program):
        # these are instance attributes / per-object state
        self.name = name
        self.program = program

student1 = Student("Alice", "Web Development")
student2 = Student("Karim", "Computer Science")

print(student1.name)
print(student2.name)

print(student1.school_name)
print(student2.school_name)

Student.school_name = "ABC College" # changing the shared attribute directrly for all instances of a class

print(student1.school_name)
print(student2.school_name)


# visual comparison:

    # Instance attributes:
    #  created with self
    #  usually set in __init
    #  different per object

    # Class attributes:
    #   defined in class body
    #   shared across all instances
    #   used for common data or class-level configuration
    
class Product:
    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = Product("Keyboard", 10)
product2 = Product("Mouse", 25)

product1.price = 8

print(product1.price)
print(product2.price)

print(product2.category)
print(product1.category)

# shadowing a class attribute

class Employee:
    bonus = 0.5

    def __init__ (self, name):
        self.name = name

employee1 = Employee("John")
employee2 = Employee("Jane")

print(f"Employee 1 bounus: {employee1.bonus}")
print(f"Employee 2 bounus: {employee2.bonus}")

Employee.bonus = 1

print(f"Employee 1 bounus: {employee1.bonus}")
print(f"Employee 2 bounus: {employee2.bonus}")

employee1.bonus = 2 # changing the shadow attribute
                    # this doesnt change the class attribute itself!
                    # we create a new instance attribute on employee1!

employee3 = Employee("test")

print(f"Employee 1 bounus: {employee1.bonus}")
print(f"Employee 2 bounus: {employee2.bonus}")
print(f"Employee 3 bounus: {employee3.bonus}")

# case study

# A good use case for class attributes are :
    # shared across all instances
    # conceptually the same for the whole class
    # they're usually configuration-like or constant-like
    # they're counters or class-wide metadata

# Bad use cases for class attributes are :
    # values that should usually be different per object.
    # any value that changes oftn, or is indiidually different

# Let's look at some examples:
    # school name ---> class attribute
    # max capacity ---> class attribute
    # account password ---> instance attribute
    # tax rates ---> class attribute
    # course grade ---> instance attribute