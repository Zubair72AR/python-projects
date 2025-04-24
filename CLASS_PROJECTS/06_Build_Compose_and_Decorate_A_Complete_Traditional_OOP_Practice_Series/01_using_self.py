"""
1. Using self
Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.
"""


class Student:  # Class
    def __init__(self, name, marks):  # Initialize via a Constructor
        self.name = name  # Save Name in (Instance) Variable
        self.marks = marks  # Save Marks

    def display(self):  # Instance Method
        print(f"Name: {self.name}\nMarks: {self.marks}")  # Print Details


student_01 = Student("Babar Azam", 99)  # Create an Instance of Student class
student_01.display()  # Call Display Method
