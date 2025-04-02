def double_list():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list of integers
    # Print Result Before
    print("List before Multiplication", my_list)
    for i in range(len(my_list)):  # For Loop with the Length if the List
        my_list[i] = my_list[i] * 2  # Multiply 2 by Tracing Index number
    # Print Result After
    print("List After Multiplication", my_list)


if __name__ == '__main__':
    double_list()
