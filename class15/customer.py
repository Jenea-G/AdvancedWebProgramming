from user import User

class Customer(User):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.customer_id = customer_id

    @property
    def customer_id(self):
        return self.__customer_id
    
    @customer_id.setter
    def customer_id(self, value):
        if value > 0:
            self.__customer_id = value
        else:
            raise ValueError("Customer id should be a positive number")
        
    def display_info(self):
        print(f"Customer's info: Name: {self.name}. Email: {self.email}. Customer id: {self.customer_id}")

class VIPCustomer(Customer):
    status = "VIP"

    def __init__(self, name, email, customer_id):
        super().__init__(name, email, customer_id)

    def display_info(self):
        super().display_info()
        print(f"{self.name} is a {self.status} customer.")