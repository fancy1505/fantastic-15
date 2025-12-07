import math

class Calculator:
    def add( self , a, b) :
        return a + b
    def substract( self, a,b) :
        return a - b
    def multiply( self , a,b) :
        return a * b
    def divide(self , a,b) :
        if b ==0 :
            raise ValueError("Cannot divide by zero")
        return a/b
    def square_root(self ,a) :
        if a < 0 :
            raise ValueError("Cannot compute square root of negative number")
        return math.sqrt(a)
    if __name__ == " __main__" :
        Calculator = Calculator()

        number1= 16
        number2 = 4
        print("Addition:", Calculator.add(number1,number2))
        print("Subtraction:",Calculator.substract(number1,number2))
        print("Multiplication:",Calculator.multiply(number1,number2))
        print("Division:",Calculator.divide(number1,number2))
        print("Square Root:",Calculator.sqaure_root(number1))