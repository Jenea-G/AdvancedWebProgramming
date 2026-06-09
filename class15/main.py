MAX_TICKETS_PER_BOOKING = 3

from user import User
from customer import Customer
from employee import Employee
from movieshow import MovieShow, ShowStatus

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

print("=== Movie tesing ===")
try:
    m1 = MovieShow("  ", 1, 0, ShowStatus.OPEN)
except ValueError as e:
    print(e)

try:
    m1 = MovieShow("Interstellar", 0, 0, "something")
except ValueError as e:
    print(e)

try:
    m1 = MovieShow("Interstellar", 100, 0, "something")
except ValueError as e:
    print(e)

try:
    m1 = MovieShow("Interstellar", 100, 0, ShowStatus.OPEN)
except ValueError as e:
    print(e)