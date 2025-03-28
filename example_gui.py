import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Employee Registration")
window.geometry('1520x900')

class design_gui_interface() :
    def __int__(self, frame1):
        frame1 = ''
    def frames(self,x, y):
        self.frame1 = Frame (window, width=1100, height=160, border=0, bg='light gray')
        self.frame1.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=31, height=1, fg='black', bg='white', font=('Arial',11, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='light gray', font=('Calibre', 10))
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y):
        self.upload_button = Button(width=15, padx=7, text='Choose File', bg='#57a1f8', fg='white', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.place (x=x, y=y)

my_gui_design = design_gui_interface()
#displaying the frames create
#instantiation of the class
my_gui_design = design_gui_interface()
#call frames attribute within the class named as design_gui_interface
#call for frame 1
my_gui_design.frames(200, 220)
#call for frame 2
my_gui_design.frames(200, 390)
#call for frame 3
my_gui_design.frames(200, 560)

firstnametxt = my_gui_design.textbox_design1(440, 262)
middle_nametxt = my_gui_design.textbox_design1(x=649, y=262)
surnametxt = my_gui_design.textbox_design1(x=858, y=262)
suffixtxt = my_gui_design.textbox_design1(1067, 262)
date_of_birthtxt = my_gui_design.textbox_design1(440, 330)
nationalitytxt = my_gui_design.textbox_design1(1067, 330)

departmenttxt = my_gui_design.textbox_design2(232,500)
designationtxt = my_gui_design.textbox_design2(495, 500)
employee_statustxt = my_gui_design.textbox_design2(760, 500)
employee_numbertxt = my_gui_design.textbox_design2(1025,500)
contact_numbertxt = my_gui_design.textbox_design2(232, 435)
email_addresstxt = my_gui_design.textbox_design2(495, 435)
other_socail_mediatxt = my_gui_design.textbox_design2(760, 435)
social_media_accounnttxt = my_gui_design.textbox_design2(1025, 435)

address_line1txt = my_gui_design.textbox_design2(232, 600)
adress_line2txt = my_gui_design.textbox_design2(495,600)
baranggaytxt = my_gui_design.textbox_design2(760, 600)
municipalitytxt = my_gui_design.textbox_design2(1025, 600)
provincetxt = my_gui_design.textbox_design2(232, 670)
zip_codetxt = my_gui_design.textbox_design2(760, 670)
countrytxt = my_gui_design.textbox_design2(495, 670)
picturepathtxt = my_gui_design.textbox_design2(1025, 670)

firstname_lbl = my_gui_design.label_design(440, 235, 'Firstname')
middle_namelbl = my_gui_design.label_design(650, 235, 'Middlename')
surnamelbl = my_gui_design.label_design(858, 235, 'Surname')
suffixlbl = my_gui_design.label_design(1067, 240, 'Suffix')
date_of_birthlbl = my_gui_design.label_design(440, 305, 'Date of Birth')
nationalitylbl = my_gui_design.label_design(1067, 305, 'Natioanality')
civil_statuslbl = my_gui_design.label_design(858, 305, 'Civil Status')
genderlbl = my_gui_design.label_design(650, 305, 'Gender')

departmentlbl = my_gui_design.label_design(232, 410, 'Department')
designationlbl = my_gui_design.label_design(498, 410, 'Designation')
employee_statuslb = my_gui_design.label_design(764, 410, 'Employee Status')
employee_numberlbl = my_gui_design.label_design(1030, 410, 'Employee Number')
employee_numberlbl = my_gui_design.label_design(232, 475, 'Employee Contact Number')
email_addresslbl = my_gui_design.label_design(498, 475, 'Email Address')
other_socail_medialbl = my_gui_design.label_design(764, 475, 'Other Social Media Account')
social_media_accounntlbl = my_gui_design.label_design(1030, 475, 'Social Media Account')

address_line1txt = my_gui_design.label_design(232, 575, 'Address Line 1')
address_line2txt = my_gui_design.label_design(495, 575, 'Address line 2')
baranggaytxt = my_gui_design.label_design(760, 575, 'Baranggay')
municipalitytxt = my_gui_design.label_design(1025, 575, 'Municipality')
provincetxt = my_gui_design.label_design(232, 645, 'Province')
zip_codetxt = my_gui_design.label_design(498, 645, 'Zip Code')
countrytxt = my_gui_design.label_design(764, 645, 'Country')
picturepathtxt = my_gui_design.label_design(1024, 645, 'Picture Path of Upload Image')

n = tk.StringVar()
combo_field = ttk.Combobox(window, width=30, textvariable=n)
combo_field['values'] = ('Female', 'Male', 'Unidentified')
combo_field.place(x=649, y=330)
combo_field.current()


n = tk.StringVar()
combo_field = ttk.Combobox(window, width=30, textvariable=n)
combo_field1 = ttk.Combobox(window, width=30, textvariable=n)
combo_field1['values'] = ('Single', 'Married', 'Widow', 'Legally', 'Separated', 'Annulled')
combo_field1.place(x=858, y=330)
combo_field.current()

upload_image = my_gui_design.image_design(r'C:\Users\Admin\PycharmProjects\PLDL01E\images\1.png', 222, 110, 200, 180)


upload_button = my_gui_design.button_design(263, 300)

window.mainloop()
