def get_first_element(element_list):
    """
    Prints the first element of a provided list.
    """
    print("📑 Complete List is : ", element_list)  # Full List Print
    print("1️⃣ First Elements of List is : ",
          element_list[0])  # First Element


def get_user_data():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    element_list = []  # EMpty List
    # Get User Input
    user_element: str = input(
        "Please enter an element of the list or press enter to stop. ")
    # If User Need more Input or Press just enter to break loop
    while user_element != "":
        # Keep Appending User Inputs in the List
        element_list.append(user_element)
        user_element = input(
            "Please enter an element of the list or press enter to stop. ")
    return element_list


def main():
    element_list = get_user_data()
    get_first_element(element_list)


if __name__ == "__main__":
    main()
