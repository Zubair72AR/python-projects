"""
21. Make a Custom Class Iterable
Assignment:
Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.
"""


class Countdown:
    def __init__(self, start):  # Initialize with start value
        self.current = start  # Set the current countdown value

    def __iter__(self):  # Implement __iter__ to make object iterable
        return self

    def __next__(self):  # Implement __next__ for countdown logic
        if self.current < 0:  # Stop when the count reaches below 0
            raise StopIteration
        val = self.current  # Return current value
        self.current -= 1  # Decrease the value for next iteration
        return val


# Using Countdown class in a for loop
for num in Countdown(5):
    print(num)
