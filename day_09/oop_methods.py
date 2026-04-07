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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() in [4, 5]:
            return False
        return True


def main():
    emp_1 = Employee("Zeina", "Zayed", 40000)
    emp_2 = Employee("Test", "Employee", 50000)

    import datetime

    my_date = datetime.date(2026, 4, 6)
    print(Employee.is_workday(my_date))


if __name__ == "__main__":
    main()
