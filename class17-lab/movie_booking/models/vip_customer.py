from models.customer import Customer

class VipCustomer(Customer):
    def __init__(self, name, discount):
        super().__init__(name)
        self.discount = discount

    def display_info(self):
        print(f"Vip customer: {self.name} | Discount: {self.discount}")