#initialize
company_name = ""
employee_code = 0
employee_name = ""
department = ""
cut_off = 0
pay_period = 0
basic_pay = 0
overtime = 0
absences = 0
honorarium = 0
tardy = 0
withholding_tax = 0
sss_contribution = 0
hdmf_contribution = 100
philhealth_contribution = 0
deduction = 0
gross_earnings = 0
net_pay = 0

#Input the company name, employee code and name, department, cut off, rate per hour, hours per day, overtime pay, absent per day, honorarium, hours of tardiness
company_name = str(input("Company name:"))
employee_code = float (input("Employee code:"))
employee_name = str(input("Employee name:"))
department = str(input("Department:"))
cut_off = float (input("Cut off:"))
rate_per_hour = float(input("Rate per hour:"))
hours_per_day = float(input("Hours per day:"))
hours_overtime_per_day = float(input("Hours overtime per day:"))
hours_absent_per_day = float(input("Hours absent per day:"))
honorarium_number_hours = float(input("honorarium:"))
hours_of_tardiness = float(input("Hours of tardiness:"))

#Set the forumla for basic pay, overtime, absences, honorarium, tardy, gross earnings
basic_pay = rate_per_hour * hours_per_day
overtime = hours_overtime_per_day * rate_per_hour
absences = hours_absent_per_day * rate_per_hour
honorarium = honorarium_number_hours * rate_per_hour
tardy = hours_of_tardiness * rate_per_hour
gross_earnings = basic_pay + overtime + honorarium

#Set the condition according to the gross earnings
if 0 <= gross_earnings < 4250:
    sss_contribution = 180
elif 4250 <= gross_earnings < 4750:
    sss_contribution = 202.50
elif 4750 <= gross_earnings < 5250:
    sss_contribution = 225
elif 5250 <= gross_earnings < 5750:
    sss_contribution = 247.50
elif 5750 <= gross_earnings < 6250:
    sss_contribution = 270
elif 6250 <= gross_earnings < 6750:
    sss_contribution = 292.50
elif 6750 <= gross_earnings < 7250:
    sss_contribution = 315
elif 7250 <= gross_earnings < 7750:
    sss_contribution = 337.50
elif 7750 <= gross_earnings < 8250:
    sss_contribution= 360
elif 8250 <= gross_earnings < 8750:
    sss_contribution = 382.50
elif 8750 <= gross_earnings < 9250:
    sss_contribution = 405
elif 9250 <= gross_earnings < 9750:
    sss_contribution = 427.50
elif 9750 <= gross_earnings < 10250:
    sss_contribution = 450
elif 10250 <= gross_earnings < 10750:
    sss_contribution = 472.50
elif 10750 <= gross_earnings < 11250:
    sss_contribution = 495
elif 11250 <= gross_earnings < 11750:
    sss_contribution = 517.50
elif 11750 <= gross_earnings < 12250:
    sss_contribution = 540
elif 12250 <= gross_earnings < 12750:
    sss_contribution = 562.50
elif 12750 <= gross_earnings < 13250:
    sss_contribution = 585
elif 13250 <= gross_earnings < 13750:
    sss_contribution = 607.50
elif 13750 <= gross_earnings < 14250:
    sss_contribution = 630
elif 14250 <= gross_earnings < 14750:
    sss_contribution = 652.50
elif 14750 <= gross_earnings < 15250:
    sss_contribution = 675
elif 15250 <= gross_earnings < 15750:
    sss_contribution = 697.50
elif 15750 <= gross_earnings < 16250:
    sss_contribution = 720
elif 16250 <= gross_earnings < 16750:
    sss_contribution = 742.50
elif 16750 <= gross_earnings < 17250:
    sss_contribution = 765
elif 17250 <= gross_earnings < 17750:
    sss_contribution = 787.50
elif 17750 <= gross_earnings < 18250:
    sss_contribution = 810
elif 18250 <= gross_earnings < 18750:
    sss_contribution = 832.50
elif 18750 <= gross_earnings < 19250:
    sss_contribution = 855
elif 19250 <= gross_earnings < 19750:
    sss_contribution = 877.50
else:
    sss_contribution = 900

#Set the condition according to the gross earnings
if gross_earnings == 10000:
    philhealth_contribution = 500
elif 10000 < gross_earnings < 100000:
    philhealth_contribution = gross_earnings * 0.05
elif gross_earnings == 100000:
    philhealth_contribution = 5000
else:
    philhealth_contribution = 0

#Set the condition according to the gross earnings
if 0 < gross_earnings < 20833:
    withholding_tax = 0
elif 20833 <= gross_earnings < 33333:
    withholding_tax = 0.00 + 0.15/20833
elif 33333 <= gross_earnings < 66667:
    withholding_tax = 1875 + 0.20/33333
elif 66667 <= gross_earnings < 166667:
    withholding_tax = 8541.80 + 0.25/66667
elif 166667 <= gross_earnings < 666667:
    withholding_tax = 33541.80 + 0.30/166667
else:
    withholding_tax = 183541.80 + 0.35/666667

deduction = absences + tardy + withholding_tax + sss_contribution + philhealth_contribution + hdmf_contribution
net_pay = gross_earnings - deduction

print("Company name:", company_name)
print("Employee code:", employee_code)
print("Employee name:", employee_name)
print("Department:", department)
print("Cut off pay", cut_off)
print("Pay period:", pay_period)
print("Basic pay:", basic_pay)
print("Overtime pay:", overtime)
print("Absences:", absences)
print("Honorarium:", honorarium)
print("Tardy:", tardy)
print("With holding tax:", withholding_tax)
print("SSS contribution:", sss_contribution)
print("HDMF contribution:", hdmf_contribution)
print("Philhealth contribution:", philhealth_contribution)
print("Deduction:", deduction)
print("Gross earnings:", gross_earnings)
print("Net pay:", net_pay)

