def perimeter_triangle():
    # User input of all sides of the triangle
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    # Print the Sum of all sides using string concatenating!
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))


if __name__ == '__main__':
    perimeter_triangle()
