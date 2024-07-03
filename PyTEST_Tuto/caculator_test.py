class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            raise ValueError
        else:
            return self.a / self.b


c1 = Calculator(2, 3)
print(c1.add())
print(c1.sub())
print(c1.mul())
print(c1.div())

import pytest


@pytest.fixture()
def calculator():
    return Calculator(1, 0)


def test_addition(calculator):
    assert calculator.add() == 1


def test_subtract(calculator):
    assert calculator.sub() == 1


def test_multiple(calculator):
    assert calculator.mul() == 20


def test_division(calculator):
    assert calculator.div() == 5


def test_division_error(calculator):
    with pytest.raises(ValueError):
        calculator.div()

