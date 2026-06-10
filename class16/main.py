# DATA CLASSES

# data classes' main job is to store and represent data clearly.

from dataclasses import dataclass

#regular version
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

# dataclass version
@dataclass
class Student:
    name: str
    gpa: float

student1 = Student("Alice", 3.8)
student2 = Student("Alice", 3.8)
print(student1)

print(student1 == student2) # true for dataclass but false for simple class

# data class is cleaner and faster to write for simple data container

# What does Data Class gives?
#   auto generated __init__
#   auto generated display
#   auto generates equality function -- to compare different instances/objects
#   enforces type

@dataclass
class Course:
    title:str
    credits: int = 3 #defining a default value

# if you have a property with a default value, all the following properties should also have one.

course1 = Course("Advanced Programming")
course2 = Course("Phys Ed", 4)

print(course1)
print(course2)


# When it's good to use a Regular Class

#   when it has lots of behaviour
#   enforces many invariants
#   has complex property logic
#   manages state changes heavily

# When a Data Class is a good fit:

#   sotres data
#   represents a record
#   all of this benefits from automatic functions such as __init__, equality with comparisons, etc.

# Methods inside a data class:

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total_value(self):
        return self.price * self.quantity
    
product1 = Product("keyboard", 49.99, 3)

print(product1.total_value()) # dataclass method is called