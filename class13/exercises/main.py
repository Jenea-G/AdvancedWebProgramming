# 1
# Create a parent class:

#   Animal
#   method: speak()

# then child classes:
#   Dog
#   Cat
# Override speak in ceach child!
# Dog says "Woof"
# Cat says "Meow"
# Then loop through them polymorphically

print("===== Ex 1 ======")
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Cat says 'Meow'")

class Dog(Animal):
    def speak(self):
        print("Dog says 'Woof'")

animals = [Cat(), Dog(), Animal()]

for animal in animals:
    animal.speak()

print()
print("===== Ex 2 ======")
# 2
# Create a parent class: Vehicle
# Child classes Car and Bike

# the share 
# brand
# describe()

# add child-specific behaviour

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def describe(self):
        print(f"Vehile's brand is {self.brand}")

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def describe(self):
        print(f"The car's brand is {self.brand}")

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def describe(self):
        print(f"The bike's brand is {self.brand}")

vehicles = [Vehicle("Ford"), Car("Kia"), Bike("Rocky Mountain")]
for vehicle in vehicles:
    vehicle.describe()

# 3
# parent class: Account
#               show_type()

# children accounts: SavingsAccount & PremiumAccount
#   override or extend behaviour accordingly
print()
print("===== Ex 3 ======")


class Account:
    def show_type(self):
        print("This is a bank account")

class SavingsAccount(Account):
    def show_type(self):
        super().show_type()
        print("of type savings")

class PremiumAccount(Account):
    def show_type(self):
        print("This is a premium account")

accounts = [Account(), SavingsAccount(), PremiumAccount()]

for account in accounts:
    account.show_type()