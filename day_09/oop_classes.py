class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}_{last.lower()}@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee("Zeina", "Zayed", 40000)
emp_2 = Employee("Test", "Employee", 50000)

print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(emp_2.email)
