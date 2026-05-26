from status import CourseStatus

class Course:
    def __init__(self, title, capacity, status):
        self.title = title
        self.capacity = capacity
        self.status = CourseStatus.OPEN