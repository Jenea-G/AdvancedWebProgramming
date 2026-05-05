# slpit is a string method that converts a string to a list by common denomitator
        # in the case above it's a ","


# Let's move towards our first design pattern!

# alternative constructor:

class Student:
    # school_name = "ABC College"

    def __init__(self, name, program): # main constructor
        self.name = name
        self.program = program

    # we keep object-creation logic inside the class
    # helping the object creation to be dynamic!
    @classmethod
    def from_string(cls, data): # alternative constructor
        name, program = data.split(",")
        return cls(name, program)
    
    @classmethod
    def from_form(cls, data):
        # parse the data according to how it's received
        pass
    
# student1 = Student("Alice", "Web Development") # valid!
student1 = Student.from_string("Alice,Web Development") # Alternative Constructor

print(f"{student1.name} studies in {student1.program}")

# in real program, data often comes in a variety of formats!

    # for example:
        # comma-separated strings (csv,excel sheet, etc.)
        # a dictionary
        # as a database row
        # as a JSON object
        # sometimes a user input that needs conversion

# so for example if you have in your db, or an excel sheet:
# value1,value2,value3

# using the alt constructor we can parse the data properly