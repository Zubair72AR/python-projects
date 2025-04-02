# Defining the conversion factor (Global constant)
INCHES_IN_FOOT: int = 12


def convert_feet_to_inch():
    # Getting user input
    user_feet_input: float = float(input("Enter number of feet: "))

    # Calculating inches from feet
    inches = user_feet_input * INCHES_IN_FOOT  # Using the global constant

    # Checking if it's "foot" or "feet" based on the input value
    foot_feet = "foot is equal to" if user_feet_input == 1 else "feet are equal to"

    # Displaying the result in feet and inches format
    print(f"{user_feet_input} {foot_feet} {inches} inches")


# Ensuring the function runs only when this file is executed directly
if __name__ == '__main__':
    convert_feet_to_inch()
