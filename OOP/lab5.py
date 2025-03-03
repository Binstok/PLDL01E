class Book:

    def __init__(self, title, author, isbn, availability):
        self.title =  title
        self.author =  author
        self.isbn = isbn
        self.availability = availability

    def borrow_bok(self, availability):
        self.availability = availability

    def return_book(self, availability):
        self.availability = availability

    def display_book(self):
        print(f'Title: {self.title}, Author: {self.author}, International Standard Book Number: {self.isbn}, Availability: {self.availability}')

class Library():
    def __init__(self):
        self.book = []

     def add_book(self):

library = Library()

book1 = Book('The Great Gatsby', 'Ryley', 20123432, 'True')
book2 = Book('1984', 'Jester', 12315343, 'True')
book3 = Book('To Kill a Mockingbird', 'Von', 734124332, 'True')

book1.display_book()




