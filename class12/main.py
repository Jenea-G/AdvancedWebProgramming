# lists
my_list = [1, "hello", True, 10.5] # lists could be mixed!
print(my_list)
print(my_list[1])

# equivalent of a foreach loop!
for i in my_list:
    print(i)

# what's split
data = "test,test2"

print(data.split(","))

# split is a string method that converts a string to a list by common denominator
        # in the case above it's a ',' 


# let's move towards our first design pattern! 

# alternative constructor:
class Student:
    def __init__(self, name, program): # main constructor
        self.name = name
        self.program = program

    # we keep object-creation logic inside the class
    # helping the object creation to be dynamic!
    @classmethod
    def from_string(cls, data): # alternative constructor
        name, program = data.split(",")
        return cls(name, program)
    
    # what if we want a new object out not all of the inputs
    @classmethod
    def newly_admitted(cls, name): # another alternative constructor
        return cls(name, "")
    

# student1 = Student("Alice", "Web Development") # valid!
student1 = Student.from_string("Alice,Web Development") # Alternative Constructor
student2 = Student.newly_admitted("John")

print(f"{student1.name} studies in {student1.program}")

print(f"{student2.name} studies in {student2.program}")



# in real program, data often comes in a variety of formats! 

    # for example: 
        # comma-separated strings (csv, excel sheet, etc.)
        # a dictionary
        # as a database row
        # as a JSON object
        # sometimes a user input that needs conversion

# so for example if you have in your database, or a excel sheet:
# value1,value2,value3, etc..

# using the alternative constructor we can parse the data properly!

# alternative constructors are important, because the object always stays the same but the input
# format changes.

# ====================
class Product:
    # 1. separate constructor arguments (__init__)
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    # 2. one comma-separated string
    @classmethod
    def from_string(cls, data):
        parts = data.split(",")
        name = parts[0]
        price = float(parts[1])
        category = parts[2]
        return cls(name, price, category)
    
    # 3. a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["category"])
    
    # 4. a new product with no category and price (just a name)
    @classmethod
    def from_name(cls, data):
        return cls(data, 0, "")
    
    def show(self):
        print(f"{self.name} is ${self.price} and is in category: {self.category}")
    

# created with comma separated string
product1 = Product.from_string("Mouse,100,Category 1")

# created with a dictionary
product2 = Product.from_dict({"name": "Tablet", "price": 50, "category": "electronics"})

# with normal constructor
product3 = Product("Keyboard", 20, "Utils")

# with just a name
product4 = Product.from_name("Screen")

product1.show()
product2.show()
product3.show()
product4.show()