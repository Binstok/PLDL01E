from tkinter import*
from PIL import Image, ImageTk

#first class gui_interface for frame, label, button design and image design
class gui_interface:

    def __int__(self, frame1):
        frame1 = ''

    def frames1(self, x, y):
        self.frame1 = Frame(width=780, height=150, bg='light grey', border=0)
        self.frame1.place(x=x, y=y)

    def frame2(self, x, y):
        self.frame1 = Frame(width=780, height=280, bg='light grey', border=0)
        self.frame1.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', font=('Algerian', 24, 'bold'))
        self.label.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='light grey', font=('Arial', 10))
        self.label.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', font=('Arial', 14, 'bold'))
        self.label.place(x=x, y=y)

    def label_design4(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='light grey', font=('Arial', 8))
        self.label.place(x=x, y=y)

    def button_design1(self, x, y):
        self.upload_button = Button(width=9, padx=2, text='Choose File', bg='#cacccb', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y):
        self.upload_button = Button(width=10, padx=5, text='Save', bg='#2a7cf7', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        self.upload_button = Button(width=10, padx=5, text='Cancel', bg='#fafbfc', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(image=self.bck_pic)
        self.lbl.place (x=x, y=y)

#second class gui_interface_textbox for textbox designs
class gui_interface_textbox():
    def __int__(self):
        frame2 = ''

    def textbox_design1(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='white', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=10, height=1, fg='black', bg='white', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=56, height=1, fg='black', bg='white', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def textbox_design4(self, x, y):
        self.textbox = Text(width=42, height=1, fg='black', bg='white', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def textbox_design5(self, x, y):
        self.textbox = Text(width=100, height=1, fg='black', bg='white', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def textbox_design6(self, x, y):
        self.textbox = Text(width=49, height=1, fg='black', bg='white', font=('Arial', 10))
        self.textbox.place(x=x, y=y)
