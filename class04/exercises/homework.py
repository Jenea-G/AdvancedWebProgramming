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
