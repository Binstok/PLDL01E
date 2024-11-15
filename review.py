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

class payment:

    def __init__(self):
        self.payment = 0
        self.bill = 0
        self.service_charge = 0
        self.change = 0

    def get_payment(self, bill, service_charge, payment):
        self.payment = payment
        self.bill = bill
        self.service_charge = service_charge


    def computation_total_bill(self):
        self.total_bill = self.bill + self.service_charge

    def computation_change (self):
        self.change = self.payment - self.total_bill
