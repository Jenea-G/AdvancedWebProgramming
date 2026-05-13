# 1. identify visibility intent
class User:
    def __init__(self, username, email, password_hash):
        self.username = username # public
        self.__email = email # private - inernal use
        self.__password_hash = password_hash # private - internal use

# which attributes are public? which are intended for internal use?

# 2. redesign the following class to improve encapsulation
class Course:
    def __init__(self, title, seats):
        self.title = title # public
        self.__seats = seats # private, can be changed internally


# 3. Create StudentAccount class:

# public username
# internal __credits
# methods: add_credits() - use_credits() - show_credits()
     
class StudentAccount():
    def __init__(self, username, credits):
        self.username = username
        self.__credits = credits

    def add_credits(self, value):
        if value > 0:
            self.__credits += value
        else:
            print("The entered value is invalid")

    def use_credits(self, value):
        if 0 < value <= self.__credits:
            self.__credits -= value
        else:
            print(f"The entered value is invalid. You cannot use {value} credits.")
    
    def show_credits(self):
        print(f"{self.username} has {self.__credits} credits.")

student_acc1 = StudentAccount("Mary", 50)
student_acc1.use_credits(0)
student_acc1.add_credits(10)
student_acc1.show_credits()

# 4. Create a MovieTicket class:

# public movie_title
# internal available_seats
# methods: book_seat() - cancel_seat() - show_status()

class MovieTicket():
    def __init__(self, movie_title, available_seats):
        self.movie_title = movie_title
        self.__available_seats = available_seats

    def book_seat(self, n):
        if self.__available_seats > n > 0:
            self.__available_seats -= n
            print("The seats are booked successfully")
        else:
            print(f"There are not enough seats to book. You can book only {self.__available_seats} seats.")

    def cancel_seat(self, n):
        if n > 0:
            self.__available_seats -= n
        else:
            print(f"You cannot cansel {n} seats, the value is invalid")

    def show_status(self):
        print(f"There are {self.__available_seats} seats availale for the '{self.movie_title}' movie.")

movie1 = MovieTicket("Interstellar", 100)
movie1.book_seat(210)
movie1.cancel_seat(10)
movie1.show_status()
movie1.book_seat(3)
movie1.show_status()