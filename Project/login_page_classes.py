from tkinter import*
from PIL import Image, ImageTk

#class for gui interface
class gui_interface:

    def __int__(self, frame1):
        frame1 = ''

    def frame1(self, x, y):
        self.frame1 = Frame (width=800, height=500, bg='white', border=0)
        self.frame1.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='white', font=('Castellar', 24, 'bold'))
        self.label.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='white', font=('Arial', 12, 'bold'))
        self.label.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.label = Label(text=text_value, fg='black', bg='white', font=('Arial', 8))
        self.label.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=40, height=1, fg='black', bg='white', font=('Arial', 16, 'bold'))
        self.textbox.place(x=x, y=y)

    def button_design1(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='Register now', bg='#f7c025', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='Forget password', bg='#f7c025', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        self.upload_button = Button(width=50, height=2, padx=10, text='Log in', bg='#f5f1e6', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design4(self, x, y):
        self.upload_button = Button(width=10, height=1, padx=10, text='Facebook', bg='#47a5fc', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design5(self, x, y):
        self.upload_button = Button(width=10, height=1, padx=10, text='Google', bg='#faf9f7', fg='black', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)

    def button_design6(self, x, y):
        self.upload_button = Button(width=10, height=1, padx=10, text='Twittier', bg='#141414', fg='white', cursor='hand2', border=2)
        self.upload_button.place(x=x, y=y)


    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(image=self.bck_pic)
        self.lbl.place (x=x, y=y)

