from user import User
from customer import Customer
from employee import Employee
from movieshow import MovieShow, ShowStatus, BookingError, InvalidStatusError

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
except InvalidStatusError as e:
    print(e)

try:
    m1 = MovieShow("Interstellar", 0, 0, "something")
except ValueError as e:
    print(e)
except InvalidStatusError as e:
    print(e)

try:
    m1 = MovieShow("Interstellar", 100, 0, "something")
except ValueError as e:
    print(e)
except InvalidStatusError as e:
    print(e)

try:
    m1 = MovieShow("Interstellar", 100, 0, ShowStatus.OPEN)
except ValueError as e:
    print(e)
except InvalidStatusError as e:
    print(e)

print("==== test booking ====")
try:
    m1.book_tickets(c2, 10)
except BookingError as error:
    print(error)

try:
    m1.book_tickets(c2, 5)
except BookingError as error:
    print(error)

m1.display_info()
m1.booked_seats = 96

try:
    m1.book_tickets(c2, 7)
except BookingError as error:
    print(error)

try:
    m1.book_tickets(c2, 4)
except BookingError as error:
    print(error)

try:
    m1.book_tickets(c2, 4)
except BookingError as error:
    print(error)

m1.display_info()

print("=== test cancel show === ")
try:
    m2 = MovieShow("Duna", 200, 0, ShowStatus.OPEN)
    m2.display_info()
except ValueError as e:
    print(e)
except InvalidStatusError as e:
    print(e)

m2.cancels_show()
m2.display_info()

print("Polymorphism")
list = [Customer("Ann", "ann@gmail.com", 2),
        Employee("Peter", "pete@mail.com", 4 ),
        User("Cat", "cat@mail.com"),
        MovieShow("Her", 150, 20, ShowStatus.OPEN)
]

for item in list:
    item.display_info()