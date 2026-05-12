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
# Account
# abstract method: calculate_fee()

# Create subclasses:
# SavingsAccount
# PremiumAccount

# Each returns a different fee.


# 4. abstract Employee
# Create:
# abstract class Employee
# abstract method calculate_salary()

# Subclasses:
# FullTimeEmployee
# PartTimeEmployee

# Each should calculate salary differently.

# 5. abstract Media
# Create:
# abstract class Media
# abstract method play()

# Subclasses:
# Song
# Video

# Each implements play() differently.