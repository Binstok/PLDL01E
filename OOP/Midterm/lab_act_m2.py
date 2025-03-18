#Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f'Name: {self.name}, Age: {self.age}'

#Derived class for student (inheritance)
class Student(Person):
    def __init__(self, name, age, grade_level):
        super().__init__(name, age)
        self.grade_level = grade_level

    # Overriding display_info method (Polymorphism)
    def display_student_info(self):
        return f'Student Name: {self.name}, Age: {self.age}, Grade level: {self.grade_level}'

#Derived class for Teacher (inheritance)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # Overriding display_info method (Polymorphism)
    def display_teacher_info(self):
        return f'Teacher Name: {self.name}, Age: {self.age}, Subject: {self.subject}'

#Creating objects
student = Student('Ryley Vince Legaspi', 19, '2ng Year')
teacher = Teacher('ENGR. Toni', 30, 'OOP')

#displaying the method for both student and teacher
print(student.display_student_info())
print(teacher.display_teacher_info())
