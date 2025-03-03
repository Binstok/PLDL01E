import tkinter as tk

##call and import classes from project then user_account_page class
from Project.user_account_page_class import gui_interface

#window
window = tk.Tk()
window.title("User Account Page")
window.geometry('1000x600')

#call the class
obj = gui_interface
gui_design = gui_interface()

#display the frame
gui_design.frames(50, 180)

#text for the gui
titlelbl = gui_design.label_design1(50, 20, 'User Account Information')
firstnamelbl = gui_design.label_design2(220, 200, 'First Name')
middle_namelbl = gui_design.label_design2(365, 200, 'Middle Name')
last_namelbl = gui_design.label_design2(510,200, 'Last Name')
suffixlbl = gui_design.label_design2(655,200, 'Suffix')
departmentlbl = gui_design.label_design2(800, 200, 'Department')
designationlbl = gui_design.label_design2(70, 280, 'Designation')
usernamelbl = gui_design.label_design2(305, 280, 'Username')
passwordlbl = gui_design.label_design2(495, 280, 'Password')
confirm_passwordlbl = gui_design.label_design2(70, 360, 'Confirm Password')
user_typelbl = gui_design.label_design2(305, 360, 'User Type')
user_statuslbl = gui_design.label_design2(495, 360, 'User Status')
employee_numberlbl = gui_design.label_design2(685, 360, 'Employee Number')

#textbox for the gui
firstnametxt = gui_design.textbox_design1(220, 220)
middle_nametxt = gui_design.textbox_design1(365, 220)
last_nametxt = gui_design.textbox_design1(510, 220)
suffixtxt = gui_design.textbox_design1(655, 220)
departmenttxt = gui_design.textbox_design1(800, 220)
designationtxt = gui_design.textbox_design2(70, 300)
usernametxt = gui_design.textbox_design3(305, 300)
passwordtxt = gui_design.textbox_design4(495, 300)
confirm_passwordtxt = gui_design.textbox_design4(70, 380)
user_typetxt = gui_design.textbox_design3(305, 380)
user_statustxt = gui_design.textbox_design3(495, 380)
employee_numbertxt = gui_design.textbox_design3(685, 380)

#upload the button
upload_button1 = gui_design.button_design1(630, 450)
upload_button2 = gui_design.button_design2(735, 450)
upload_button3 = gui_design.button_design3(840, 450)

#call and upload the image
upload_image = gui_design.image_design(r'C:\Users\Admin\PycharmProjects\PLDL01E\images\1.png', 55, 100, 145, 145)

window.mainloop()