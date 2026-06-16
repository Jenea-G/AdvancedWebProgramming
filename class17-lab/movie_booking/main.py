from core.constants import MAX_TICKETS_PER_BOOKING
from core.enums import ShowStatus
from core.exceptions import InvalidBookingError
from models.customer import Customer
from models.movie_show import MovieShow
from models.staff import Staff
from models.vip_customer import VipCustomer
from utils import separator, display

def main():
    customer = Customer("Ava")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)

    customer.display_info()
    show.display_info()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)

    separator()
    print("Challenges")
    separator()
    employee = Staff("Kevin", "Technician")
    employee.display_info()

    separator()
    objects = [
        Customer("My customer"), MovieShow("The movie", 15, ShowStatus.OPEN), Staff("Lily", "Operator"), VipCustomer("Thomas", 0.2)
    ]
    display(objects)

if __name__ == "__main__":
    main()
