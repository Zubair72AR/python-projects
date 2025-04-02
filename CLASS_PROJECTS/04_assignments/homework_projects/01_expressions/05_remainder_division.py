def divide_remainder():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Integer division (quotient) and remainder calculation
    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    # Display the result using f-string
    print(
        f"The result of this division is {quotient} with a remainder of {remainder}")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    divide_remainder()
