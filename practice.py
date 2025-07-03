from abc import ABC, abstractmethod


class Operation(ABC):

    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(Operation):
    def execute(self, a, b):
        return a + b


class Devide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль!")
        return a / b


class Subtraction(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Calculator:
    def __init__(self, operation: Operation):
        self.operation = operation

    def calculate(self, a, b):
        return self.operation.execute(a, b)


calculator = Calculator(Addition())
print(calculator.calculate(5, 3))
