
class student_data:
#input all the data needed
    def __init__(self):

        self.student_name = input("Student Name: ")
        self.course = input("Course: ")
        self.student_number = input("Student Number: ")
        self.academic_year = input("Academic Year: ")
        self.date = input("Date: ")

        self.section = []
        self.subject = []
        self.units = []

        for i in range(5):
            self.section.append(input(f"Section {i + 1}: "))
            self.subject.append(input(f"Subject {i + 1}: "))
            self.units.append(float(input(f"Units {i + 1}: ")))

    def display_student_info(self):
        print("==================================================================================")
        print("==================================================================================")
        print("Student Name: ", self.student_name, "\t\t\t\t\tStudent Number: ", self.student_number)
        print("Course: ", self.course, "\t\t\t\t\t\t\tAcademic Year: ", self.academic_year)
        print("==================================================================================")
        for i in range(5):
            print(f"\tSection: {self.section[i]} \t\t\t\t\tSubject: {self.subject[i]} \t\t\t\t\tUnits: {self.units[i]}")
        print("==================================================================================")
        print("==================================================================================")




emp1 = student_data()
emp1.display_student_info()