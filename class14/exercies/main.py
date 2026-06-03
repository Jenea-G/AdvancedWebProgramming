# 1
# Create a class with:
#   private balance
#   deposit(amount)
#   withdraw(amount)

# use exceptions for:
#   negative deposit
#   negative withdrawal
#   insufficient funds
class DepositError(Exception):
    pass
class NegativeWithdrawalError(Exception):
    pass
class InsufficientFundslError(Exception):
    pass

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, name):
        if not name.strip():
            raise ValueError("Owner's name cannot be empty")
        self.__owner = name

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance should be more or equal to 0")
        self.__balance = value

    def deposit(self, amount):
        if amount < 0:
            raise DepositError("The amount to deposit should be a positive number")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeWithdrawalError("The amount to withdraw should be a positive number")
        if amount > self.balance:
            raise InsufficientFundslError("There are not enough money on your account.")
        self.balance -= amount

try:
    acc1 = Account("", 300)
except ValueError as error:
    print("The account was't created: ", error)
else:
    print(f"The account for {acc1.owner} was successfully created")

try:
    acc1 = Account("Amy", 300)
except ValueError as error:
    print("The account was't created: ", error)
else:
    print(f"The account for {acc1.owner} was successfully created")

try:
    acc1.deposit(-50)
except DepositError as error:
    print("The deposit operation failed:", error)
else:
    print(f"The deposit operation succeded. You have ${acc1.balance} on your account")

try:
    acc1.withdraw(-90)
except NegativeWithdrawalError as error:
    print("The withdrawal operation failed:", error)
except InsufficientFundslError as error:
    print("The withdrawal operation failed:", error)
else:
    print(f"The withdrawal operation succeded. You have ${acc1.balance} left on your account")
# finally:
#     print("Operation completed")

# 2
print()
print("====== Exercise 2 =====")

# Create a class with:
# property Celcius

# Raise an exception if:
# temperature is below absolute zero
class Temperature:
    def __init__(self, temp):
        self.temperature = temp
    
    @property
    def temperature(self):
        return self.__temp
    
    @temperature.setter
    def temperature(self, value):
        if -273.15 > value:
            raise ValueError("Temperature cannot be below absolute zero")
        self.__temp = value

try:
    t1 = Temperature(-300)
except ValueError as error:
    print(error)
else:
    print(f"Temperature is {t1.temperature}")

# 3
print()
print("====== Exercise 3 =====")
# Create:
# Class NegativePriceError(Exception):
# pass

# Then use it in a product class.

class NegativePriceError(Exception):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise NegativePriceError("The price cannot be negative")
        self.__price = value

    def setPrice(self, value):
        self.price = value

try:
    p1 = Product("Mouse", -5)
except NegativePriceError as error:
    print(error)
else:
    print(f"The product {p1.name} was successfully added")

try:
    p2 = Product("Headset", 55)
except NegativePriceError as error:
    print(error)
else:
    print(f"The product {p2.name} was successfully added")

try:
    p2.setPrice(60)
except NegativePriceError as error:
    print(error)
else:
    print(f"The price of {p2.name} was successfully updated and is now {p2.price}$")