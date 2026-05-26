from status import CourseStatus
from delivery import DeliveryMode

MAX_CAPACITY = 60

class Course:
    def __init__(self, title, capacity, status, delivery): 
        if (self.is_capacity_valid(capacity)):
            self.capacity = capacity
        else:
            raise ValueError(f"capacity should be greater than 0 and not exeed {MAX_CAPACITY}")
        self.title = title
        self.status = status
        self.delivery = delivery

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if not isinstance(value, CourseStatus):
            raise ValueError("status must be a CourseStatus value")
        self.__status = value
    
    @property
    def delivery(self):
        return self.__delivery
    
    @delivery.setter
    def delivery(self, value):
        if not isinstance(value, DeliveryMode):
            raise ValueError("Delivery mode must be a DeliveryMode enum value")
        self.__delivery = value

    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value} | Delivery mode: {self.delivery.value}")

    def close_registration(self):
        self.status = CourseStatus.CLOSED

    def cancel_course(self):
        self.status = CourseStatus.CANCELLED
    
    def reopen_course(self):
        if (self.status == CourseStatus.CLOSED):
            self.status = CourseStatus.OPEN
        else:
            raise ValueError("Only closed courses could be reopened")

    @staticmethod
    def is_capacity_valid(value):
        if (0 < value <= MAX_CAPACITY):
            return True
        return False
    
    def is_open_for_registration(self):
        if (self.status == CourseStatus.OPEN):
            return True
        return False

