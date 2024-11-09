class customer_electric_bill_info:
#initialize customer info
    def __init__(self):
        self.name = ""
        self.address = ""
        self.account_number = 0
        self.previous_bill = 0
        self.previous_bill_output = ""
        self.rate = ""
        self.date = ""
        self.bill_period = ""
        self.due_date = ""
        self.actual_consumption = 0
        self.next_meter_reading = ""
        self.rate_per_kilowatts = 0
#Get customer data
    def get_customer_data(self, name, address, account_number, previous_bill, rate, date, bill_period, due_date, actual_consumption, next_meter_reading, rate_per_kilowatts):
        self.name = name
        self.address = address
        self.account_number = account_number
        self.previous_bill = previous_bill
        self.rate = rate
        self.date = date
        self.bill_period = bill_period
        self.due_date = due_date
        self.actual_consumption = actual_consumption
        self.next_meter_reading = next_meter_reading
        self.rate_per_kilowatts = rate_per_kilowatts
#Initialize Customer billing statement
class customer_billing_statement:
    def __init__(self):
        self.generation = 0
        self.transmission = 0
        self.system_loss = 0
        self.distribution = 0
        self.subsidies = 0
        self.government_taxes = 0
        self.universal_charges = 0
        self.fitall = 0
        self.applied_credits = 0
        self.other_charges = 0
        self.installment_due = 0
#Get billing statement
    def get_billing_statement(self, generation, transmission, system_loss, distribution, subsidies, government_taxes, universal_charges, fitall, applied_credits, other_charges, installment_due):
        self.generation = generation
        self.transmission = transmission
        self.system_loss = system_loss
        self.distribution = distribution
        self.subsidies = subsidies
        self.government_taxes = government_taxes
        self.universal_charges = universal_charges
        self.fitall = fitall
        self.applied_credits = applied_credits
        self.other_charges = other_charges
        self.installment_due = installment_due

#Set the condition in balance previous billing
    def balance_previous_billing(self):
        if self.previous_bill == 0:
            self.previous_bill_output = print("Thank you")
        else:
            self.previous_bill_output = print("Pleas pay")
#Set the computation for charges
    def computation_charges(self):
        self.charges = self.actual_consumption * self.rate_per_kilowatts
#Set the computation for the total amount
    def computation_total_amount(self):
        self.total_amount = self.previous_bill + self.charges



