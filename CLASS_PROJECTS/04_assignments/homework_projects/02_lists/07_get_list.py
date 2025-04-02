def make_user_list():
    user_list = []  # Blank List
    num = 1  # Track User Input (for fun/Learning Something New)
    ordinal_suffix = "st"
    # Get First Element of List
    list_items = input(f"Please Enter {num}{ordinal_suffix} Element of List: ")

    while list_items != "":  # While Loop Till Get "" Blank Value
        user_list.append(list_items)  # Keep Appending User Data
        num += 1  # Plus Number
        if num % 100 in [11, 12, 13]:  # Avoid "ST" with 11, 12, 13 or 111, 112 , 113 and so on
            ordinal_suffix = "th"
        elif num % 10 == 1:
            ordinal_suffix = "st"  # Add "ST"
        elif num % 10 == 2:
            ordinal_suffix = "nd"  # Add "ND"
        elif num % 10 == 3:
            ordinal_suffix = "rd"  # Add "RD"
        else:
            ordinal_suffix = "th"  # Add "TH"

        list_items = input(
            f"Please Enter {num}{ordinal_suffix} Element of List: ")

    # Total Number of Elements in the List
    print(f"\n✅ You Entered {num - 1} Elements in the List")
    print("📑 Here's the list:", user_list)  # Result of List


if __name__ == "__main__":
    make_user_list()
