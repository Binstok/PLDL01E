import payroll_oop2

obj = payroll_oop2.Employee_Info()
company = input("Enter Company name: ")
department = input("Enter Employee Department: ")
employee_name = input("Enter Employee Name: ")
employee_code = input("Enter Employee Number or code: ")
salary_cutoff = input("Enter Salary Cut Off: ")
emp_data = obj.get_emp_data(company, department, employee_name, employee_code, salary_cutoff)

#data entry for basic pay computation
obj2 = payroll_oop2.Employee_Salary()
rate_pay = float(input("Enter Employee rate per hour: "))
number_working_hours = float(input("Enter employee number of working hours: "))
honorarium_pay = float(input("Enter honorarium pay: "))
number_absences = float(input("Enter number of absences in hours: "))

#compute for basic pay
basic_pay = obj2.get_basic_pay(rate_pay, number_working_hours)
absences_deduction = obj2.get_absences_deduction(rate_pay, number_absences)

#dispaly of output
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
obj.display_data()
print("Basic Pay: %.2f" % basic_pay)
print("Honorarium Pay: %.2f" % honorarium_pay)
print("Employee absences deduction: %.2f" % absences_deduction)
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
