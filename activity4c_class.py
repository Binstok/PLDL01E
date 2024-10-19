import activity4a_class

student_tuition_fee = activity4a_class.student_fee
section = []
subject = []
units = []

for i in range(5):
  section.append(input(f"Section {i + 1}: "))
  subject.append(input(f"Subject {i + 1}: "))
  units.append(float(input(f"Units {i + 1}: ")))

adu_chronicle = float(input("AdU Chronicle: "))
athletic = float(input("Athletic: "))
audio_visual_library = float(input("Auio Visual Library: "))
ausg = float(input("AUSG: "))
cultural_fee = float(input("Cultural Fee: "))
energy_cost_aircon_classroom = float(input("Energy Cost Aircon Classroom: "))
guidance = float(input("Guidance: "))
insurance_fee = float(input("Insurance fee: "))
learning_management_system = float(input("Learning Management System: "))
library_fee = float(input("Library fee: "))
medical_and_dental = float(input("Medical and Dental Fee: "))
registration = float(input("Registration: "))
rso = float(input("RSO: "))
student_activities_fee = float(input("Student Activities Fee: "))
student_nurturance_fee = float(input("Student Nurturance Fee: "))
technology_fee = float(input("Technology Fee: "))
test_papers = float(input("Test paper: "))
downpayment = float(input("Downpayment: "))

total_units = sum(units)
tuition_fee_lecture = float(1551.00 * total_units)
assessment_amount = tuition_fee_lecture + adu_chronicle + athletic + audio_visual_library + ausg + cultural_fee + energy_cost_aircon_classroom + guidance + insurance_fee + learning_management_system + library_fee + medical_and_dental + registration + rso + student_activities_fee + student_nurturance_fee + technology_fee + test_papers
total_due = assessment_amount - downpayment
balance = total_due / 3

print("Tuition Fee: ", tuition_fee_lecture)
print("AdU Chronicle: ", adu_chronicle)
print("Athletic: ", athletic)
print("Audio-Visual Library: ", audio_visual_library)
print("AUSG: ", ausg)
print("Cultural Fee: ", cultural_fee)
print("Energy Cost, Aircon Classroom: ", energy_cost_aircon_classroom)
print("Guidance: ", guidance)
print("Insurance Fee: ", insurance_fee)
print("Learning Management System: ", learning_management_system)
print("Library Fee: ", library_fee)
print("Medical and Dental: ", medical_and_dental)
print("Registration: ", registration)
print("RSO: ", rso)
print("Student Activities Fee: ", student_activities_fee)
print("Student Nurturance Fee: ", student_nurturance_fee)
print("Technology Fee: ", technology_fee)
print("Test Papers: ", test_papers)
print("==================================================================================")
print("Assessment Amount: ", assessment_amount)
print("Downpayment: ", downpayment)
print("==================================================================================")
print("Total Due: ", total_due)
print("")
print("")
print("")
print("==================================================================================")
print("Prelims: ", balance)
print("Midterms: ", balance)
print("Finals: ", balance)
print("==================================================================================")