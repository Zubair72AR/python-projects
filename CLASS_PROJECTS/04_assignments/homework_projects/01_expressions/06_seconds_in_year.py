# Constants to simplify time calculations
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60


def main():
    # Calculating total seconds in a year using predefined constants
    total_seconds: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # Displaying the result
    print(f"There are {total_seconds} seconds in a year!")


if __name__ == '__main__':
    main()
