"""
13. Composition
Assignment:
Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.
"""


class Engine:  # Class
    def start(self):  # Instance Method
        print("Engine started")  # Start the Engine


class Car:  # Class
    def __init__(self, engine):  # Constructor with Engine object
        self.engine = engine  # Assign the Engine object

    def start_engine(self):  # Instance Method
        self.engine.start()  # Call Engine's start method


# Example Usage
engine = Engine()  # Create Engine Object
car = Car(engine)  # Pass Engine Object to Car
car.start_engine()  # Start the Engine via Car
