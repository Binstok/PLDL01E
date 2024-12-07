import midterm_exam

#data entry for service information
obj = midterm_exam.Service_Information()
soa = int(input("SOA: "))
statement_of_account_for_the_month_of = input("STATEMENT OF ACCOUNT For the month of: ")
contract_number = int(input("Contract Account No.: "))
account_name = str(input("Account name: "))
service_address = input("Service Address: ")
tin = input("TIN: ")
rate_class = str(input("Rate Class (Residential/Commercial): "))
business_area = input("Business Area: ")
customer_info = obj.get_customer_info(soa, statement_of_account_for_the_month_of, contract_number, account_name, service_address,tin, rate_class, business_area)

#data entry for metering information and billing summary
obj2 = midterm_exam.Metering_Information_Billing_Summary()
meter_number = input("Meter No.: ")
mru_number = int(input("MRU No.: "))
seq_number = input("Seq No.: ")
reading_date = input("Reading Date: ")
present_reading = int(input("Present Reading: "))
previous_reading = int(input("Previous Reading: "))
consumption = float(input("Consumption (cu.m): "))
previous_consumption = int(input("Previous Months Consumption: "))
maintenance_service_charge = float(input("Maintenance Service Charge: "))
payment_due_date = input("Payment Due Date: ")

#Computation for basic charge, environmental charges, total current charges before tax, government tax, current charges
basic_charge = obj2.get_basic_charge(consumption)
environmental_charges = obj2.get_environmental_charges(basic_charge)
total_current_charges_before_tax = obj2.get_total_current_charges_before_tax(basic_charge, environmental_charges, maintenance_service_charge)
government_tax = obj2.get_government_tax(total_current_charges_before_tax)
current_charges = obj2.get_total_amount_due(total_current_charges_before_tax, government_tax)
matering_information_summary = obj2.get_metering_information_billing_summary(meter_number, mru_number, seq_number, reading_date, present_reading, previous_reading, consumption, previous_consumption, maintenance_service_charge, payment_due_date, basic_charge, environmental_charges, total_current_charges_before_tax, government_tax, current_charges, payment_due_date)

#Display all the data needed
obj.display_customer_info()
print("------------------------------------------------------------------------------------------------------")
obj2.display_matering_information_billing_summery()
print("Current Charges: %.2f" % current_charges)
print("Basic Charge: %.2f" % basic_charge)
print("Environmental Charges (20% of Basic Charge): ", environmental_charges)
print("Maintenance Service Charge (MSC): ", maintenance_service_charge)
print("Total Current Charges Before Taxes: %.2f" % total_current_charges_before_tax)
print("Government Taxes: %.2f" % government_tax)
print("------------------------------------------------------------------------------------------------------")
print("TOTAL AMOUNT DUE: %.2f" % current_charges)
print("PAYMENT DUE DATE: ", payment_due_date)
print("------------------------------------------------------------------------------------------------------")


