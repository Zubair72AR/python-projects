"""
8. The super() Function
Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.
"""


class Person:  # Base Class
    def __init__(self, name: str):  # Constructor
        self.name = name  # Save Name


class Teacher(Person):  # Derived Class
    def __init__(self, name: str, subject: str):  # Constructor
        super().__init__(name)  # Call Base Class Constructor
        self.subject = subject  # Save Subject

    def show(self):  # Display Method
        print(f"Name: {self.name}, Subject: {self.subject}")  # Show Details


teacher_01 = Teacher("Sir Ali Aftab", "Python")  # Create Instance
teacher_01.show()  # Call Method
