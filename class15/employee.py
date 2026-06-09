from user import User

class Employee(User):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.employee_id = employee_id

    @property
    def employee_id(self):
        return self.__employee_id
    
    @employee_id.setter
    def employee_id(self, value):
        if value > 0:
            self.__employee_id = value
        else:
            raise ValueError("employee id should be a positive number")
        
    def display_info(self):
        print(f"Employee's info: Name: {self.name}. Email: {self.email}. Employee id: {self.employee_id}")
