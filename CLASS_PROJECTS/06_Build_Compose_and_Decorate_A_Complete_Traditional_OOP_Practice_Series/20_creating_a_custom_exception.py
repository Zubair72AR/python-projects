"""
20. Creating a Custom Exception
Assignment:
Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
"""


class InvalidAgeError(Exception):  # Custom Exception
    pass


def check_age(age):
    try:
        if age < 18:
            # Raise custom exception
            raise InvalidAgeError("Age must be 18 or older")
        else:
            print("Age is valid")  # Valid age
    except InvalidAgeError as e:
        print(f"Error: {e}")  # Handle exception


# Test the function
check_age(16)  # This will raise the InvalidAgeError
check_age(20)  # This will print "Age is valid"
