# Let's create a Product from differet formats

# you are designing a product class

# product class needs:
    #name
    # price
    # category

# the daa to create this class may arrive in 3 different formats:
    # 1. separate constructor arguemnts (__init__)
    # 2. one comma-separated string
    # 3 a dictionary

# you need to design the class so all three fromats can be used cleanly.

# example dictionary:
dict = {
    "name" : "Cake",
    "price": 18,
    "category": "Pastry"
}

# example string:
str = "Pizza,7,Bakery"
# hint --> int(str) converts a string to integer

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    @classmethod
    def from_string(cls, data):
        name, price, category = data.split(",")
        return cls(name, int(price), category)

    @classmethod
    def from_dictionary(cls, data):
        name, price, category = data["name"], data["price"], data["category"]
        return cls(name, price, category)
    
    @classmethod
    def from_name(cls, data):
        return cls(data, 0, "")
    
    def show_product(self):
        print(f"Product name is {self.name}, the price is {self.price}$ and the category is {self.category}")

product1 = Product.from_dictionary(dict)
product2 = Product.from_string(str)
product3 = Product("Apple", 5, "Fruits")
product4 = Product.from_name("Rice")

product1.show_product()
product2.show_product()
product3.show_product()
product4.show_product()