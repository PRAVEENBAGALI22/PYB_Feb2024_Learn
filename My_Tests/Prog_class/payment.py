# this is program for method overriding
# payment method is set to pass which gets 


class Payment:
    def __init__(self, amount):
        self.amount = amount

    def payment_method(self):
        pass


class Creditcard(Payment):
    def payment_method(self):
        return f"Payment done from Credit card of {self.amount} "


class Debitcard(Payment):
    def payment_method(self):
        return f"Payment done from Debit card of {self.amount} "


c1 = Creditcard(50)
print(c1.payment_method())
print(c1.amount)

d1 =Debitcard(100)
print(d1.payment_method())
print(d1.amount)