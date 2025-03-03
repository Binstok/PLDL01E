import tkinter as tk
from tkinter import ttk

#call and import classes from project then payroll_page_classess
from Project.payroll_page_classes import gui_interface

#window
window = tk.Tk()
window.title("Payroll Page")
window.geometry('1000x1080')

#instantiation of classes
gui_design = gui_interface()

#text header
payrolllbl = gui_design.label_design2(180, 50, 'SE-RI`S CHOICE PAYROLL')

#text of employee basic info
employee_basic_infolbl = gui_design.label_design3(20, 150, 'EMPLOYEE BASIC INFO: ')
employee_namelbl = gui_design.label_design1(40, 400, 'Employee Name: ')
employee_searchlbl = gui_design.label_design1(40, 430, 'Employee Search: ')
department = gui_design.label_design1(40, 460, 'Department: ')

#text of basic income
basic_incomelbl = gui_design.label_design3(20, 500, 'BASIC INCOME: ')
rate_per_hourlbl = gui_design.label_design1(40, 530, 'Rate/Hour: ')
number_of_hourslbl = gui_design.label_design1(40, 560, 'No. of Hours/Cut off: ')
incomelbl = gui_design.label_design1(40, 590, 'Income/Cut off: ')

#text of honorarium income
honorariumlbl = gui_design.label_design3(20, 630, 'HONORARIUM INCOME: ')
rate_per_hourlbl = gui_design.label_design1(40,660, 'Rate/Hour: ' )
number_of_hourslbl = gui_design.label_design1(40, 690, 'No. of Hours/Cut off: ')
incomelbl = gui_design.label_design1(40, 720, 'Income/Cut off: ')

#text of other income
other_incomelbl = gui_design.label_design3(20, 760, 'OTHER INCOME: ')
rate_per_hourlbl = gui_design.label_design1(40,790, 'Rate/Hour: ' )
number_of_hourslbl = gui_design.label_design1(40, 820, 'No. of Hours/Cut off: ')
incomelbl = gui_design.label_design1(40, 850, 'Income/Cut off: ')

#text of summary income
summary_incomelbl = gui_design.label_design3(20, 890, 'SUMMARY INCOME:')
gross_incomelbl = gui_design.label_design1(40, 920, 'GROSS INCOME: ')
net_incomelbl = gui_design.label_design1(40,950, 'NET INCOME: ')

#others text needed
first_namelbl = gui_design.label_design1(550, 180, 'First Name: ')
middle_namelbl = gui_design.label_design1(550, 210, 'Middle Name: ' )
surnamelbl = gui_design.label_design1(550, 240, 'Surname: ')
civil_statuslbl = gui_design.label_design1(550, 270, 'Civil Status: ')
qualified_dependents_statuslbl = gui_design.label_design1(550, 300, 'Qualified Dependents Status: ')
paydatlbl = gui_design.label_design1(550, 330, 'Paydate: ')
employee_statuslbl = gui_design.label_design1(550, 360, 'Employee Status: ')
designationlbl = gui_design.label_design1(550, 390, 'Designation: ')

#text of regular deduction
regular_deductionlbl = gui_design.label_design3(520, 490, 'REGULAR DEDUCTION: ')
sss_contributionlbl = gui_design.label_design1(550, 520, 'SSS Contribution: ')
philheal_contributionlbl = gui_design.label_design1(550, 550, 'PhilHealth Contribution: ')
pagibig_contributionlbl = gui_design.label_design1(550, 580, 'Pagibig Contribution: ')
incometax_contributionlbl = gui_design.label_design1(550, 610, 'Income Tax Contribution: ')

#text of other deduction
other_deductionlbl = gui_design.label_design3(520, 650, 'OTHER DEDUCTIONS: ')
sss_loanlbl = gui_design.label_design1(550, 680, 'SSS Loan: ')
pagibig_loanlbl = gui_design.label_design1(550, 710, 'Pagibig Loan: ')
faculty_saving_depositlbl = gui_design.label_design1(550, 740, 'Faculty Savings Deposit: ')
faculty_saving_loanlbl = gui_design.label_design1(550, 770, 'Faculty Savings Loan: ')
salary_loanlbl = gui_design.label_design1(550, 800, 'Salary Loan: ')
other_loanlbl = gui_design.label_design1(550, 830, 'Other Loans: ')

#text of deduction summary
deduction_summarylbl = gui_design.label_design3(520, 870, 'DEDUCTION SUMMARY: ')
total_deductionlbl = gui_design.label_design1(550, 900, 'Total Deductions: ')


#textboxes
employee_nametxt = gui_design.textbox_design1( 180, 400)
departmenttxt = gui_design.textbox_design2(180, 460)
rate_per_hourtxt = gui_design.textbox_design1(180, 530)
number_of_hourstxt = gui_design.textbox_design1(180, 560)
incometxt = gui_design.textbox_design2(180, 590)
rate_per_hourtxt = gui_design.textbox_design1(180, 660)
number_of_hourstxt = gui_design.textbox_design1(180, 690)
incometxt = gui_design.textbox_design2(180, 720)
rate_per_hourtxt = gui_design.textbox_design1(180, 790)
number_of_hourstxt = gui_design.textbox_design1(180, 820)
incometxt = gui_design.textbox_design2(180, 850)
gross_incometxt = gui_design.textbox_design1(180, 920)
net_incometxt = gui_design.textbox_design2(180, 950)
first_nametxt = gui_design.textbox_design2(750, 180)
middle_nametxt = gui_design.textbox_design2(750, 210)
surnametxt = gui_design.textbox_design2(750, 240)
qualified_dependents_statustxt = gui_design.textbox_design1(750, 300)
paydattxt = gui_design.textbox_design1(750, 330)
employee_statustxt = gui_design.textbox_design2(750,360)
designationtxt = gui_design.textbox_design2(750, 390)
sss_contributiontxt = gui_design.textbox_design2(750, 520)
philheal_contributiontxt = gui_design.textbox_design2(750, 550)
pagibig_contributiontxt = gui_design.textbox_design2(750, 550)
incometax_contributiontxt = gui_design.textbox_design2(750, 580)
sss_loantxt = gui_design.textbox_design1(750, 680)
pagibig_loantxt = gui_design.textbox_design1(750, 710)
faculty_saving_deposittxt = gui_design.textbox_design1(750, 740)
faculty_saving_loantxt = gui_design.textbox_design1(750, 770)
salary_loantxt = gui_design.textbox_design1(750, 800)
other_loantxt = gui_design.textbox_design1(750, 830)
total_deductiontxt = gui_design.textbox_design2(750, 900)

#call all the buttons
upload_button = gui_design.button_design(180, 428)
upload_button = gui_design.button_desing2(520, 945)
upload_button = gui_design.button_design3(635, 945)
upload_button = gui_design.button_design4(736, 945)
upload_button = gui_design.button_design5(802, 945)
upload_button = gui_design.button_design6(867, 945)

# adding combo box for civil status
n = tk.StringVar()
combo_field = ttk.Combobox(window, width=26, textvariable=n)
combo_field['values'] = ('Single', 'Married', 'Widow', 'Legally', 'Separated', 'Annulled')
combo_field.place(x=750, y=270)
combo_field.current()

#call image to display
upload_image = gui_design.image_design(r'C:\Users\Admin\PycharmProjects\PLDL01E\images\1.png', 30, 180, 220, 200)

window.mainloop()