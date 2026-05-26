from status import CourseStatus

class Course:
    def __init__(self, title, capacity, status):
        if not isinstance(status, CourseStatus):
            raise ValueError("status must be a CourseStatus value")
        
        self.title = title
        self.capacity = capacity
        self.status = status

    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value}")