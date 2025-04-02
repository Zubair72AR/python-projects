def main():
    year = int(input("📅 Please enter year, e.g. 2025: "))
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True  # if divided by 4, 100 and 400
            else:
                leap = False  # if Divided by 4 and 100 and not by 400
        else:
            leap = True  # if Divided by 4 and not by 100
    else:
        leap = False  # if not Divided by 4

    # Print Message
    if leap:
        print(f"✅ Leap Year ➜ {year}.")
    else:
        print(f"❌ Not a Leap Year ➜ {year}.")


if __name__ == '__main__':
    main()


# # Short
# def leap_year():
#     year = int(input("📅 Please enter year, e.g. 2025: "))

#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"✅ Leap Year ➜ {year}.")
#     else:
#         print(f"❌ Not a Leap Year ➜ {year}.")


# if __name__ == '__main__':
#     leap_year()
