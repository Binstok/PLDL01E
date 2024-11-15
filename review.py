class screen_display:

    def __init__(self):
        self.name = ""
        self.address = ""
        self.gender = ""
        self.age = 0

    def get_info(self, name, address, gender, age):
        self.name = name
        self.address = address
        self.gender = gender
        self.age = age

    def display_info(self):
        print("Name: ", self.name)
        print("Adress: ", self.address)
        print("Gender: ", self.gender)
        print("Age: ", self.age)

class payment:

    def __init__(self):
        self.bill = 0
        self.payment = 0
        self.service_charge = 0
        self.change = 0

    def get_payment(self, bill, payment, service_charge):
        self.bill = bill
        self.payment = payment
        self.service_charge = service_charge

    def display_payment (self):
        print("Bill: ", self.bill)
        print("Payment: ", self.payment)
        print("Service Charge", self.service_charge)


    def computation_total_bill(self):
        self.total_bill = self.bill + self.service_charge

    def computation_change (self):
        self.change = self.payment - self.total_bill
