MAX_LENGTH = 3


def make_user_list():
    user_list = []  # List
    # Get First Element of List
    list_items = input(f"Please enter element of List: ")

    while list_items != "":  # While Loop Till Get "" Blank Value
        user_list.append(list_items)  # Keep Appending User Data
        list_items = input(
            f"Please enter element of List: ")  # Keep Asking User Data untill "" gets Blank

    print("📑 Here's the list with Initial Length: ", user_list)  # Result of List
    return user_list


def get_shorter_list(user_list):
    # if List Length Less then 4
    if len(user_list) <= 3:
        print("⛔ No Element is Remove.")
    # While Loop till Max Length
    while len(user_list) > MAX_LENGTH:
        last_elements = user_list.pop()  # Keep POP last element of List
        # Keep Printing Last Removed One
        print("🔚Removed Last Element: ", last_elements)
    print(f"Final List has {len(user_list)} Element: ", user_list)


def main():
    user_list = make_user_list()
    get_shorter_list(user_list)


if __name__ == "__main__":
    main()
