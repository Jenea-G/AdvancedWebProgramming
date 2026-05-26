from status import CourseStatus

class Course:
    def __init__(self, title, capacity, status):

        
        self.title = title
        self.capacity = capacity
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

