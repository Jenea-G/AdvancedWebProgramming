from helper import Helper

from enum import Enum
class ShowStatus(Enum):
    OPEN = "Open"
    SOLD_OUT = "Sold out"
    CANCELLED = "Cancelled"

class BookingError(Exception):
    pass

class InvalidStatusError(Exception):
    pass
class MovieShow:
    MAX_TICKETS_PER_BOOKING = 7

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
            raise InvalidStatusError("status must be a ShowStatus value")
        self.__status = value

    def book_tickets(self, customer, quantity):
        if self.status == ShowStatus.CANCELLED:
            raise BookingError("You cannot book tickets. The show is cancelled")
        if self.status == ShowStatus.SOLD_OUT:
            raise BookingError("The tickets are already sold out")
        if  0 >= quantity or quantity > self.MAX_TICKETS_PER_BOOKING :
            raise BookingError(f"The quantity should be greater than 0 and cannot exceed the maximum booking per customer: {self.MAX_TICKETS_PER_BOOKING}")
        if (self.remaining_seats - quantity) < 0:
            raise BookingError(f"There are only {self.remaining_seats} seats left.")

        self.booked_seats += quantity
        if self.capacity == self.booked_seats:
            self.status = ShowStatus.SOLD_OUT

        print(f"{customer.name} has successfully booked {quantity} tickets for '{self.title}")

    def cancels_show(self):
        self.status = ShowStatus.CANCELLED

    def display_info(self):
        print(f"The movie show '{self.title}' has capacity of: {self.capacity}. Seats already booked: {self.booked_seats}. Status: {self.status}.")

    @property
    def remaining_seats(self):
        return self.capacity - self.booked_seats
