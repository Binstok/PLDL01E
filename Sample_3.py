#initialization net income, gross income, total deduction, name of the employee, and pag-ibig contribution
net_income = 0
gross_income = 0
total_deduction = 0
name_of_the_employee = ""
pagibig_contribution = 100

#getting input the name of the employee, rate per hour, hours per day, days per week, weeks per month, sss contribution, philhealth contributiobn, tax contribution
name_of_the_employee = str (input("Enter the name of the employee:"))
rate_per_hour = float(input("Enter the value of rate per hour:"))
hours_per_day = float(input("Enter the value of hours per day:"))
days_per_week = int(input("Enter the value of days per week:"))
weeks_per_month = int(input("Enter the value of weeks per month:"))
sss_contribution = float(input("Enter the value of sss contribution:"))
philhealth_contribution = float(input("Enter the value of philhealth contribution:"))
tax_contribution = float(input("Enter the value of tax contribution:"))

#setting the formula for gross income, total deduction, net income
gross_income = rate_per_hour * hours_per_day * days_per_week * weeks_per_month
total_deduction = sss_contribution + philhealth_contribution + tax_contribution + pagibig_contribution
net_income = gross_income - total_deduction

#display the employee name, net income, gross incomne, total deduction
print("name_of_the_employee:", name_of_the_employee)
print("net_income:", net_income)
print("gross_income:", gross_income)
print("total_deduction:", total_deduction)