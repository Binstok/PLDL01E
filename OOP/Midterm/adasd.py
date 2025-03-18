# Base class
class Animal:
    def __init__(self, type, name):  # Corrected the method name to __init__
        self.type = type
        self.name = name

    def display_info(self):
        return f'Animal type: {self.type}, Name: {self.name}'

# Derived class (inheritance)
class Birds(Animal):
    def __init__(self, name, type, color):  # Corrected the method name to __init__
        super().__init__(type, name)  # Corrected the method name to __init__
        self.color = color

    # Overriding display_info method (Polymorphism)
    def display_info(self):
        return f'Bird Name: {self.name}, Bird Type: {self.type}, Color: {self.color}'

# Testing the classes
abc = Animal('Birds', 'Parrot')
egh = Birds('Perry', 'Parrot', 'Red, Blue and Yellow')

print(abc.display_info())  # Display the method from Animals
print(egh.display_info())  # Display the overridden method from Birds