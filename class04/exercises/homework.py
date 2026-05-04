# Exercise 1 -- Implement a Book class

class Book:
    book_counter = 0; # class attribute

    def __init__ (self, name, author):
        self.name = name # instance attribute
        self.author = author # instance attribute
        self.increment_counter()

    
    def increment_counter(self):
        Book.book_counter += 1

book1 = Book("The Little Prince", "Antoine de Saint-Exupery")
print(book1.name)
print(Book.book_counter)
book2 = Book("1984", "George Orwell")
book3 = Book("World Without End", "Ken Follett")
print(Book.book_counter)

# Exercise 2 -- Create a class called Student.
print("==== Exercise 2 ====")
class Student:
    school_name = "Vanier College"
    student_count = 0

    def __init__ (self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade
        self.increment_count()

    def increment_count(self):
        Student.student_count += 1

    def display_info(self):
        print(f"{self.name} studies {self.program} at {self.school_name}. Grade: {self.grade}")

student1 = Student("Ann", "Architecture", 89)
student2 = Student("Bob", "Business Foundations", 83)
student3 = Student("Cathy", "Computer Science", 95)

print(f"Students count: {Student.student_count}")
student1.display_info()
student2.display_info()
student3.display_info()

# Exercise 3 -- Create a class called Product.
print("==== Exercise 3 ====")

class Product:
    category = "Electronics"
    tax_rate = 0.15

    def __init__ (self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        self.price = round(self.price * (1 + self.tax_rate), 2)
        # self.price = self.price + (self.price * self.tax_rate)
        return self.price
    
product1 = Product("SSD", 340)
product2 = Product("Mouse", 60)
product3 = Product("Keyboard", 100)

print(f"{product1.name}'s price with tax is {product1.price_with_tax()}")
print(f"{product2.name}'s price with tax is {product2.price_with_tax()}")
print(f"{product3.name}'s price with tax is {product3.price_with_tax()}")

Product.tax_rate = 0.20
print("--- Taxed changed --- ")

print(f"{product1.name}'s price with tax is {product1.price_with_tax()}")
print(f"{product2.name}'s price with tax is {product2.price_with_tax()}")
print(f"{product3.name}'s price with tax is {product3.price_with_tax()}")

# Exercise 3 -- Create a class called Employee.
print("==== Exercise 4 ====")

class Employee:
    company_name = "TechNova"
    bonus_rate = 0.10
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.increment_count()

    def increment_count(self):
        Employee.employee_count += 1

    def calculate_bonus(self):
        bonus = self.salary * self.bonus_rate
        return bonus
    
    def display_employee(self):
        print(f"{self.name} works at TechNova. Salary: {self.salary}. Bonus: {self.calculate_bonus()}")

employee1 = Employee("John", 50000)
employee2 = Employee("Jane", 60000)
employee3 = Employee("Jake", 40000)

employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

Employee.bonus_rate = 0.20 # class attribute change

print('--- Class attribute "bonus rate" changed to 0.2')
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

employee1.bonus_rate = 0.50 # instance attribute change
print('--- Instance attribute "bonus rate" changed for empoyee1 to 0.5')
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

Employee.bonus_rate = 0.05 # class attribute change
print('--- Class attribute "bonus rate" changed to 0.05')
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

# employee1 has a shadowed bonus_rate as we changed it individually