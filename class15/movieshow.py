from helper import Helper

from enum import Enum
class ShowStatus(Enum):
    OPEN = "Open"
    SOLD_OUT = "Sold out"
    CANCELLED = "Cancelled"

class MovieShow:
    def __init__(self, title, capacity, booked_seats, status):
        self.title = title
        self.capacity = capacity
        self.booked_seats = booked_seats
        self.status = status
        print("Movie show has been created")

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if Helper.isValidName(value):
            self.__title = value
        else:
            raise ValueError("Title cannot be empty")
        
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if Helper.isGreaterThan0(value):
            self.__capacity = value
        else:
            raise ValueError("capacity must be greater than 0")
        
    @property
    def booked_seats(self):
        return self.__booked_seats
    
    @booked_seats.setter
    def booked_seats(self, value):
        if Helper.isPositiveNumber(value) and value <= self.capacity:
            self.__booked_seats = value
        else:
            raise ValueError("Booked seats cannot be negative and cannot exceed capacity")
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        if not isinstance(value, ShowStatus):
            raise ValueError("status must be a ShowStatus value")
        self.__status = value