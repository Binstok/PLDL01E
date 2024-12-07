import midterm_quiz_1

obj = midterm_quiz_1.customer_electric_bill_info()
name = input("Name: ")
address = input("Address: ")
account_number = int(input("Account Number: "))
previous_bill = float(input("Previous Bill: "))
rate = input("Rate (Residential or Commercial): ")
date = input("Bill date/Meter reading date: ")
bill_period = input("Bill period: ")
due_date = input("Due date: ")
actual_consumption = float(input("Actual Consumption (Kilowatts): "))
next_meter_reading = input("Next Meter reading: ")
rate_per_kilowatts = float(input("Rate per kilowatts: "))

charges = obj.get_computation_charges(actual_consumption, rate_per_kilowatts)
