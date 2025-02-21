import random

while True:
    choice = input("Roll the Dice y/n: ").lower()
    if choice == 'y':
        num1 = random.randint(1, 99)
        print(num1)
    elif choice == 'n':
        print("Thanks for Playing")
        break
    else:
        print("Invalid choice. Please Press y/n.")
        