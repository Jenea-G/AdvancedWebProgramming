# Static methods !!!

    # they belong to the class
    # but it doesnt use self or cls
    # it's marked with @staticmethod

# it's basically a function placed inside the class namespace becuse it's related to thatt class's purpose.

class Student:
    # this method doesnt need a specific stuent object or the class itself!
    # but, it's still related to the Student domain.
    @staticmethod
    def is_valid_name(name):
        if(len(name.strip()) > 0):
            return True
        else:
            return False
        
print(Student.is_valid_name("Alice"))
print(Student.is_valid_name(""))

class Helper:
    @staticmethod
    def is_valid_email(email):
        return "@" in email and '.' in email # if @ and . are in email then True -- otherwise - False
    
    @staticmethod
    def is_valid_name(name):
        if(len(name.strip()) > 0):
            return True
        else:
            return False
        
    @staticmethod
    def format_price(price):
        return f"${price:.2f}"
    
print(Helper.is_valid_email("test"))
print(Helper.is_valid_email("test@mail.com"))

print(Helper.format_price(20))

class Student:
    def __init__(self, name, email):
        if(Helper.is_valid_email(email)):
            self.email = email
        else:
            return
        
        if(Helper.is_valid_name(name)):
            self.name = name
        else:
            return


class Product:
    def __init__(self, name, price, category):
        if(Helper.is_valid_name(name)):
            self.name = name
        else:
            return
        
        self.price = price
        self.category = category
    
    def show_price(self):
        print(Helper.format_price(self.price))

    @staticmethod
    def is_valid_category(category):
        return len(category.strip()) > 0
        
# it is very common in backend programming to have static methods that are helper functions
# because these will be used all over your code, in a standardized manner.

# comparison:

# Instance methods:
    # no decorator (@ something)
    # first parameter: self (ALWAYS)
    # works with only one object
    # reads/modifies instance state

# Class methods:
    # deorator: @classmethod
    # first parameter is: cls (ALWAYS)
    # works with class-level state (class attributes, etc.)
    # often used for alternative constructors or shared behaviour

# Static methods:
    # decorator: @staticmethod
    # no self or cls 
    # usually used as utility/helper logic