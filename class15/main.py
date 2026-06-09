MAX_TICKETS_PER_BOOKING = 3

from enum import Enum
class ShowStatus(Enum):
    OPEN = "Open"
    SOLD_OUT = "Sold out"
    CANCELLED = "Cancelled"

from user import User

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
