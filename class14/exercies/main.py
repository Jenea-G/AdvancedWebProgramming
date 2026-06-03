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