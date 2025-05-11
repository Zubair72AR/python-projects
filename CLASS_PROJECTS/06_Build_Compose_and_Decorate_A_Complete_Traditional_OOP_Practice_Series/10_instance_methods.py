"""
10. Instance Methods
Assignment:
Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.
"""


class Dog:  # Class
    def __init__(self, name: str, breed: str):  # Constructor
        self.name = name  # Save Name
        self.breed = breed  # Save Breed

    def bark(self):  # Instance Method
        print(f"{self.name} says woof!")  # Print Bark Message


dog1 = Dog("Max", "German Shepherd")  # Create Instance
dog1.bark()  # Call bark method
