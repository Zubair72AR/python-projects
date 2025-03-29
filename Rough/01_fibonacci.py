MAX_fibonacci: int = 10000  # mAX Limit


def Fibonacci():
    current_fibonacci = 0  # The 0th Fibonacci Number
    next_fibonacci = 1  # The 1st Fibonacci Number
    while current_fibonacci <= MAX_fibonacci:
        # Print Current FIBONACCI
        print(current_fibonacci)
        # Total of Both FIBONACCI
        both_fibonacci = current_fibonacci + next_fibonacci
        # Make Current = Next FIBONACCI
        current_fibonacci = next_fibonacci
        # Next = Both FIBONACCI
        next_fibonacci = both_fibonacci


if __name__ == "__main__":
    Fibonacci()
