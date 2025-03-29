fruit_list = ["apple 🍏", "banana 🍌", "orange 🍊", "grape 🍇", "pineapple 🍍"]


def list_practice():
    # Current List
    print(f"Current List: {fruit_list}")

    # Print the length of the list.
    print(f"Length of List: {len(fruit_list)}")

    # Add 'mango' at the end of the list.
    fruit_list.append("mango 🥭")

    # Print the updated list.
    print(f"Updated List: {fruit_list}")


if __name__ == "__main__":
    list_practice()
