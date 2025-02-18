#class
class Car:
#initialize
    def __init__(self, brand, year, model, engine):
        self.brand = brand
        self.year = year
        self.model = model         #value holder
        self.engine = engine

 #display function
    def display_car_info(self):
        print(f'Brand: {self.brand}, Year: {self.year}, Model: {self.model}, Engine: {self.engine}')

#initialize object for class car
car1 = Car('Toyota', 2024, 'Fortuner', 'Diesel')
car2 = Car('Mitsubishi', 2025, 'Montero', 'Diesel')
car3 = Car('Honda', 2022, 'Civic', 'Gas')
car4 = Car('Mitsubishi', 2023, 'Xpander', 'Gas')

#call to display car info
car1.display_car_info()
print('=========================================================================')
car2.display_car_info()
print('=========================================================================')
car3.display_car_info()
print('=========================================================================')
car4.display_car_info()

