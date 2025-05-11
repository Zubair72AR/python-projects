"""
7. Access Modifiers: Public, Private, and Protected
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.
"""


class Employee:  # Class
    def __init__(self, name, salary, ssn):  # Constructor
        self.name = name          # Public Variable
        self._salary = salary     # Protected Variable
        self.__ssn = ssn          # Private Variable


e = Employee("Ali", 50000, "123-45-6789")  # Create an Instance

# Access Public
print(f"Public Name: {e.name}")  # ✅ Accessible

# Access Protected
# ⚠️ Accessible but should be treated as protected
print(f"Protected Salary: {e._salary}")

# Access Private using try block
try:
    print(f"Private SSN: {e.__ssn}")  # ❌ Error
except AttributeError as error:
    print(f"Private SSN: Access Denied ➜ {error}")
