#Base class
class Student:
#initialize the name and grade
    def __init__(self, name):
        self.name = name
        self._grade = []

 #Method to add a grade to the student's grade list
    def add_grade(self, grade):
        if isinstance(grade, int):
            self._grade.append(grade)
        else:
            print('Grade must be Intiger')

#Method to calculate and return the average grade
    def get_average(self):
        if not self._grade:
            return 0
        return sum(self._grade) / len(self._grade)

#Method to get the student's name
    def get_name(self):
        return self.name

#Create an instance of Student
student = Student('Ryley Vince')

#Add grades to the student's record
student.add_grade(95)
student.add_grade(98)
student.add_grade(90)

#Display the output
print(f'Name: {student.get_name()}, Average Grade: {student.get_average():.2f}')