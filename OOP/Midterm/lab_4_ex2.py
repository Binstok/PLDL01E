#Define the class
class SimpleCalculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return 'ERROR'
        return a/b

#Create an instance of the calculator
simplecalculator = SimpleCalculator()

#Test and print results for each operation
print('4 + 4 = ', simplecalculator.add(4, 4))
print('10 - 2 = ', simplecalculator.subtract(10, 2))
print('5 x 5 = ', simplecalculator.multiply(5, 5))
print('4/2 = ', simplecalculator.divide(4, 2))
print('2/0 = ', simplecalculator.divide(2, 0))

