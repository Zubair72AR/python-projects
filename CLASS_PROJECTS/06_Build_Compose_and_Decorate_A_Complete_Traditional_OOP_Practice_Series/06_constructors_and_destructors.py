"""
6. Constructors and Destructors
Assignment:
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).
"""


class Logger:  # Class

    def __init__(self):  # Constructor
        print("Logger started...")  # Message when object is created

    def __del__(self):  # Destructor
        print("Logger stopped...")  # Message when object is destroyed


# Create an Instance
log = Logger()

# Deleting the object
del log
