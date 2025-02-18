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

    def display_customer_data(self):
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("")
        print("=================================================================================================")
        print("Elertic Bill")
        print("Summary for Customer Account Number (CAN): ", self.account_number)
        print("=================================================================================================")
        print("Balance From Previous Billing")
        print(self.previous_bill)
        if self.previous_bill == 0:
            previous_bill_output = print("Thank you")
        else:
            previous_bill_output = print("Please pay")
        print("=================================================================================================")
        print("Current Charges: ")
        print("Amount due: ", self.total_amount)
        print("Due Date: ", self.due_date)
        print("Total Amount Due: ", self.total_amount)
        print("")
        print("=================================================================================================")
        print("Service Info: ")
        print("Servince ID Number: ", self.account_number)
        print("Rate: ", self.rate)
        print("Contract in the name of: ", self.name)
        print("Servince Address: ", self.address)
        print("=================================================================================================")
        print("Billing Info")
        print("Bill Date: ", self.date)
        print("Meter Reading Date: ", self.date)
        print("Bill Period: ", self.bill_period)
        print("Due Date: ", self.due_date)
        print("Total KWH: ", self.actual_consumption)
        print("Total current amount: ", self.total_amount)
        print("Next Meter Reading: ", self.next_meter_reading)
        print("=================================================================================================")
        print("Customer Account Number: ", self.account_number, "\t\t\t\t\t\tDue Date: ", self.due_date)
        print("=================================================================================================")
        print("Please Pay")
        print(self.total_amount)

    def get_computation_charges(self):
        self.charges = self.actual_consumption * self.rate_per_kilowatts

        # Set the computation for the total amount
    def get_computation_total_amount(self):
        self.total_amount = self.previous_bill + self.charges

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

    def display_billing_statement(self):
        print("=================================================================================================")
        print("Bill Consumption Summary")
        print("Remaining Balance From Previous Bill: ", self.previous_bill)
        print("Generation: ", self.generation)
        print("Transmission: ", self.transmission)
        print("System Loss: ", self.system_loss)
        print("Disbribution (Meralco): ", self.distribution)
        print("Subsidies: ", self.subsidies)
        print("Government Taxes: ", self.government_taxes)
        print("Universal Charges: ", self.universal_charges)
        print("FiT-All (Renewable): ", self.fitall)
        print("Applied Credits: ", self.applied_credits)
        print("Other Charges: ", self.other_charges)
        print("Installment Due: ", self.installment_due)
        print("=================================================================================================")
        print("Total Amount Due: ", self.total_amount)


#Set the condition in balance previous billing
    def get_balance_previous_billing(self):
        if self.previous_bill == 0:
            self.previous_bill_output = print("Thank you")
        else:
            self.previous_bill_output = print("Please pay")
#Set the computation for charges
    def get_computation_charges(self, actual_consumption, rate_per_kilowatts):
        self.charges = actual_consumption * rate_per_kilowatts
        return self.charges
#Set the computation for the total amount
    def get_computation_total_amount(self):
        self.total_amount = self.previous_bill + self.charges



