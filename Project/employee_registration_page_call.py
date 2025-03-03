import tkinter as tk
from tkinter import ttk

#call and import classes from project then employee_registration_page_classess
from Project.employee_registration_page_classes import gui_interface, gui_interface_textbox

#window
window = tk.Tk()
window.title('EMPLOYEE REGISTRATION PAGE')
window.geometry('800x1400')

#call the classes
obj = gui_interface
gui_design = gui_interface()
gui_design2 = gui_interface_textbox()

#display the frames
gui_design.frames1(10, 150)
gui_design.frames1(10, 320)
gui_design.frames1(10, 520)
gui_design.frame2(10, 720)

#label for the first frame
titlelbl = gui_design.label_design1(47, 30, 'SE-RI`S EMPLOYEE PERSONAL INFORMATION')
firstnamelbl = gui_design.label_design2(200, 160, 'First Name' )
middle_namelbl = gui_design.label_design2(350, 160, 'Middle Name')
last_namelbl = gui_design.label_design2(500, 160, 'Last Name')
suffixlbl = gui_design.label_design2(650, 160, 'Suffix')
date_of_birthlbl = gui_design.label_design2(200, 220, 'Date of Birth')
genderlbl = gui_design.label_design2(350, 220, 'Gender')
nationalitylbl = gui_design.label_design2(480, 220, 'Nationality')
civilstatuslbl = gui_design.label_design2(610, 220, 'Civil Status')
no_file_chosenlbl = gui_design.label_design4(90, 235, 'No File Chosen')

#label for the second frame
departmentlbl = gui_design.label_design2(25, 330, 'Department')
designationlbl = gui_design.label_design2(430, 330, 'Designation')
qua_dept_statuslbl = gui_design.label_design2(580, 330, 'Qualified Dep. Status')
employee_statuslbl = gui_design.label_design2(25, 390, 'Employee Status')
paydatelbl = gui_design.label_design2(430, 390, 'Paydate')
employee_numberlbl = gui_design.label_design2(580, 390, 'Employee Number')

#label for the third frame (contact infoormation)
contact_infolbl = gui_design.label_design3(10, 490, 'Contact Information')
contact_numberlbl = gui_design.label_design2(25, 530, 'Contact No.')
emaillbl = gui_design.label_design2(330, 530, 'Email Address')
other_social_medialbl = gui_design.label_design2(25, 590, 'Other(Social Media)')
social_media_accountidlbl = gui_design.label_design2(330, 590, 'Social Media Account ID/No.')

#label for the fourth frame (address)
addresslbl = gui_design.label_design3(10, 690, 'Address')
address_line1lbl = gui_design.label_design2(25, 730, 'Address Line 1')
address_line2lbl = gui_design.label_design2(25, 780, 'Address Line 2')
city_municipalitylbl = gui_design.label_design2(25, 830, 'City/Municipality')
state_provincelbl = gui_design.label_design2(382, 830, 'State/Province')
countrylbl = gui_design.label_design2(25, 880, 'Country' )
zip_codelbl = gui_design.label_design2(382, 880, 'Zipe Code')
picture_pathlbl = gui_design.label_design2(25, 930, 'Picture Path')

#textbox for the first frame
firstnametxt = gui_design2.textbox_design1(200, 180)
middle_nametxt = gui_design2.textbox_design1(350, 180)
last_nametxt = gui_design2.textbox_design1(500, 180)
suffixtxt = gui_design2.textbox_design2(650, 180)
date_of_birthtxt = gui_design2.textbox_design1(200, 240)

#textbox for the second frame
departmenttxt = gui_design2.textbox_design3(25, 350)
designationtxt = gui_design2.textbox_design1(430, 350)
qua_dept_statustxt = gui_design2.textbox_design1(580, 350)
employee_statustxt = gui_design2.textbox_design3(25, 410)
paydatetxt = gui_design2.textbox_design1(430, 410)
employee_numbertxt = gui_design2.textbox_design1(580, 410)

#textbox for the third frame (contact infoormation)
contact_numbertxt = gui_design2.textbox_design4(25, 550)
emailtxt = gui_design2.textbox_design3(330, 550)
social_media_accountidtxt = gui_design2.textbox_design3(330, 610)

#textbox for the fourth frame (address)
address_line1txt = gui_design2.textbox_design5(25, 750)
address_line2txt = gui_design2.textbox_design5(25, 800)
city_municipalitytxt = gui_design2.textbox_design6(25, 850)
state_provincetxt = gui_design2.textbox_design6(382, 850)
zip_codetxt = gui_design2.textbox_design1(382, 900)

#upload the buttons
upload_button1 = gui_design.button_design1(15, 230)
upload_button2 = gui_design.button_design2(10, 1010)
upload_button3 = gui_design.button_design3(110, 1010)

#adding combo box for gender
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=17, textvariable=n)
combo_field1['values'] = ('Male', 'Female')
combo_field1.place(x=350, y=240)
combo_field1.current()

#adding combo box for nationality
n = tk.StringVar()
combo_field2 = ttk.Combobox(window, width=17, textvariable=n)
combo_field2['values'] = ('Filipino', 'Citizen of different country')
combo_field2.place(x=480, y=240)
combo_field2.current()

#adding combo box for civil status
n = tk.StringVar()
combo_field3 = ttk.Combobox(window, width=15, textvariable=n)
combo_field3['values'] = ('Single', 'Married', 'Widow', 'Legally', 'Separated', 'Annulled')
combo_field3.place(x=610, y=240)
combo_field3.current()

#adding combo box for other social media
n = tk.StringVar()
combo_field4 = ttk.Combobox(window, width=46, textvariable=n)
combo_field4['values'] = ('Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok', 'Snapchat', 'Telegram')
combo_field4.place(x=25, y=610)
combo_field4.current()

#adding combo box for country
n = tk.StringVar()
combo_field5 = ttk.Combobox(window, width=54, textvariable=n)
combo_field5['values'] = ('Philippines', 'China', 'Singapore', 'Japan', 'Thailand', 'Malaysia', 'Indonesia', 'Cambodia', 'Myanmar', 'Bangladesh')
combo_field5.place(x=25, y=900)
combo_field5.current()

#call and upload the image
upload_image = gui_design.image_design(r'C:\Users\Admin\PycharmProjects\PLDL01E\images\1.png', 10, 90, 125, 125)

window.mainloop()