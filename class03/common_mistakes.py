# mistake 1 -- forgetting self

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell_one(self): # WE NEED TO PASS SELF AS A PARAMETER, ALWAYS!!
        self.stock -= 1


# mistake 2 -- forgeting self for attributes!

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell_one(self):
        stock -= 1 #if you dont put self. before attribute name it wont recognize it

    def get_name(self):
        print(self.name) # is for quick demonstration
        return(self.name) # is for using it somewhere or doing smth with it

p = Product ("test", 1)
print(p.stock)
p.sell_one()