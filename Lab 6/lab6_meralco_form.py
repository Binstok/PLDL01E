import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Meralco form')
window.geometry('1000x1200')

#add class 1 for frame 1 and 2
class gui_interface():

    def __int__(self, frame1):
        frame = ''

    def frame1(self, x, y):
        self.frame1 = Frame(window, width= 990 , height= 300, border=0, bg='white')
        self.frame1.place(x=x, y=y)

    def frame2(self, x, y):
        self.frame2 = Frame(window, width= 645 , height= 725, border=0, bg='white')
        self.frame2.place(x=x, y=y)

    def frame3(self, x, y):
        self.frame3 = Frame(window, width= 990 , height= 25, border=0, bg='dark orange')
        self.frame3.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.label = Label(text=text_value, bg='dark orange', fg='black', font=('Arial', 12, 'bold') )
        self.label.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.label = Label(text=text_value, bg='white', fg='black', font=('Arial', 12, 'bold') )
        self.label.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.label = Label(text=text_value, bg='white', fg='black', font=('Arial', 12) )
        self.label.place(x=x, y=y)

    def label_design4(self, x, y, text_value):
        self.label = Label(text=text_value, bg='white', fg='black', font=('Arial', 10) )
        self.label.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='white', font=('Arial', 12, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=10, height=1, fg='black', bg='white', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='white', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.place (x=x, y=y)

#class 2 for frame 3 and billing statement
class gui_interface_billing_statement():
    def __int__(self, frame3):
        frame = ''

    def frame4(self, x, y):
        self.frame4 = Frame(window, width= 335 , height= 725, border=0, bg='white')
        self.frame4.place(x=x, y=y)

    def frame5(self, x, y):
        self.frame5 = Frame(window,width= 317, height= 150, border=0, bg='light blue')
        self.frame5.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='white', font=('Arial', 12, 'bold'))
        self.label.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='light blue', font=('Arial', 10))
        self.label.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='light blue', font=('Arial', 12, 'bold'))
        self.label.place(x=x, y=y)

    def label_design4(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='white', font=('Arial', 9))
        self.label.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=15, height=1, fg='black', bg='light blue', font=('Arial', 12, 'bold') )
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='light blue', font=('Arial', 12, 'bold') )
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=10, height=1, fg='black', bg='light blue', font=('Arial', 12, 'bold') )
        self.textbox.place(x=x, y=y)

    def textbox_design4(self, x, y):
        self.textbox = Text(width=10, height=1, fg='black', bg='light grey', font=('Arial', 10) )
        self.textbox.place(x=x, y=y)

    def textbox_design5(self, x, y):
        self.textbox = Text(width=13, height=1, fg='black', bg='light grey', font=('Arial', 12, 'bold') )
        self.textbox.place(x=x, y=y)

#display the frame and instantiation of classes
gui_design1 = gui_interface()
gui_design2 = gui_interface_billing_statement()
gui_design1.frame1(5, 5)
gui_design1.frame3(5, 110)
gui_design1.frame2(5, 315)
gui_design2.frame4(660, 315)
gui_design2.frame5(670, 325)

#text for name and address
namelbl = gui_design1.label_design2(10, 10, 'Name: ')
addresslbl = gui_design1.label_design2(10, 40, 'Address: ')

#design of lines
line1lbl = gui_design1.label_design3(5, 135, '_____________________________________________________________________________________________________________')
line2lbl = gui_design1.label_design3(5, 165, '_____________________________________________________________________________________________________________')
line3lbl = gui_design1.label_design3(5, 200, '_____________________________________________________________________________________________________________')
line4lbl = gui_design1.label_design3(660, 840, '____________________________________')

#text for customer info and bill
electric_bill_lbl = gui_design1.label_design1(425, 110,' ELECTRIC BILL')
customer_account_numberlbl = gui_design1.label_design2(10, 160, 'Summary for Customer Account Number (CAN): ')
balancelbl = gui_design1.label_design4(25, 190, 'Balance from Previous Billing: ')
current_chargeslbl = gui_design1.label_design2(25, 223, 'CURRENT CHARGES')
amount_duelbl = gui_design1.label_design4(25, 245, 'Amount due: ')
due_datelbl = gui_design1.label_design4(200, 245, 'Due Date: ' )
total_amount_duelbl = gui_design1.label_design2(600, 240, 'TOTAL AMOUNT DUE: ')

#text for service info
service_infolbl = gui_design1.label_design2(10, 325, 'SERVINCE INFO')
service_id_numberlbl = gui_design1.label_design4(10, 350, 'Service ID Number: ')
ratelbl = gui_design1.label_design4(10, 375, 'Rate: ')
contact_in_the_namelbl = gui_design1.label_design4(10, 400, 'Contact in the name of: ')
service_addresslbl = gui_design1.label_design4(10, 425, 'Service Address: ')

#text for billing info
billing_infolbl = gui_design1.label_design2(10, 475, 'BILLING INFO')
bill_datelbl = gui_design1.label_design4(10, 500, 'Bill Date: ')
meter_reading_datelbl = gui_design1.label_design4(10, 525, 'Meter Reading Date: ')
bill_periodlbl = gui_design1.label_design4(10, 550, 'Bill Period: ')
due_date2lbl = gui_design1.label_design4(10, 575, 'Due Date: ')
total_kwhlbl = gui_design1.label_design4(10, 600, 'Total KWH: ')
total_current_amountlbl = gui_design1.label_design4(10, 625, 'Total Current Amount: ')
next_meter_readinglbl = gui_design1.label_design4(10, 650, 'Next Meter Reading: ')

#test for break down electricity charges
breakdownlbl = gui_design1.label_design2(10, 700, 'BREAKDOWN OF ELECTRICITY CHARGES')
bill_subgrouplbl = gui_design1.label_design4(10, 725, 'BILL SUBGROUP')
generationlbl = gui_design1.label_design4(10, 750, 'Generation')
transmissionlbl = gui_design1.label_design4(10, 775, 'Transmission')
system_losslbl = gui_design1.label_design4(10, 800, 'System Loss')
distributionlbl = gui_design1.label_design4(10, 825, 'Distribution (Meralco)')
subsidieslbl = gui_design1.label_design4(10, 850, 'Subsidies')
government_taxlbl = gui_design1.label_design4(10, 875, 'Government Taxes')
universal_chargeslbl = gui_design1.label_design4(10, 900, 'Unversal Charges')
fitlbl = gui_design1.label_design4(10, 925, 'FiT-All (Renewable)')
other_chargeslbl = gui_design1.label_design4(10, 950,'Other Charges')
subtotallbl = gui_design1.label_design4(250, 725, 'SUBTOTAL')
percentagelbl = gui_design1.label_design4(450, 725, 'PERCENTAGE')

#text of customer account in billing statement
customer_account_number2lbl = gui_design2.label_design2(670, 330, 'Customer Account Number(CAN)')
due_date3lbl = gui_design2.label_design2(888, 330, 'Due Date')
plbl = gui_design2.label_design3(685, 430, '₱')

#text for bill computation summary
bill_computation_summarylbl = gui_design2.label_design1(665,500, 'BILL COMPUTATION SUMMARY')
remaining_balance_from_previous_billlbl = gui_design2.label_design4(665, 525, 'Remaining Balance from Previous Bill')
charges_for_this_billing_periodlbl = gui_design2.label_design4(665, 550, 'Charges for this Billing Period')
generation2lbl = gui_design2.label_design4(675, 575, 'Generation')
transmission2lbl = gui_design2.label_design4(675, 600, 'Transmission')
system_loss2lbl = gui_design2.label_design4(675, 625, 'System Loss')
distribution2lbl = gui_design2.label_design4(675, 650, 'Distribution (Meralco)')
subsidies2lbl = gui_design2.label_design4(675, 675, 'Subsidies')
government_tax2lbl = gui_design2.label_design4(675, 700, 'Government Taxes')
universal_charges2lbl = gui_design2.label_design4(675, 725, 'Unversal Charges')
fit2lbl = gui_design2.label_design4(675, 750, 'FiT-All (Renewable)')
applied_creditslbl = gui_design2.label_design4(675, 775, 'Applied Credits')
other_charges2lbl = gui_design2.label_design4(675, 800,'Other Charges')
installment_duelbl = gui_design2.label_design4(665, 825, 'Installment Due')
total_amount_due2lbl = gui_design2.label_design1(665, 870, 'Total Amount Due')
p2lbl = gui_design2.label_design1(853, 870, '₱')

#textbox for name and address
nametxt = gui_design1.textbox_design1(65, 10)
addresstxt = gui_design1.textbox_design1(85, 40)

#textbox for customer info and bill
customer_account_numbertxt = gui_design1.textbox_design1(380, 160)
balancetxt = gui_design1.textbox_design2(200, 190)
amount_duetxt = gui_design1.textbox_design2(25, 265)
due_datetxt = gui_design1.textbox_design2(200, 265)
total_amount_duetxt = gui_design1.textbox_design1(775, 240)

#textbox for service info
service_id_numbertxt = gui_design1.textbox_design3(200, 350)
contact_in_the_nametxt = gui_design1.textbox_design3(200, 400)
service_addresstxt = gui_design1.textbox_design3(200, 425)

#textbox for billing info
bill_datetxt = gui_design1.textbox_design3(200, 500)
meter_reading_datetxt = gui_design1.textbox_design3(200, 525)
bill_periodtxt = gui_design1.textbox_design3(200, 550)
due_date2txt = gui_design1.textbox_design3(200, 575)
total_kwhtxt = gui_design1.textbox_design3(200, 600)
total_current_amounttxt = gui_design1.textbox_design3(200, 625)
next_meter_readingtxt = gui_design1.textbox_design3(200, 650)

#text box for subtotal
subtotal1txt = gui_design1.textbox_design2(250, 750)
subtotal2txt = gui_design1.textbox_design2(250, 775)
subtotal3txt = gui_design1.textbox_design2(250, 800)
subtotal4txt = gui_design1.textbox_design2(250, 825)
subtotal5txt = gui_design1.textbox_design2(250, 850)
subtotal6txt = gui_design1.textbox_design2(250, 875)
subtotal7txt = gui_design1.textbox_design2(250, 900)
subtotal8txt = gui_design1.textbox_design2(250, 925)
subtotal9txt = gui_design1.textbox_design2(250, 950)

#textbox for percentage
percentage1txt = gui_design1.textbox_design2(450, 750)
percentage2txt = gui_design1.textbox_design2(450, 775)
percentage3txt = gui_design1.textbox_design2(450, 800)
percentage4txt = gui_design1.textbox_design2(450, 825)
percentage5txt = gui_design1.textbox_design2(450, 850)
percentage6txt = gui_design1.textbox_design2(450, 875)
percentage7txt = gui_design1.textbox_design2(450, 900)
percentage8txt = gui_design1.textbox_design2(450, 925)
percentage9txt = gui_design1.textbox_design2(450, 950)

#textbox for customer account in billing statement
customer_account_number2txt = gui_design2.textbox_design2(675, 350)
due_date3txt = gui_design2.textbox_design3(890, 350)
total_amounttxt = gui_design2.textbox_design1(700, 430)

#textbox for bill computation summary
remaining_balance_from_previous_billtxt = gui_design2.textbox_design4(915, 525)
charges_for_this_billing_period2txt = gui_design2.textbox_design4(915, 550)
generation2txt = gui_design2.textbox_design4(915, 575)
transmission2txt = gui_design2.textbox_design4(915, 600)
system_loss2txt = gui_design2.textbox_design4(915, 625)
distribution2txt = gui_design2.textbox_design4(915, 650)
subsidies2txt = gui_design2.textbox_design4(915, 675)
government_tax2txt = gui_design2.textbox_design4(915, 700)
universal_charges2txt = gui_design2.textbox_design4(915, 725)
fit2txt = gui_design2.textbox_design4(915, 750)
applied_creditstxt = gui_design2.textbox_design4(915, 775)
other_charges2txt = gui_design2.textbox_design4(915, 800)
installment_duetxt = gui_design2.textbox_design4(915, 825)
total_amount_due2txt = gui_design2.textbox_design5(870, 870)

#dding combo box for balance from previous billing
n = tk.StringVar()
combo_field = ttk.Combobox(window, width=10, textvariable=n)
combo_field['values'] = ('Thank You', 'Please Pay')
combo_field.place(x=300, y=190)
combo_field.current()

#adding combo box for rate in service info
n = tk.StringVar()
combo_field2 = ttk.Combobox(window, width=20, textvariable=n)
combo_field2['values'] = ('Residential', 'Commercial')
combo_field2.place(x=200, y=375)
combo_field2.current()

#call image to display
upload_image = gui_design1.image_design(r'C:\Users\Admin\PycharmProjects\PLDL01E\images\meralco.png', 895, 10, 90, 90)

window.mainloop()