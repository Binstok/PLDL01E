import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk

from payroll_oop3 import department

window = tk.Tk()
window.title("Payroll Page")
window.geometry('900x1520')

class gui_interface():

    def __int__(self, frame1):
        frame1 = ''

    def frames(self, x, y):
        self.frame1 = Frame(window, width=1000, height=700, border=0, bg='black')

    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 11))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='light grey', font=('Arial', 11))
        self.textbox.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.label_design1 = Label(text=text_value, fg='black', font=('Arial', 10))
        self.label_design1.place(x=x, y=y)

    def label_design2(self, x, y, text2_value):
        self.label_design2 = Label(text=text2_value, fg='black', font=('Times New Roman', 30, 'bold'))
        self.label_design2.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.label_design3 = Label(text=text_value, fg='black', font=('Arial', 14, 'bold'))
        self.label_design3.place(x=x, y=y)

    def button_design(self, x, y):
        self.upload_button = Button(width=25, padx=10, text='SEARCH', bg='#FF0000', fg='white', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.place (x=x, y=y)

gui_design = gui_interface()

gui_design = gui_interface()
gui_design.frames(1500, 1500)

payrolllbl = gui_design.label_design2(200, 50, 'SE-RI`S CHOICE PAYROLL')
employee_basic_infolbl = gui_design.label_design3(20, 150, 'EMPLOYEE BASIC INFO: ')

employee_namelbl = gui_design.label_design1(40, 400, 'Employee Name: ')

window.mainloop()