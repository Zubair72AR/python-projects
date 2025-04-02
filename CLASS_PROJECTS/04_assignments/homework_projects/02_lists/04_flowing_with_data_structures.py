def updated_values(my_list, my_int, my_str, value_list, value_int, value_str):
    for i in range(3):
        my_list.append(value_list)
        my_int = my_int + value_int
        my_str = my_str + value_str
    print("\n🚀 Inside: 📑", my_list, "🔢", my_int, "🔠", my_str)


def main():
    # Getting Data to Add in The "LIST, INTEGER, STRING"
    value_list = input("Message to copy 3x into list: ")
    value_int = int(input("Number to add 3x to int: "))
    value_str = input("Word to repeat 3x in string: ")
    # Define "LIST, INTEGER, STRING" for comparing together to understand it better
    my_list = []  # List
    my_int = 0  # Integer
    my_str = "start"  # String
    print("\n🔴 Before: 📑", my_list, "🔢", my_int, "🔠", my_str)
    updated_values(my_list, my_int, my_str, value_list, value_int, value_str)
    print("\n🟢 After: 📑", my_list, "🔢", my_int, "🔠", my_str)


if __name__ == "__main__":
    main()
