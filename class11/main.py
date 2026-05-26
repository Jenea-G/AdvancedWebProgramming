# Enums and Constants in Application Design

# ===  A constant === is a value that should not change during the program.
# Python does not enforce contants strictly, but by convention we write then in uppercase:
MAX_STUDENTS = 30
DEFAULT_CREDITS = 3
STATUS_OPEN = "open"

# this tells other programmers that this value should be treated as fixed

# === An Enum === is a special type used to define a fixed set of named values.

from enum import Enum
class Status(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"

# now the allowed values are much clearer and more controlled.

# We use enums insted of plain strings to:

#   make allowed values explicit
#   improve readability
#   reduce spelling mistakes
#   make validation easier
#   improve program design

# Constants used for:
#   - one fixed number
#   - one repeated fixed string
#   - configuration values

MAX_CAPACITY = 40

# Enums used for:
#   - one variable that must be chosen from a known set of options
class CourseStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"

# ======= EXAMPLES ==========

STATUS_OPEN = "open"
STATUS_CLOSED = "closed"
STATUS_CANCELLED = "cancelled"

status = STATUS_OPEN
print(status)
class CourseStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"

status = CourseStatus.OPEN
print(status)
print(status.value)

# Ex C - comparison - this is clearer and safer than comparing to loose strings.
if status == CourseStatus.OPEN:
    print("Registration is allowed.")

from enum import Enum

# Ex D - loop through enum values
class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

for priority in Priority:
    print(priority, priority.value)
# This is useful when you want to show all allowed choices.