
class student_data:
#input all the data needed
    def __init__(self):
        self.student_name = ""
        self.course = ""
        self.student_number = 0
        self.academic_year = ""
        self.date = ""
        self.section = 0
        self.subject = ""
        self.units = 0

    def get_student_data(self, student_name, course, student_number, academic_year, date, section, subject, units ):
        self.student_name = student_name
        self.course = course
        self.student_number = student_number
        self.academic_year = academic_year
        self.date = date
        self.section = section
        self.subject = subject
        self.units = units

    def display_student_data(self):
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

class student_fee:
    def __init__(self):
        #input Assessment fees
        self.adu_chronicle = 0
        self.athletic = 0
        self.audio_visual_library = 0
        self.ausg = 0
        self.cultural_fee = 0
        self.energy_cost_aircon_classroom = 0
        self.guidance = 0
        self.insurance_fee = 0
        self.learning_management_system = 0
        self.library_fee = 0
        self.medical_and_dental = 0
        self.registration = 0
        self.rso = 0
        self.student_activities_fee = 0
        self.student_nurturance_fee = 0
        self.technology_fee = 0
        self.test_papers = 0
        self.downpayment = 0


    def computation_tuition_fee_lecture(self):
        total_units = sum(self.units)
        self.tuition_fee_lecture = float(1551.00 * total_units)
        return self.tuition_fee_lecture
    def computation_assessment_amount(self):
        self.assessment_amount = self.tuition_fee_lecture + self.adu_chronicle + self.athletic + self.audio_visual_library + self.ausg + self.cultural_fee + self.energy_cost_aircon_classroom + self.guidance + self.insurance_fee + self.learning_management_system + self.library_fee + self.medical_and_dental + self.registration + self.rso + self.student_activities_fee + self.student_nurturance_fee + self.technology_fee + self.test_papers
        return self.assessment_amount
    def computation_total_due(self):
        self.total_due = self.assessment_amount - self.downpayment
        return self.total_due
    def computation_balance(self):
        self.balance = self.total_due/3
        return self.balance


