class Car:

    def __init_(self):
        self.brand = ''
        self.model = ''
        self.year = 0
        self.engine = ''

    def get_car_data(self):
        self.brand = str(input('Brand: '))
        self.model = str(input('Model: '))
        self.year = int(input('Year: '))
        self.engine = str(input('Engine: '))

    def display_car_data(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Engine: {self.engine}')

emp = Car()
emp.get_car_data()
emp.display_car_data()