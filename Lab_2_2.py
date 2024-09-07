#initialization net income, gross income, total deduction, name of the employee, department, and pag-ibig contribution
net_income = 0
gross_income = 0
total_deduction = 0
department = ""
name_of_the_employee = ""
pagibig_contribution = 100

#getting input the name of the employee, rate per hour, hours per day, days per week, weeks per month, sss contribution, philhealth contributiobn, tax contribution
name_of_the_employee = str(input("Enter the name of the employee:"))
department = str(input("Enter the department:"))
rate_per_hour = float(input("Enter the value of rate per hour:"))
hours_per_day = float(input("Enter the value of hours per day:"))
days_per_week = int(input("Enter the value of days per week:"))
weeks_per_month = int(input("Enter the value of weeks per month:"))

#setting the formula for gross income, total deduction, net income
gross_income = rate_per_hour * hours_per_day * days_per_week * weeks_per_month

#set condition according to the total gross income by the employee and set the formula
if 0 <= gross_income <= 20000:
    total_deduction = 125.75 + 100 + pagibig_contribution
elif 20000 <= gross_income <=50000:
    total_deduction = 2200.50 + 1200 + pagibig_contribution
elif 50000 < gross_income <= 75000:
    total_deduction = 4800 + 6800 + pagibig_contribution
else:
    total_deduction = 5800 + 8800 + pagibig_contribution

#setting the formula for net income
net_income = gross_income - total_deduction

#display the employee name, net income, gross incomne, total deduction
print("Name of the employee:", name_of_the_employee)
print("Department:", department)
print("Total gross income:", gross_income)
print("Total deduction:", total_deduction)
print("Net income:", net_income)
