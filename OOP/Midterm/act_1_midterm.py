# Base class
class Animal:
    def speak(self):
        return "Animal sound"

# Derived class inheriting from Animal
class Dog(Animal):
    def bark(self):
        return "Woof!"

# Create an instance of Dog
dog = Dog()
print(dog.speak())  # Output: Animal sound
print(dog.bark())   # Output: Woof!

print('')

# First base class
class Crawl:
    def crawl(self):
        return 'I can crawl'

# Second base class
class Run:
    def run(self):
        return 'I can run'

# Derived class inheriting from both crawl and run
class Crocodile(Crawl, Run):
    def growls(self):
        return 'Growls'

# Create an instance of crocodile
crocodile = Crocodile()
#Display the output
print(crocodile.run())
print(crocodile.crawl())
print(crocodile.growls())

print ('')

#First class
class Animal:
    def speak(self):
        return 'Sound of Dog and Cat'

#Second class for dog
class Dog(Animal):
    def dog_sound(self):
        return 'Bark'

#Third class for Cat
class Cat(Animal):
    def cat_sound(self):
        return 'Meow'

# Create an instance of crocodile
dog = Dog()
cat = Cat()
#display the output
print(dog.speak())
print(dog.dog_sound())
print(cat.cat_sound())
