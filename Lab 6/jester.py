import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Payroll Page')
window.geometry("900x1520")

class design_gui_interface():

    def __int__(self, frame1):
        frame1 = ' '

    def frames(self, x, y):
        self.frame1 = Frame(window, width=1000, height=700, border=0, bg='light gray')
        self.frame1.place(x=x, y=y)

    def heading_design1(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Times New Roman', 30, 'bold'))
        self.heading.place(x=x, y=y)

    def textbox_design(self, x, y):
        self.textbox = tk.Text(width=25, height=1, fg='black', bg='white', font=('Arial', 12))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='light gray', font=('Arial', 12))
        self.textbox.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, font=('Arial', 10,))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, font=('Arial', 12, 'bold'))
        self.lbl.place(x=x, y=y)

    def button_design1(self, x, y):
        self.upload_button = Button(width=10,padx=10,text='SEARCH',bg='red', fg='white',cursor='hand2',border=5)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='GROSS INCOME', bg='blue', fg='white', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='NET INCOME', bg='blue', fg='white', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def button_design4(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='SAVE', bg='cyan', fg='white', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def button_design5(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='UPDATE', bg='cyan', fg='white', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def button_design6(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='NEW', bg='yellow', fg='black', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image,resize(length, width))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.place(x=x, y=y)


# Instantiation of the class
my_gui_design = design_gui_interface()

# Heading for payroll
my_gui_design.heading_design1(x=250, y=20, text_value="SE-RI'S CHOICE PAYROLL")



# Label1 for employee basic info
employee_numberlbl = my_gui_design.label_design1(x=40, y=290, text_value='Employee Number')
search_employeelbl = my_gui_design.label_design1(x=40, y=330, text_value='Search Employee')
departmentlbl = my_gui_design.label_design1(x=40, y=360, text_value='Deperment')
firstname_lbl = my_gui_design.label_design1(x=450, y=120, text_value='Firstname')
middle_namelbl = my_gui_design.label_design1(x=450, y=150, text_value='Middle Name')
surnamelbl = my_gui_design.label_design1(x=450, y=180, text_value='Surname')
civil_statuslbl = my_gui_design.label_design1(x=450, y=210, text_value='Civil Status')
qualified_dependents_statuslbl = my_gui_design.label_design1(x=450, y=240, text_value='Qualified Depentents Status')
pay_datelbl = my_gui_design.label_design1(x=450, y=270, text_value='Paydate')
employee_statuslbl = my_gui_design.label_design1(x=450, y=300, text_value='Employee Status')
designationlbl = my_gui_design.label_design1(x=450, y=330, text_value='Designation')

# Label1 for basic income
rate_per_hourlbl = my_gui_design.label_design1(x=40, y=440, text_value='Rate / Hour')
no_of_hours_cut_offlbl = my_gui_design.label_design1(x=40, y=470, text_value='No. of Hours / Cut Off')
income_cut_offlbl = my_gui_design.label_design1(x=40, y=500, text_value='Income / Cut Off')

# Label1 for Honorarium income
rate_per_hourlbl = my_gui_design.label_design1(x=40, y=580, text_value='Rate / Hour')
no_of_hours_cut_offlbl = my_gui_design.label_design1(x=40, y=610, text_value='No. of Hours / Cut Off')
income_cut_offlbl = my_gui_design.label_design1(x=40, y=640, text_value='Income / Cut Off')

# Label1 for other income
rate_per_hourlbl = my_gui_design.label_design1(x=40, y=720, text_value='Rate / Hour')
no_of_hours_cut_offlbl = my_gui_design.label_design1(x=40, y=750, text_value='No. of Hours / Cut Off')
income_cut_offlbl = my_gui_design.label_design1(x=40, y=780, text_value='Income / Cut Off')

# Label1 for summary income
gross_incomelbl = my_gui_design.label_design1(x=40, y=860, text_value='GROSS INCOME')
net_incomelbl = my_gui_design.label_design1(x=40, y=890, text_value='NET INCOME')

# Label1 for regular deductions
sss_contributionlblb = my_gui_design.label_design1(x=450, y=410, text_value='SSS Contribution')
philhealth_contributionlbl = my_gui_design.label_design1(x=450, y=440, text_value='PhilHealth Contribution')
pagibig_contributionlblb = my_gui_design.label_design1(x=450, y=470, text_value='Pagibig Contribution')
income_tax_contributiontxt = my_gui_design.label_design1(x=450, y=500, text_value='Income Tax Contribution')

# Label1 for other deductions
sss_loanlbl = my_gui_design.label_design1(x=450, y=580, text_value='SSS Loan')
pagibig_loanlbl = my_gui_design.label_design1(x=450, y=610, text_value='Pagibig Loan')
faculty_savings_depositlbl = my_gui_design.label_design1(x=450, y=640, text_value='Faculty Savings Deposit')
faculty_savings_loanlbl = my_gui_design.label_design1(x=450, y=670, text_value='Faculty Savings Loan')
salary_loanlbl = my_gui_design.label_design1(x=450, y=700, text_value='Salary Loan')
other_loanlbl = my_gui_design.label_design1(x=450, y=730, text_value='Other Loan')

# Label1 for deduction summary
total_deductionlbl = my_gui_design.label_design1(x=450, y=810, text_value='Total Deduction')

# Label2 design
employee_basic_infolbl = my_gui_design.label_design2(x=20, y=100, text_value='EMPLOYEE BASIC INFO:')
basic_incomelbl = my_gui_design.label_design2(x=30, y=400, text_value='BASIC INCOME:')
honorarium_incomelbl = my_gui_design.label_design2(x=30, y=540, text_value='HONORARIUM INCOME:')
other_incomelbl = my_gui_design.label_design2(x=30, y=680, text_value='OTHER INCOME:')
summary_incomelbl = my_gui_design.label_design2(x=30, y=820, text_value='SUMMARY INCOME:')
regular_deductionslbl = my_gui_design.label_design2(x=430, y=370, text_value='REGULAR DEDUCTIONS:')
other_deductionslbl = my_gui_design.label_design2(x=430, y=540, text_value='OTHER DEDUCTIONS:')
deduction_summarylbl = my_gui_design.label_design2(x=430, y=770, text_value='DEDUCTION SUMMARY:')

# Textbox for employee basic info
employee_numbertxt = my_gui_design.textbox_design(x=180, y=290)
departmenttxt = my_gui_design.textbox_design2(x=180, y=360)
firstnametxt = my_gui_design.textbox_design2(x=640, y=120)
middle_nametxt = my_gui_design.textbox_design2(x=640, y=150)
surnametxt = my_gui_design.textbox_design2(x=640, y=180)
civil_statustxt = my_gui_design.textbox_design2(x=640, y=210)
qualified_dependents_statustxt = my_gui_design.textbox_design(x=640, y=240)
pay_datetxt = my_gui_design.textbox_design(x=640, y=270)
employee_statustxt = my_gui_design.textbox_design2(x=640, y=300)
designationtxt = my_gui_design.textbox_design2(x=640, y=330)

# Textbox for basic income
rate_per_hourtxt = my_gui_design.textbox_design(x=180, y=440)
no_of_hours_cut_offtxt = my_gui_design.textbox_design(x=180, y=470)
income_cut_offtxt = my_gui_design.textbox_design2(x=180, y=500)

# Textbox for honorarium income
rate_per_hourtxt = my_gui_design.textbox_design(x=180, y=580)
no_of_hours_cut_offtxt = my_gui_design.textbox_design(x=180, y=610)
income_cut_offtxt = my_gui_design.textbox_design2(x=180, y=640)

# Textbox for other income
rate_per_hourtxt = my_gui_design.textbox_design(x=180, y=710)
no_of_hours_cut_offtxt = my_gui_design.textbox_design(x=180, y=740)
income_cut_offtxt = my_gui_design.textbox_design2(x=180, y=770)

# Textbox for summary income
gross_incometxt = my_gui_design.textbox_design(x=180, y=860)
net_incometxt = my_gui_design.textbox_design2(x=180, y=890)

# Textbox for regular deductions
sss_contributiontxt = my_gui_design.textbox_design2(x=640, y=410)
philhealth_contributiontxt = my_gui_design.textbox_design2(x=640, y=440)
pagibig_contributiontxt = my_gui_design.textbox_design2(x=640, y=470)
income_tax_contribution = my_gui_design.textbox_design2(x=640, y=500)

# Textbox for other deductions
sss_loantxt = my_gui_design.textbox_design(x=640, y=580)
pagibig_loantxt = my_gui_design.textbox_design(x=640, y=610)
faculty_savings_deposittxt = my_gui_design.textbox_design(x=640, y=640)
faculty_savings_loantxt = my_gui_design.textbox_design(x=640, y=670)
salary_loantxt = my_gui_design.textbox_design(x=640, y=700)
other_loantxt = my_gui_design.textbox_design(x=640, y=730)

# Textbox for deduction summary
total_deductiontxt = my_gui_design.textbox_design(x=640, y=810)

# Adding combo for civil status
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=34, textvariable=n)
combo_field1['values'] = (' Single', ' Married', ' Widow', ' Legally Separated', ' Annulled')
combo_field1.place(x=640, y=210)
combo_field1.current()

# Call for all button
uploadbutton = my_gui_design.button_design1(x=180, y=320)
uploadbutton = my_gui_design.button_design2(x=430, y=870)
uploadbutton = my_gui_design.button_design3(x=535, y=870)
uploadbutton = my_gui_design.button_design4(x=641, y=870)
uploadbutton = my_gui_design.button_design5(x=747, y=870)
uploadbutton = my_gui_design.button_design6(x=430, y=905)

window.mainloop()
