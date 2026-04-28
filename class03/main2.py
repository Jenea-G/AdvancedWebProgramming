class User:
    def __init__ (self, un, email = "N/A"): #default value for email
        self.username = un
        self.email = email

user1 = User("abc", "abc@canada.com")
user2 = User("def")

print(user1.email)
print(user2.email)


# conditions inside of a method
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell_one(self):
        if self.stock > 0:
            self.stock = self.stock - 1
            print(f"sold 1 !! now we have {self.stock} more left")
        else:
            print(f"{self.name} is out of stock")

product1 = Product('mouse', 2)

product1.sell_one()
product1.sell_one()
product1.sell_one()
