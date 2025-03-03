class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' has been borrowed.")
        else:
            print(f"Book '{self.title}' is not available for borrowing.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Book '{self.title}' has been returned.")
        else:
            print(f"Book '{self.title}' is already available.")

    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {availability}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book)
                return
        print(f"Book with title '{title}' not found in the library.")


# Implementation
# Step 1: Create a library
library = Library()

# Step 2: Create at least three books
book1 = Book("1984", "George Orwell", "9780451524935")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")

# Step 3: Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Step 4: Display all books in the library
library.display_books()

# Step 5: Search for a book by title
library.search_book("1984")

# Step 6: Borrow a book and display updated status
book1.borrow_book()
library.display_books()

# Step 7: Return a book and display updated status
book1.return_book()
library.display_books()