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
