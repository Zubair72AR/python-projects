"""
9. Abstract Classes and Methods
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().
"""

from abc import ABC, abstractmethod  # Import Abstract Base Classes


class Shape(ABC):  # Abstract Class
    @abstractmethod
    def area(self):  # Abstract Method
        pass  # Must be implemented in subclasses


class Rectangle(Shape):  # Derived Class
    def __init__(self, width: int, height: int):  # Constructor
        self.width = width  # Save Width
        self.height = height  # Save Height

    def area(self):  # Implement Abstract Method
        return self.width * self.height  # Calculate Area


r1 = Rectangle(5, 10)  # Create Instance
print(f"Area of Rectangle: {r1.area()}")  # Call area method
