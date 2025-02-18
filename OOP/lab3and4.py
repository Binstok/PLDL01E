class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.status = "Available"

# method for borrowing book
    def borrow_book(self):
        if self.status == "Available":
            self.status = "Borrowed"
            print(f"You Borrowed {self.title}.")
        else:
            print(f"{self.title} is not available")

#method for returning book
    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            print(f"{self.title} Have Been Returned.")
        else:
            print(f"{self.title} is Available")

#initialize object for books
books = [
    Book("English", "Yutaka", 2022),
    Book("Science", "Komiya", 2023),
    Book("Math", "Von", 2020)
]

# Display the list of book
print("LIST OF BOOKS")
for i, book in enumerate(books, start=1):
    print(f"{i}. {book.title} by {book.author} ({book.year_published}) - Status: {book.status}")

# Main loop for user interaction
while True:
    try:
        print("\nCHOOSE OPTIONS:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Exit")
        action = int(input("Enter your choice (1-3): "))

        if action == 3:
            print("Exiting program. Goodbye!")
            break

        elif action in [1, 2]:
            print("Select a book:")
            for i, book in enumerate(books, start=1):
                print(f"{i}. {book.title} ({book.status})")

            book_choice = int(input("Enter the number of the book: "))
            if 1 <= book_choice <= len(books):
                selected_book = books[book_choice - 1]
#borrow action
                if action == 1:
                    selected_book.borrow_book()
#return action
                elif action == 2:
                    selected_book.return_book()
            else:
                print("Invalid book number. Try again.")

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    except ValueError:
        print("Please enter a valid number.")

#class
class Student:
    # initialize
    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    # display function
    def display_student_info(self):
        print(f'Student ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Year Level: {self.year_level}')

#initialize object for class student
student1 = Student(1, 'Ryley', 'BSCpE', '2nd year')
student2 = Student(2, 'Von', 'BSCE', '3rd year' )
student3 = Student(3, 'Jester', 'BSME', '1st year')

#call to display student info
student1.display_student_info()
print('--------------------------------------------------------------------------------')
student2.display_student_info()
print('--------------------------------------------------------------------------------')
student3.display_student_info()


