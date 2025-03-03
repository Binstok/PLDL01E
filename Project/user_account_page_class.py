from tkinter import*
from PIL import Image, ImageTk

#class for gui interface
class gui_interface() :

    def __int__(self, frame1):
        frame1 = ''

    def frames(self,x, y):
        self.frame1 = Frame (width=900, height=350, border=0, bg='light gray')
        self.frame1.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', font=('Calibre', 20, 'bold'))
        self.label.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='light grey', font=('Arial', 10))
        self.label.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=15, height=1, fg='black', bg='light grey', font=('Arial', 12))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='light grey', font=('Arial', 12))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='white', font=('Arial', 12))
        self.textbox.place(x=x, y=y)

    def textbox_design4(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 12))
        self.textbox.place(x=x, y=y)

    def button_design1(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='Update', bg='#3d70fc', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='Delete', bg='#fce249', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='Cancel', bg='#D3D3D3', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(image=self.bck_pic)
        self.lbl.place (x=x, y=y)
