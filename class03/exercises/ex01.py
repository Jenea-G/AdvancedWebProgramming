# create a class of fruit
    # give it three attributes (1 should be price)
    # define 3 methods that access the attributes and return them
    # define a method that changes the price to new price (taken as an parameter)

class Fruit:
    def __init__ (self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def describe(self): # this is a getter
        return f"{self.name} costs {self.price}$, there are {self.stock} in stock"
    
    def sell(self, quantity):
        if (quantity > self.stock): return f"Not enough in stock, you can sell only {self.stock}"
        new_stock = self.stock - quantity
        self.stock = new_stock
        return new_stock
    
    def set_price(self, new_price): # this is a setter
        self.price = new_price
        return self.price


fruit1 = Fruit("banana", 30, 4)
print(fruit1.sell(5))
print(fruit1.sell(2))
print(fruit1.sell(3))

fruit2 = Fruit("durian", 10, 3)
fruit3 = Fruit("apple", 5, 20)

fruits = [fruit1, fruit2, fruit3]

fruit3.set_price(4)

for fruit in fruits:
    print(fruit.describe())