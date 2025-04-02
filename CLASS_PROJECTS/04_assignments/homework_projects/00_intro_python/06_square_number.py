def square_value():
    user_value: float = float(input("Type a number to see its square: "))
    calculated_square = user_value ** 2
    print(f"The square of {user_value} is: {calculated_square}")


if __name__ == '__main__':
    square_value()
