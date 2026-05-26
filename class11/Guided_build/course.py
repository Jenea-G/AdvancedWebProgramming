from status import CourseStatus

MAX_CAPACITY = 60

class Course:
    def __init__(self, title, capacity, status): 
        if (self.is_capacity_valid(capacity)):
            self.capacity = capacity
        else:
            raise ValueError(f"capacity should be greater than 0 and not exeed {MAX_CAPACITY}")
        self.title = title
        self.status = status

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if not isinstance(value, CourseStatus):
            raise ValueError("status must be a CourseStatus value")
        self.__status = value

    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value}")

    def close_registration(self):
        self.status = CourseStatus.CLOSED

    def cancel_course(self):
        self.status = CourseStatus.CANCELLED
    
    def reopen_course(self):
        self.status = CourseStatus.OPEN

    @staticmethod
    def is_capacity_valid(value):
        if (0 < value <= MAX_CAPACITY):
            return True
        return False

