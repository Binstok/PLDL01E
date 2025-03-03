import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Assessment form')
window.geometry('1000x1200')

#classess
class gui_interface():

    def __int__(self, frame1):
        frame1 = ''

    def frame1(self, x, y):
        self.frame1 = Frame (window, width=600, height=900, border=0, bg='light grey')
        self.frame1.place(x=x, y=y)

    def frame2(self, x, y):
        self.frame2 = Frame(window, width=357, height=900, border=0, bg='light grey')
        self.frame2.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.label = Label(bg='light grey', font=('Arial', 20), text=text_value)
        self.label.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='light grey', font=('Arial', 12, 'bold'))
        self.label.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='light grey', font=('Arial', 10))
        self.label.place(x=x, y=y)

    def label_design4(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='light grey', font=('Arial', 8))
        self.label.place(x=x, y=y)

    def label_design5(self,x ,y, text_value):
        self.label = Label(text=text_value, fg='black', bg='light grey', font=('Arial', 10, 'bold'))
        self.label.place(x=x, y=y)

    def label_design6(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='light grey', font=('Arial', 10))
        self.label.place(x=x, y=y)

    def label_design7(self, x, y, text_value):
        self.label = Label (text=text_value, fg='black', font=('Times New Roman', 16, 'bold'))
        self.label.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 9))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='light grey', font=('Arial', 9))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=15, height=1, fg='black', bg='white', font=('Arial', 9))
        self.textbox.place(x=x, y=y)

    def textbox_design4(self, x, y):
        self.textbox = Text(width=10, height=1, fg='black', bg='white', font=('Arial', 9))
        self.textbox.place(x=x, y=y)

    def textbox_design5(self, x, y):
        self.textbox = Text(width=2, height=1, fg='black', bg='white', font=('Arial', 9))
        self.textbox.place(x=x, y=y)

    def textbox_design6(self, x, y):
        self.textbox = Text(width=10, height=1, fg='black', bg='light grey', font=('Arial', 9))
        self.textbox.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.place (x=x, y=y)



#display the frame and instantiation of classes
gui_design = gui_interface()
gui_design.frame1(20, 120)
gui_design.frame2(625, 120)

#text of lpu
lpulbl = gui_design.label_design7(130, 10, 'LYCEUM OF THE PHILIPPINES UNIVERSITY')

#text of assessment form and student information
assessmentlbl = gui_design.label_design2(30, 130, 'STUDENT ASSESSMENT FORM')
namelbl = gui_design.label_design3(30, 180, 'Name: ')
student_numberlbl = gui_design.label_design3(30, 200, 'Student Number: ')
courselbl = gui_design.label_design3(30, 220, 'Course: ')
semesterlbl = gui_design.label_design3(350, 180, 'Semester: ')
academic_yearlbl = gui_design.label_design3(350, 200,'Academic Year: ')
class_schedulelbl = gui_design.label_design5(30, 249, 'CLASS SCHEDULE')

#text lines
line1 = gui_design.label_design1(20, 265, '------------------------------------------------------------------')
line2 = gui_design.label_design1(625, 265, '---------------------------------------')
line3 = gui_design.label_design1(20, 295, '------------------------------------------------------------------')
line4 = gui_design.label_design1(625, 295, '---------------------------------------')
line5 = gui_design.label_design1(625, 819, '---------------------------------------')
line6 = gui_design.label_design1(20, 819,'------------------------------------------------------------------' )

#text of students subjects
subject_codelbl = gui_design.label_design4(30, 290, 'SUBJECT CODE')
courselbl = gui_design.label_design4(140, 290, 'COURSE DESCRIPTION')
sectionlbl = gui_design.label_design4(313, 290, 'SECTION/ROOM')
timeanddaylbl = gui_design.label_design4(465, 290, 'DAY/TIME')
unitslbl = gui_design.label_design4(573, 290,'UNITS')
total_unitslbl = gui_design.label_design5(480, 600, 'TOTAL UNITS: ')

#text of students assessment fees
assessment_feeslbl = gui_design.label_design4(630, 290, 'ASSESSMENT FEES')
tuition_fee_lecturelbl = gui_design.label_design5(630, 325,'TUITION FEE : ')
total_miscellaneouslbl = gui_design.label_design5(630, 345, 'TOTAL MISCELLANEOUS FEES: ')
athletic_feelbl = gui_design.label_design3(630, 365, 'Athletic Fee: ' )
bar_operation_feelbl = gui_design.label_design3(630, 385, 'Bar Operation Fee: ')
ictfeelbl = gui_design.label_design3(630, 405, 'ICT Fee: ')
insurance_feelbl = gui_design.label_design3(630, 425, 'Insurance: ')
law_council_feelbl = gui_design.label_design3(630, 445, 'Law Council Fee: ')
library_feelbl = gui_design.label_design3(630, 465, 'Library Fee: ')
law_journal_feelbl = gui_design.label_design3(630, 485, 'Law Journal Fee:')
learning_management_feelbl = gui_design.label_design3(630, 505, 'Learning Management Fee: ')
medical_and_dental_feelbl =gui_design.label_design3(630, 525, 'Medical/Dental Fee: ')
registrationlbl = gui_design.label_design3(630, 545, 'Registration Fee: ')
student_activity_feelbl = gui_design.label_design3(630, 565, 'Student Activity Fee:')
utilities_bldg_chargeslbl = gui_design.label_design3(630, 585, 'Utilities Bldg Charges: ')

#text of laboratory and other fees
total_laboratory_and_other_feelbl = gui_design.label_design5(630, 620, 'TOTAL LABORATORY AND OTHER: ')
laboratory_feelbl = gui_design.label_design3(630, 650, 'LABORATORY FEES ')
otherfeeslbl = gui_design.label_design3(630, 740, 'OTHER FEES')

#text of total assessment fees
total_assessmentfeelbl = gui_design.label_design3(630, 852, 'TOTAL ASSESSMENT: ')
installment_chargelbl = gui_design.label_design5(630, 872, 'ADD: INSTALLMENT CHARGE: ')
line7lbl = gui_design.label_design6(625, 888, '---------------------------------------------------------------------------------------')
total_amount_duelbl= gui_design.label_design3(630, 905, 'TOTAL AMOUNT DUE: ')
less_payment_madelbl = gui_design.label_design5(630, 925, 'LESS: PAYMENT MADE: ')
line8lbl = gui_design.label_design6(625, 942, '---------------------------------------------------------------------------------------')
balancelbl = gui_design.label_design3(630, 955, 'BALANCE(PAYABLE INSTALLMENTS): ')

#text of payments and balance
installment_paymentlbl = gui_design.label_design5(30, 852, 'INSTALLMENT PAYMENT SCHEDULE')
paymentlbl = gui_design.label_design5(30, 872, 'PAYMENT')
due_datelbl = gui_design.label_design5(265, 872, 'DUE DATE')
minimum_amount_duelbl = gui_design.label_design5(450, 872, 'MINIMUM AMOUNT DUE')
payment1lbl = gui_design.label_design3(30, 892, 'Payment 1')
payment2lbl = gui_design.label_design3(30, 912, 'Payment 2')

#other texts
line8lbl = gui_design.label_design6(180, 952,'----------------------------------------------------------------------------' )
signature_name_datelbl = gui_design.label_design3(225, 965, 'Signature over Printed Name and Date')
printed_bylbl = gui_design.label_design3(30, 992, 'Printed by:')
date_and_time_printedlbl = gui_design.label_design3(630, 992, 'Date and Time Printed: ')

#textbox box for student information
nametxt = gui_design.textbox_design1(75, 180)
student_numbertxt = gui_design.textbox_design1(135, 200)
coursetxt = gui_design.textbox_design3(80, 220)
semestertxt = gui_design.textbox_design3(415, 180)
academic_yeartxt = gui_design.textbox_design3(448, 203)

#textbox for students subjects
subject_code1txt = gui_design.textbox_design4(30, 325)
subject_code2txt = gui_design.textbox_design4(30, 355)
subject_code3txt = gui_design.textbox_design4(30, 385)
subject_code4txt = gui_design.textbox_design4(30, 415)
subject_code5txt = gui_design.textbox_design4(30, 445)
subject_code6txt = gui_design.textbox_design4(30, 475)
subject_code7txt = gui_design.textbox_design4(30, 505)
subject_code8txt = gui_design.textbox_design4(30, 535)
subject_code9txt = gui_design.textbox_design4(30, 565)

#textbox for course descriptions
course_description1txt = gui_design.textbox_design3(140, 325)
course_description2txt = gui_design.textbox_design3(140, 355)
course_description3txt = gui_design.textbox_design3(140, 385)
course_description4txt = gui_design.textbox_design3(140, 415)
course_description5txt = gui_design.textbox_design3(140, 445)
course_description6txt = gui_design.textbox_design3(140, 475)
course_description7txt = gui_design.textbox_design3(140, 505)
course_description8txt = gui_design.textbox_design3(140, 535)
course_description9txt = gui_design.textbox_design3(140, 565)

#textbox for sections
section1txt = gui_design.textbox_design3(300, 325)
section2txt = gui_design.textbox_design3(300, 355)
section3txt = gui_design.textbox_design3(300, 385)
section4txt = gui_design.textbox_design3(300, 415)
section5txt = gui_design.textbox_design3(300, 445)
section6txt = gui_design.textbox_design3(300, 475)
section7txt = gui_design.textbox_design3(300, 505)
section8txt = gui_design.textbox_design3(300, 535)
section9txt = gui_design.textbox_design3(300, 565)

#textbox for time and day
timeandday1txt = gui_design.textbox_design3(440,325)
timeandday2txt = gui_design.textbox_design3(440,355)
timeandday3txt = gui_design.textbox_design3(440,385)
timeandday4txt = gui_design.textbox_design3(440,415)
timeandday5txt = gui_design.textbox_design3(440,445)
timeandday6txt = gui_design.textbox_design3(440,475)
timeandday7txt = gui_design.textbox_design3(440,505)
timeandday8txt = gui_design.textbox_design3(440,535)
timeandday9txt = gui_design.textbox_design3(440,565)

#textbox for units
units1txt = gui_design.textbox_design5(580,325)
units2txt = gui_design.textbox_design5(580,355)
units3txt = gui_design.textbox_design5(580,385)
units4txt = gui_design.textbox_design5(580,415)
units5txt = gui_design.textbox_design5(580,445)
units6txt = gui_design.textbox_design5(580,475)
units7txt = gui_design.textbox_design5(580,505)
units8txt = gui_design.textbox_design5(580,535)
units9txt = gui_design.textbox_design5(580,565)
total_unitstxt = gui_design.textbox_design5(580, 600)

#textbox for assessment fees
tuition_fee_lecturetxt = gui_design.textbox_design6(900, 325)
total_miscellaneoustxt = gui_design.textbox_design6(900, 345)
athletic_feetxt = gui_design.textbox_design6(900, 365)
bar_operation_feetxt = gui_design.textbox_design6(900, 385)
ictfeetxt = gui_design.textbox_design6(900, 405)
insurance_feetxt = gui_design.textbox_design6(900,425)
law_council_feetxt = gui_design.textbox_design6(900, 445)
library_feetxt = gui_design.textbox_design6(900, 465)
law_journal_feetxt = gui_design.textbox_design6(900, 485)
learning_management_feetxt = gui_design.textbox_design6(900, 505)
medical_and_dental_feetxt = gui_design.textbox_design6(900, 525)
registrationtxt = gui_design.textbox_design6(900, 545)
student_activity_feetxt = gui_design.textbox_design6(900, 565)
utilities_bldg_chargestxt = gui_design.textbox_design6(900, 585)

#textbox for laboratory and other fee
total_laboratory_and_other_feetxt = gui_design.textbox_design6(900, 620)
laboratory1txt = gui_design.textbox_design2(630, 670)
laboratory2txt = gui_design.textbox_design2(630, 690)
laboratory3txt = gui_design.textbox_design2(630, 710)
laboratory_fee1txt = gui_deslaboratory_fee1txt = gui_design.textbox_design6(900, 670)
laboratory_fee2txt = gui_deslaboratory_fee1txt = gui_design.textbox_design6(900, 690)
laboratory_fee3txt = gui_deslaboratory_fee1txt = gui_design.textbox_design6(900, 710)
other1txt = gui_design.textbox_design2(630, 760)
other2txt = gui_design.textbox_design2(630, 780)
other3txt = gui_design.textbox_design2(630, 800)
otherfees1txt = gui_design.textbox_design6(900, 760)
otherfees2txt = gui_design.textbox_design6(900, 780)
otherfees3txt = gui_design.textbox_design6(900, 800)

#textbox for payment and balance
total_assessmentfeetxt = gui_design.textbox_design6(900, 852)
installment_chargetxt = gui_design.textbox_design6(900, 872)
total_amount_duetxt = gui_design.textbox_design6(900, 905)
less_payment_madetxt = gui_design.textbox_design6(900, 925)
balancetxt = gui_design.textbox_design6(900, 958)

#textbox for installment paymen schedule
due_date1txt = gui_design.textbox_design6(265, 892)
due_date2txt = gui_design.textbox_design6(265, 912)
minimum_amount_due1txt = gui_design.textbox_design6(450, 892)
minimum_amount_due1txt = gui_design.textbox_design6(450, 912)

#other textbox
printed_bytxt = gui_design.textbox_design2(100,994)
date_and_time_printedtxt = gui_design.textbox_design2(770, 994)

# adding combo box for semester
n = tk.StringVar()
combo_field = ttk.Combobox(window, width=15, textvariable=n)
combo_field['values'] = ('First Semester', 'Second Semester', 'Summer Term')
combo_field.place(x=415, y=180)
combo_field.current()

#call image to display
upload_image = gui_design.image_design(r'C:\Users\Admin\PycharmProjects\PLDL01E\images\lpu_logo.png', 20, 10, 100, 100)

window.mainloop()

