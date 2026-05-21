#  Create a class called: CourseSection
class CourseSection:
    def __init__(self, title, capacity, enrolled = 0):
        if(self.is_not_empty(title)):
            self.title = title
        else:
            raise ValueError("The title shouldn't be empty.")
        self.capacity = capacity
        self.enrolled = enrolled
        print(f"Course section for '{self.title}' was successfully created.")

    @staticmethod
    def is_not_empty(title):
        if(len(title.strip()) > 0):
            return True
        else:
            return False
        
    @staticmethod
    def is_positive_number(capacity):
        if(capacity > 0):
            return True
        else:
            return False
        
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if(self.is_positive_number(value)):
            self.__capacity = value
        else:
            raise ValueError("The capacity should be greater than 0")
        
    @property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, value):
        if(value >= 0):
            self.__enrolled = value
        else:
            raise ValueError("The enrolled number should be greater than or equal to 0.")
        
    def register_student(self):
        if(self.capacity > self.enrolled):
            self.enrolled += 1
            print(f"You have successfully enrolled to the {self.title} course.")
        else:
            raise ValueError("The maximum course capacity have been reached. You cannot enroll to this course.")
        
    def drop_student(self):
        if(self.enrolled > 0):
            self.enrolled -= 1
            print("You have dropped the course successfully.")
        else:
            raise ValueError("You cannot drop. There are no sutdents enrolled to the course.")
        
    def display_info(self):
        print(f"The {self.title} course has the maximum capacity of {self.capacity}, and {self.enrolled} students are currently enrolled")

    