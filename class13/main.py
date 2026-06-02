# Inheritance

# what happens when several classes are relaed and should share common behaviour
# without duplicating code??


# Encapsulation (recap)

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance # object state should be protected intentionally.

# Properties:
# let's keep clean attribute syntax
# validate and/ or controll access to our attributes

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

    @property
    def gpa(self):
        return self.__gpa ## define private attribute
    
    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0: # This is an invariant!
            self.__gpa = value
        else:
            raise ValueError("Invalid GPA")
        
# Invariants:

# is a rule that must always remain true

# constants and enums

from enum import Enum

class CourseStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"

status = CourseStatus.OPEN
print(status.value)

# enums reduce invalid values and improve readability.

# for example: CourseStatus class becomes a container for a series of constants.

# all of the consepts above help us design one class properly.


# INHERITANCE 
# let's one class reuse and extend another class.

# A parent class : more general class
# A child class : more specific class that inherits from the parent

# suppose you are building different kinds of users in a system.
# you might Have: User - StudentUser - AdminUser
# They may all shere:
#   username
#   password
#   email
#   name
#   address
#   phone_number

# they may differ in:
#       students have a program
#       admins have departments

# without inheritance, we have to repeat the code across several classes.
# with inheritance, the child can reuse common parent behaviour.

# Inheritance = shared structure + specialization

class User:
    def __init__(self, username):
        print("hello from parent constructor")
        self.username = username
    
    def introduce(self):
        print(f"Hello, my name is {self.username}")

class StudentUser(User): # extending the User class
    def __init__(self, username, program):
        super().__init__(username) # super means go to the parent class
                                    # and in here we refer to the parent class' constructor
                                    # hello message will print here as we are executing the parent constructor here
        self.program = program

student1 = StudentUser("Jane", "Web Dev")
student1.introduce() # studentUser uses the function from the parent class
print(student1.program)

class AdminUser(User):
    def __init__(self, username, dpt):
        super().__init__(username)
        self.dpt = dpt

admin1 = AdminUser("John", "Accounting")
admin1.introduce()
print(admin1.dpt)

# StudentUser(User): this basically means StudentUser inherits from User
# StudentUser gets access to inherited methods like introduce()
# super().__init__(name) calls parent
    # super is very important. because without the parent setup might not happen!
    # double important when the parent constructor initializes important shared data.


# The difference between abstract classes and inheritance:
#   abstract classes define strict rules on what functions need to be implemented by the class.
#   inheritance allows one Parent class to pass down functions and attributes to a child class.