"""
3. Public Variables and Methods
Assignment:
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.
"""


class Car:  # Class
    def __init__(self, brand: str):  # Constructor
        self.brand = brand  # Public Variable

    def start(self):  # Public Method
        print(f"{self.brand} is starting...")


# Create an Instance
car1 = Car("Toyota")

# Accessing public variable and method from outside the class
print(f"Car Brand: \"{car1.brand}\"")
car1.start()
