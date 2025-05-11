"""
12. Static Methods
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
"""


class TemperatureConverter:  # Class
    @staticmethod
    def celsius_to_fahrenheit(c):  # Static Method
        return (c * 9/5) + 32  # Convert Celsius to Fahrenheit


# Example usage
celsius = 25  # Celsius Value
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(
    celsius)  # Call Static Method

print(f"{celsius}°C is equal to {fahrenheit}°F")  # Print Converted Value
