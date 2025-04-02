def temperature():
    # User input and Convert Data type to Float
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    # Calculation Fahrenheit to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    # Printing Result in Celsius
    print(
        f"Temperature {degrees_fahrenheit}°F is equal to {degrees_celsius:.2f}°C")


if __name__ == '__main__':
    temperature()
