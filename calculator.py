# calculator.py (updated with factorial and fibonacci implementations)
print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        if b < 0:
            return 1 / (a ** abs(b))
        return a ** b

    def crap_function(self):
        pass

    def factorial(self, n):
        """Calculate the factorial of n"""
        if not isinstance(n, int):
            raise ValueError("Factorial input must be an integer")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def fibonacci(self, n):
        """Return the nth Fibonacci number"""
        if not isinstance(n, int):
            raise ValueError("Fibonacci input must be an integer")
        if n < 0:
            raise ValueError("Fibonacci number is not defined for negative numbers")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b