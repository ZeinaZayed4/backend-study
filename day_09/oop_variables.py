class Employee:
    no_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}_{last.lower()}@email.com"

        Employee.no_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.no_of_employees)

emp_1 = Employee("Zeina", "Zayed", 40000)
emp_2 = Employee("Test", "Employee", 50000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.no_of_employees)
