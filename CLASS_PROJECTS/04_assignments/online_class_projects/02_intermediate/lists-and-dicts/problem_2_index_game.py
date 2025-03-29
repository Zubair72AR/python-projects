from itertools import islice

# Problem #2: Index Game


def access_element(current_list, current_dict, index):
    try:
        # Store Dictionary Keys in List
        dict_key_list = list(current_dict.keys())
        # Access Dictionary by List Indexing and Return, also Return List by indexing
        return current_list[index], current_dict[dict_key_list[index]]
    except IndexError:
        return "Index out of range."


def modify_element(current_list, current_dict, index, new_value):
    try:
        # Update New Value to List by INdexing
        current_list[index] = new_value
        # Store Dictionary Keys in List
        dict_key_list = list(current_dict.keys())
        # Update Dictionary by List Indexing
        current_dict[dict_key_list[index]] = new_value
        # Return
        return current_list, current_dict
    except IndexError:
        return "Index out of range."


def slice_list(current_list, current_dict, start, end):
    try:
        # Slice Dictionary by ISLICE Itertools
        sliced_dict = dict(islice(current_dict.items(), start, end))
        # Slice list and return with sliced Dictionary
        return current_list[start:end], sliced_dict
    except IndexError:
        return "Invalid indices."


def index_game():
    # List and Dictionary
    current_list = [25, "Orange", 88, "Grapes", 13, "Laptop", 56]
    current_dict = {
        "fruit": "🍍 Pineapple",
        "color": "🟥 Red",
        "animal": "🐘 Elephant",
        "country": "🍁 Canada",
        "car": "🚗 Ferrari",
        "bird": "🦜 Parrot",
        "city": "🏙️ Dubai"
    }

    # Print List and Dictionary
    print(f"Current List: {current_list}")
    print(f"Current Dict: {current_dict}")
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").strip().lower()

    if operation == "access":
        # Get User Input
        index = int(input("Enter index to access: "))
        print(access_element(current_list, current_dict, index))
    elif operation == "modify":
        # Get User Input
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ").strip()
        print(modify_element(current_list, current_dict, index, new_value))
    elif operation == "slice":
        # Get User Input
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(current_list, current_dict, start, end))
    else:
        print("Invalid operation.")


if __name__ == "__main__":
    index_game()
