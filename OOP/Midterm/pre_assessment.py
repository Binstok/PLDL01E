# Base class
class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name
    
    def display_info(self):
        return f'Animal type: {self.type}, Name: {self.name}'

# Derived class (inheritance)
class Birds(Animal):
    def __init__(self, name, type, color):
        super().__init__(type, name)
        self.color = color

    # Overriding display_info method (Polymorphism)
    def display_info(self):
        return f'Bird Name: {self.name}, Bird Type: {self.type}, Color: {self.color}'

# Testing the classes
animal = Animal('Birds', 'Parrot')
bird = Birds('Perry', 'Parrot', 'Red, Blue and Yellow')

print(animal.display_info())  # Display the method from Animals
print(bird.display_info())  # Display the overridden method from Birds