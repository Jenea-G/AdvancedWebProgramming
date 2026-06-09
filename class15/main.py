MAX_TICKETS_PER_BOOKING = 3

from enum import Enum
class ShowStatus(Enum):
    OPEN = "Open"
    SOLD_OUT = "Sold out"
    CANCELLED = "Cancelled"

from user import User
from customer import Customer
from employee import Employee

try:
    u1 = User("", "user1@mail.com")
    u1.display_info()
except ValueError as e:
    print(e)

try:
    u2 = User("Minnie", "minnie@mail.com")
    u2.display_info()
except ValueError as e:
    print(e)

try:
    c1 = Customer("Lily", "lily@mail.com", 0)
    c1.display_info()
except ValueError as e:
    print(e)

try:
    c2 = Customer("Lily", "lily2@mail.com", 1)
    c2.display_info()
except ValueError as e:
    print(e)

try:
    e1 = Employee("Tom", "tom@mail.com", -3)
    e1.display_info()
except ValueError as e:
    print(e)

try:
    e2 = Employee("Tom", "tom2@mail.com", 1)
    e2.display_info()
except ValueError as e:
    print(e)