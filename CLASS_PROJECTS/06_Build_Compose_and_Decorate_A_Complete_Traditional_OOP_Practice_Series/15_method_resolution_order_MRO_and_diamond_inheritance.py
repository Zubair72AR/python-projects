"""
15. Method Resolution Order (MRO) and Diamond Inheritance
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.
"""


class A:  # Class A
    def show(self):
        print("Class A: Show Method")


class B(A):  # Class B inheriting A
    def show(self):
        print("Class B: Show Method")


class C(A):  # Class C inheriting A
    def show(self):
        print("Class C: Show Method")


class D(B, C):  # Class D inheriting both B and C
    pass  # No need to override show(), will use MRO


# Creating Object of D
d = D()

# Calling show() to observe MRO
d.show()
