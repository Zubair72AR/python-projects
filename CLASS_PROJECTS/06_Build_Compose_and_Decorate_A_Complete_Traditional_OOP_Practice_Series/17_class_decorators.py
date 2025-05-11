"""
17. Class Decorators
Assignment:
Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.
"""


def add_greeting(cls):  # Class decorator
    class NewClass(cls):  # Inherit the original class and add the greet method
        def greet(self):
            return "Hello from Decorator!"
    return NewClass


@add_greeting  # Applying class decorator
class Person:
    pass


# Creating an instance of the decorated class
person = Person()

# Calling the new greet method
print(person.greet())
