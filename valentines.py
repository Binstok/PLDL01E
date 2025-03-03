import tkinter as tk
from tkinter import*
from tkinter import messagebox

window = tk.Tk()
window.title("Valentines Date")
window.geometry('600x400')

class gui_interface():

    def __int__(self, frame):
        frame = ''

    def frame1(self, x, y):
        self.frame1 = Frame (window, width=580, height=380, bg='#e882cf')
        self.frame1.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.label = Label (text=text_value, bg='light pink', font=('Blackadder ITC', 24))
        self.label.place(x=x, y=y)

    def button_design(self, x, y, command):
        self.upload_button = Button(width=10, padx=10, text='YES or NO', bg='#e882cf', fg='black', cursor='hand2', border=2
                                    , command=command)
        self.upload_button.place(x=x, y=y)

    def ask_valentine(self):
        response = messagebox.askyesno("Valentine's Day", "Will you be my Valentine?")
        if response:
            messagebox.showinfo("Yay!", "I'm so happy! ❤️, it's on February 15(Saturday), museum Date and dinner date.")
        else:
            messagebox.showinfo("Oh no!", "Maybe next time! 💔, kawawa binstok huhuhu")

my_gui_design = gui_interface()

my_gui_design.frame1(10,10)

will = my_gui_design.label_design1(140, 75, "Will you be my Valentine?")

button = my_gui_design.button_design(240, 200, my_gui_design.ask_valentine)


window.mainloop()

