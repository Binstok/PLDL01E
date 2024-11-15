import review


obj = review.screen_display

name = str(input("Name: "))
address = input("Address: ")
gender = str(input("Gender (M or F): "))
age = int(input("Age: "))

obj2 = review.payment
bill = float(input("Bill: "))
payment = float(input("Payment: "))
service_charge = float(input("Service Charge: "))


total_bill = bill + service_charge
change = payment - total_bill

print("")
print("=============================================================")
print("Name: ", name, "\t\t\t\t\t\t\t Address: ", address )
print("Gender", gender, "\t\t\t\t\t\t Age: ", age)
print("=============================================================")
print("=============================================================")
print("Payment: ", payment)
print("Bill: ", bill)
print("Service Charge: ", service_charge)
print("=============================================================")
print("Total bill: ", total_bill)
print("Change: ", change)
print("=============================================================")
