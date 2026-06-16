from core.constants import MAX_TICKETS_PER_BOOKING
from core.enums import ShowStatus
from core.exceptions import InvalidBookingError
from models.customer import Customer
from models.movie_show import MovieShow
from models.staff import Staff
from utils import separator

def main():
    customer = Customer("Ava")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)
    employee = Staff("Kevin", "Technician")

    customer.display_info()
    show.display_info()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)

    separator()
    print("Challenges")
    separator()
    employee.display_info()

if __name__ == "__main__":
    main()
