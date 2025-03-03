import tkinter as tk

#call and import classes from project then login_page_clasess
from Project.login_page_classes import gui_interface

#window
window = tk.Tk()
window.title('LOGIN PAGE')
window.geometry('1400x800')

#call the classes
obj = gui_interface
gui_design = gui_interface()

#upload the image
upload_image = gui_design.image_design(r'C:\Users\Admin\PycharmProjects\PLDL01E\images\login_page.jpg', 0, 0, 1400, 800)

#display the frame
gui_design.frame1(280,120)

#text for login page
player_loginlbl = gui_design.label_design1(550, 150, 'Player`s Login')
usernamelbl = gui_design.label_design2(450, 260, 'Enter email/username')
passwordlbl = gui_design.label_design2(450, 340, 'Enter Password')
login_withlbl = gui_design.label_design3(668, 520, 'Log in with')

#textbox for login page
usernametxt = gui_design.textbox_design1(450, 280)
passwordtxt = gui_design.textbox_design1(450, 360)

#upload all the buttons
upload_button1 = gui_design.button_design1(450, 400)
upload_button2 = gui_design.button_design2(835, 400)
upload_button3 = gui_design.button_design3(500, 450)
upload_button4 = gui_design.button_design5(520, 550)
upload_button5 = gui_design.button_design4(645, 550)
upload_button6 = gui_design.button_design6(770, 550)

window.mainloop()