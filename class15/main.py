MAX_TICKETS_PER_BOOKING = 3

from enum import Enum
class ShowStatus(Enum):
    OPEN = "Open"
    SOLD_OUT = "Sold out"
    CANCELLED = "Cancelled"