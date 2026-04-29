class Employee:
    bonus = 0.25
    base_salary = 500

    def __init__ (self, name, sales_count):
        self.name = name
        self.sales_count = sales_count

    def salary(self):
        base_salary = Employee.base_salary
        bonus = Employee.bonus
        
        if self.sales_count > 10:
            salary = base_salary + self.sales_count * bonus
            return salary
        else:
            return base_salary
        
employee1 = Employee("Kelly", 12)
employee2 = Employee("Bob", 6)

print(employee1.salary())
print(employee2.salary())