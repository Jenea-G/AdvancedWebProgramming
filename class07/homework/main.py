# 1. Create an abstract class:
print("===== 1. Vehicles ===== ")
# Vehicle
# abstract method: move()
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

# Create subclasses:
# Car
# Bicycle

# Each must implement move() differently.
class Car(Vehicle):
    def move(self):
        print("Make sure you have a drivers licence before driving!")

class Bicycle(Vehicle):
    def move(self):
        print("Put on your helmet for safety before taking a ride!")

def commute(vehicle):
    vehicle.move()

car1 = Car()
bicycle1 = Bicycle()

commute(car1)
commute(bicycle1)

# 2. Create an abstract class:
print("===== 2. File Handler ===== ")
# FileHandler
# abstract methods: 
# read()
# write()
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    def write(self):
        pass


# Create subclasses:
# TextFileHandler

class TextFileHandler(FileHandler):
    type = "text"
    def read(self):
        print(f"The {self.type} file was opened with MicrosoftWord")

    def write(self):
        print(f"The changes to the {self.type} file have been successfully registered")

# JsonFileHandler

class JsonFileHandler(FileHandler):
    type = "json"
    def read(self):
        print(f"The {self.type} file was opened in a code editor")

    def write(self):
        print(f"The changes to the {self.type} file have been successfully registered")

textHandler = TextFileHandler()
jsonHandler = JsonFileHandler()

def open(fileHandler):
    fileHandler.read()

def save(fileHandler):
    fileHandler.write()

open(textHandler)
save(textHandler)
open(jsonHandler)
save(jsonHandler)
# They can just print messages instead of reading real files.


# 3. Create an abstract class:
print("===== 3. Account ===== ")
# Account
# abstract method: calculate_fee()
class Account(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass

# Create subclasses:
# SavingsAccount
# PremiumAccount
# Each returns a different fee.

class SavingsAccount(Account):
    type = "savings"

    def __init__(self, holder_name, acc_number, balance):
        self.holder_name = holder_name
        self.acc_number = acc_number
        self.balance = balance
    
    def calculate_fee(self):
        if(self.balance == 0): fee = 5
        if(self.balance < 100): fee = 2
        else: fee = 0
        return fee
    
class PremiumAccount(Account):
    type = "premium"

    def __init__(self, holder_name, acc_number, n_operations):
        self.holder_name = holder_name
        self.acc_number = acc_number
        self.n_operation = n_operations
    
    def calculate_fee(self):
        if(self.n_operation <= 10): fee = 4
        else: fee = 8
        return fee

def show_fee(acc):
    print(f"The monthly fee for {acc.type} account is: {acc.calculate_fee()}$.")

savings1 = SavingsAccount("Leila", 1234, 100)
premium1 = PremiumAccount("Billy", 456, 12)

show_fee(savings1)
show_fee(premium1)

# 4. abstract Employee
print("===== 4. Employee ===== ")
# Create:
# abstract class Employee
# abstract method calculate_salary()
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

# Subclasses:
# FullTimeEmployee
# PartTimeEmployee

# Each should calculate salary differently.
class FullTimeEmployee(Employee):
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def calculate_salary(self):
        salary = self.rate * 8 * 14
        return salary

class PartTimeEmployee(Employee):
    def __init__(self, name, rate, hours_week):
        self.name = name
        self.rate = rate
        self.hours_week = hours_week

    def calculate_salary(self):
        salary = self.hours_week * self.rate * 2
        return salary

def show_salary(e):
    print(f"The salary of {e.name} is {e.calculate_salary()}$ per two weeks.")

employee1 = FullTimeEmployee("Mrs Bloom", 33)
employee2 = PartTimeEmployee("Mr Fruit", 28, 20)

show_salary(employee1)
show_salary(employee2)
# 5. abstract Media
# Create:
# abstract class Media
# abstract method play()

# Subclasses:
# Song
# Video

# Each implements play() differently.