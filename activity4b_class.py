import activity4a_class

obj = activity4a_class.student_data
student_name = input("Student Name: ")
course = input("Course: ")
student_number = input("Student Number: ")
academic_year = input("Academic Year: ")
date = input("Date: ")

section = []
subject = []
units = []

for i in range(5):
  section.append(input(f"Section {i + 1}: "))
  subject.append(input(f"Subject {i + 1}: "))
  units.append(float(input(f"Units {i + 1}: ")))

print("==================================================================================")
print("==================================================================================")
print("Student Name: ",student_name, "\t\t\t\t\tStudent Number: ", student_number)
print("Course: ", course, "\t\t\t\t\t\t\tAcademic Year: ", academic_year)
print("==================================================================================")
for i in range(5):
    print(f"\tSection: {section[i]} \t\t\t\t\tSubject: {subject[i]} \t\t\t\t\tUnits: {units[i]}")
print("==================================================================================")
print("==================================================================================")
