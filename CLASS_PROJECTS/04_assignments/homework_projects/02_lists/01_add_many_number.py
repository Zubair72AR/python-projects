def total_numbers(list_of_numbers) -> int:
    # Total variable
    total = 0
    # for Loop calculating
    for num in list_of_numbers:
        total += num
    # returning total sum
    return total


def main_func():
    test_list: list[int] = [1, 3, 5, 7, 9]  # list
    sum_list: int = total_numbers(test_list)  # using Total_number func for sum
    print("Sum of the numbers in the list: ", sum_list)  # print the result


if __name__ == '__main__':
    main_func()
