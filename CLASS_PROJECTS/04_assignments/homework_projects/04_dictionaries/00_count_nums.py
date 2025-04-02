def count_number_qty():
    num_list = []  # empty LIST
    while True:
        # get user Input
        user_input = input("🔢 Please enter a number: ")
        # If find Blank
        if not user_input:
            break
        # If find positive Numbers
        if user_input.isdigit():
            num = int(user_input)  # change into INTEGER
            num_list.append(num)  # Append in the LIST
        else:
            # if find string or negative value
            print("❌ Invalid input! Please enter a valid number (e.g., 0, 9, 15).")

    # Count Numbers Quantity
    num_dict = {}  # empty DICT
    for val in num_list:  # for Loop to check
        if val not in num_dict:  # if not find in DICT
            num_dict[val] = 1  # add 1
        else:  # if already in DICT
            num_dict[val] += 1  # plus 1

    # display Result
    for key, val in num_dict.items():
        qty = "time" if val <= 1 else "times"
        print(f"Number {key} appears {val} {qty}.")


if __name__ == '__main__':
    count_number_qty()
