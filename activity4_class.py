
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

        #input Assessment fees
        self.adu_chronicle = float(input("AdU Chronicle: "))
        self.athletic = float(input("Athletic: "))
        self.audio_visual_library = float(input("Auio Visual Library: "))
        self.ausg = float(input("AUSG: "))
        self.cultural_fee = float(input("Cultural Fee: "))
        self.energy_cost_aircon_classroom = float(input("Energy Cost Aircon Classroom: "))
        self.guidance = float(input("Guidance: "))
        self.insurance_fee = float(input("Insurance fee: "))
        self.learning_management_system = float(input("Learning Management System: "))
        self.library_fee = float(input("Library fee: "))
        self.medical_and_dental = float(input("Medical and Dental Fee: "))
        self.registration = float(input("Registration: "))
        self.rso = float(input("RSO: "))
        self.student_activities_fee = float(input("Student Activities Fee: "))
        self.student_nurturance_fee = float(input("Student Nurturance Fee: "))
        self.technology_fee = float(input("Technology Fee: "))
        self.test_papers = float(input("Test paper: "))
        self.downpayment = float(input("Downpayment: "))

    def computation_tuition_fee_lecture(self):
        total_units = sum(self.units)
        self.tuition_fee_lecture = float(1551.00 * total_units)

    def computation_assessment_amount(self):
        self.assessment_amount = self.tuition_fee_lecture + self.adu_chronicle + self.athletic + self.audio_visual_library + self.ausg + self.cultural_fee + self.energy_cost_aircon_classroom + self.guidance + self.insurance_fee + self.learning_management_system + self.library_fee + self.medical_and_dental + self.registration + self.rso + self.student_activities_fee + self.student_nurturance_fee + self.technology_fee + self.test_papers

    def computation_total_due(self):
        self.total_due = self.assessment_amount - self.downpayment

    def computation_balance(self):
        self.balance = self.total_due/3

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
        print("Tuition Fee: ", self.tuition_fee_lecture)
        print("AdU Chronicle: ", self.adu_chronicle)
        print("Athletic: ", self.athletic)
        print("Audio-Visual Library: ", self.audio_visual_library)
        print("AUSG: ", self.ausg)
        print("Cultural Fee: ", self.cultural_fee)
        print("Energy Cost, Aircon Classroom: ", self.energy_cost_aircon_classroom)
        print("Guidance: ", self.guidance)
        print("Insurance Fee: ", self.insurance_fee)
        print("Learning Management System: ", self.learning_management_system)
        print("Library Fee: ", self.library_fee)
        print("Medical and Dental: ", self.medical_and_dental)
        print("Registration: ", self.registration)
        print("RSO: ", self.rso)
        print("Student Activities Fee: ", self.student_activities_fee)
        print("Student Nurturance Fee: ", self.student_nurturance_fee)
        print("Technology Fee: ", self.technology_fee)
        print("Test Papers: ", self.test_papers)
        print("==================================================================================")
        print("Assessment Amount: ", self.assessment_amount)
        print("Downpayment: ", self.downpayment)
        print("==================================================================================")
        print("Total Due: ", self.total_due)
        print("")
        print("")
        print("")
        print("Prelims: ", self.balance)
        print("Midterms: ", self.balance)
        print("Finals: ", self.balance)
        print("==================================================================================")



emp1 = student_data()
emp1.computation_tuition_fee_lecture()
emp1.computation_assessment_amount()
emp1.computation_total_due()
emp1.computation_balance()
emp1.display_student_info()
S