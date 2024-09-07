#initialization student name, final quizzes, final research/assignment, final project, final grade, and equivalent mark
student_name =""
final_quizzes = 0
final_research_assignment = 0
final_project = 0
final_grade = 0
equivalent_mark= ""

#input student name, final quizzes, final research/assignment, final project, final exam
student_name = str(input("Enter student name:"))
final_quizzes = float(input("Enter Final quizzes:"))
final_research_assignment = float(input("Enter final research and assignment grade:"))
final_project = float(input("Enter Final project grade:"))
final_exam = float(input("Enter Final exam grade:"))

#setting formula to get final grade = 0.30 * final quizzes + 0.10 * final assignment/research + 0.40 * final exam + 0.20 final project
final_grade = 0.30*final_quizzes + 0.10*final_research_assignment + 0.40*final_exam + 0.20*final_project

#set the condition based on the final grade to it equivalent grade
if 98 <= final_grade <= 100:
    equivalent_mark = 4.00
elif 95 <= final_grade <= 97:
    equivalent_mark = 3.75
elif 92 <= final_grade <= 94:
    equivalent_mark = 3.50
elif 89 <= final_grade <= 91:
    equivalent_mark = 3.25
elif 86 <= final_grade <= 88:
    equivalent_mark = 3.00
elif 83 <= final_grade <= 85:
    equivalent_mark = 2.75
elif 80 <= final_grade <= 82:
    equivalent_mark = 2.50
elif 77 <= final_grade <= 79:
    equivalent_mark = 2.25
elif 74 <= final_grade <= 76:
    equivalent_mark = 2.00
elif 71 <= final_grade <= 73:
    equivalent_mark = 1.75
elif 68 <= final_grade <= 70:
    equivalent_mark = 1.50
elif 64 <= final_grade <= 67:
    equivalent_mark = 1.25
elif 60 <= final_grade <= 63:
    equivalent_mark = 1.00
else:
    equivalent_mark = 0

#print student name, final quizzes, final research/assignment, final project, final grade, and equivalent mark
print("Student name:", student_name)
print("Final quizzes grade:", final_quizzes)
print("Final research and assignment grade:", final_research_assignment)
print("Final project grade:", final_project)
print("Final grade:", final_grade)
print("Equivalent mark:", equivalent_mark)