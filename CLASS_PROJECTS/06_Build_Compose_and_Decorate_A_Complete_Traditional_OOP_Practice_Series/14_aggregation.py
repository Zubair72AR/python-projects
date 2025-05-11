"""
14. Aggregation
Assignment:
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
"""


class Employee:  # Class
    def __init__(self, name):  # Constructor
        self.name = name  # Save Employee Name


class Department:  # Class
    def __init__(self, employee):  # Constructor accepting Employee object
        self.employee = employee  # Store Employee object reference


# Example Usage
emp1 = Employee("Ali")  # Create Employee Object
dept1 = Department(emp1)  # Pass Employee Object to Department
# Access Employee Name via Department
print(f"Employee Name in Department: {dept1.employee.name}")
