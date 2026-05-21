#  Create a class called: CourseSection
class CourseSection:
    def __init__(self, title, capacity, enrolled = 0):
        if(self.is_not_empty(title)):
            self.title = title
        else:
            raise ValueError("The title shouldn't be empty.")
        if(self.is_positive_number(capacity)):
            self.__capacity = capacity
        else:
            raise ValueError("The capacity should be greater than 0")
        if(enrolled >= 0):
            self.__enrolled = enrolled
        else:
            raise ValueError("The enrolled number should be greater than or equal to 0.")
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
            self.capacity = value
        else:
            raise ValueError("The capacity should be greater than 0")
        
    @property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, value):
        if(value >= 0):
            self.enrolled = value
        else:
            raise ValueError("The enrolled number should be greater than or equal to 0.")

    