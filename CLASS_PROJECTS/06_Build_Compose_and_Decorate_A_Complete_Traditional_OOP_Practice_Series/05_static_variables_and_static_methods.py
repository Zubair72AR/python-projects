"""
5. Static Variables and Static Methods
Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.
"""


class MathUtils:  # Class

    @staticmethod
    def add(a: int, b: int) -> int:  # Static Method
        return a + b  # Return Sum


# Using Static Method without creating an object
result = MathUtils.add(10, 25)
print(f"Sum: {result}")
