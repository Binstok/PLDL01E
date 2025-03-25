class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary:.2f}")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print("Position: Manager")


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")
        print("Position: Developer")


def show_employee_details(employee):
    employee.display_info()
    print("-" * 30)


# Create employee objects
manager = Manager("John Doe", 1001, 75000.00, "Engineering")
developer = Developer("Jane Smith", 1002, 65000.00, "Python")

# Store in a list
employees = [manager, developer]

# Display all employees
for emp in employees:
    show_employee_details(emp)