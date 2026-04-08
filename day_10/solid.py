from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, item, quantity, price):
        self.items.append(item)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i, _ in enumerate(self.prices):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuth(Authorizer):
    authorized = False

    def verify_code(self, code):
        print(f"Verifying code: {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
    

class NotARobot(Authorizer):
    authorized = False

    def not_a_robot(self):
        print("Are you a robot?!")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized.")
        print("Processing debit payment type...")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type...")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type...")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Laptop", 1, 50000)
order.add_item("Ipad", 1, 40000)
order.add_item("Mouse", 2, 1000)

print(f"Total price: E£{order.total_price()}")

authorizer = NotARobot()
processor = DebitPaymentProcessor("123456", authorizer)
authorizer.not_a_robot()
processor.pay(order)
