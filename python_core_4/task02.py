class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


calculator = Calculator()
print(calculator.add(10, 5) == 15)
print(calculator.subtract(10, 5) == 5)
print(calculator.multiply(10, 5) == 50)
print(calculator.divide(10, 5) == 2)
