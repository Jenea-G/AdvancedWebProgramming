class Employee:
    bonus = 0.25
    base_salary = 500
    company_name = "Creators"

    def __init__ (self, name, sales_count):
        self.name = name
        self.sales_count = sales_count

    def calc_salary(self):
        salary = self.base_salary

        if self.sales_count > 10:
            salary = salary + self.sales_count * self.bonus
        return salary
        
employee1 = Employee("Kelly", 12)
employee2 = Employee("Bob", 6)

print(employee1.calc_salary())
print(employee2.calc_salary())

print("new base salary 1000")
Employee.base_salary = 1000

print(employee1.calc_salary())
print(employee2.calc_salary())