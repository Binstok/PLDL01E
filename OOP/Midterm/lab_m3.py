#Base class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        return f'Name: {self.name}, Employee ID: {self.employee_id}, Salary: ${self.salary}'

#Derived class for manager
class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super(). __init__(name, employee_id, salary)
        self.department = department

    def display_info(self):
        return f'[Manager] Name: {self.name}, Employee ID: {self.employee_id}, Salary: ${self.salary}, Department: {self.department}'

#Derived class for Developer
class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super(). __init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        return f'[Developer] Name: {self.name}, Employee ID: {self.employee_id}, Salary: ${self.salary}, Programming Language: {self.programming_language}'

#Derived class for Intern
class Intern(Employee):
    def __init__(self, name, employee_id, salary, duration):
        super(). __init__(name, employee_id, salary)
        self.duration = duration

    def display_info(self):
        return f'[This Employee is Intern] Name: {self.name}, Employee ID: {self.employee_id}, Salary: ${self.salary}, Duration: {self.duration} months'

def show_employee_details(employee):
    print(employee.display_info())

# Create objects
manager = Manager('Alice', 101, 80000, 'HR')
developer = Developer('Bob', 102, 75000, 'Python')
intern = Intern('Ryley', 103, 40000, 3)

#Store in a list
employees = [manager, developer, intern]

# Display all employees
for emp in employees:
    show_employee_details(emp)

