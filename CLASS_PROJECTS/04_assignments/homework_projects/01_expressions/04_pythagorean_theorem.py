import math  # Import the math library so we can use the sqrt function


def pythagorean():
    # Get the two side lengths from the user and cast them to be numbers
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the two sides
    bc: float = math.sqrt(ab**2 + ac**2)

    # Print the result using f-string
    print(f"The length of BC (the hypotenuse) is: {bc}")


if __name__ == '__main__':
    pythagorean()
