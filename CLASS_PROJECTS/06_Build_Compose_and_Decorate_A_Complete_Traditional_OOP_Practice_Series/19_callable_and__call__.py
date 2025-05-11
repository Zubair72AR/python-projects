"""
19. callable() and __call__()
Assignment:
Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.
"""


class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the multiplication factor

    def __call__(self, number):
        return number * self.factor  # Multiply input number by the factor


# Create an instance of Multiplier with a factor of 3
m = Multiplier(3)

# Check if the object is callable
print(callable(m))  # Should return True

# Call the object like a function
print(m(5))  # Should return 15 (5 * 3)
