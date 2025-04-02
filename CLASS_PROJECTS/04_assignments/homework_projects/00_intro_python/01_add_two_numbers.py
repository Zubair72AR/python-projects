# Make Function of Sum
def sum():
    # Get value 01
    value1: str = input("Enter First Number -> ")
    # Convert value 01 to integer type
    value1: int = int(value1)
    # Get value 02
    value2: str = input("Enter Second Number -> ")
    # Convert value 02 to integer type
    value2: int = int(value2)
    # Calculate the sum of value 01 and value 02
    total: int = value1 + value2
    # Print the result
    print(f"The Total of {value1} + {value2} = {total}")


# Runs the function only if this script is executed directly, not when imported.
if __name__ == "__main__":
    # Call the function to start the program
    sum()
