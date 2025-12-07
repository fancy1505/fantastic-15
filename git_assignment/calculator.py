import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot compute square root of negative number")
        return math.sqrt(a)

if __name__ == "__main__":
    calculator = Calculator()

    number1 = 16
    number2 = 4

    print("Addition:", calculator.add(number1, number2))
    print("Subtraction:", calculator.subtract(number1, number2))
    print("Multiplication:", calculator.multiply(number1, number2))
    print("Division:", calculator.divide(number1, number2))
    print("Square Root:", calculator.square_root(number1))
