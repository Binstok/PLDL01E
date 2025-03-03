from tkinter import*
from PIL import Image, ImageTk

class gui_interface():

    def __int__(self, frame1):
        frame1 = ''

    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='light grey', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', font=('Arial', 10))
        self.label.place(x=x, y=y)

    def label_design2(self, x, y, text2_value):
        self.label= Label(text=text2_value, fg='black', font=('Algerian', 40, 'bold'))
        self.label.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', font=('Arial', 12, 'bold'))
        self.label.place(x=x, y=y)

    def button_design(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='SEARCH', bg='#ed2626', fg='white', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_desing2(self, x, y):
        self.upload_button = Button(width=12, padx=10, text='GROSS INCOME', bg='#1568ed', fg='white', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='NET INCOME', bg='#1568ed', fg='white', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design4(self, x, y):
        self.upload_button = Button(width=5, padx=10, text='SAVE', bg='#49afbf', fg='white', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design5(self, x, y):
        self.upload_button = Button(width=5, padx=10, text='UPDATE', bg='#49afbf', fg='white', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design6(self, x, y):
        self.upload_button = Button(width=5, padx=10, text='NEW', bg='#edd539', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(image=self.bck_pic)
        self.lbl.place (x=x, y=y)