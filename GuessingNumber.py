import random


def play_game():
    number_to_guess = random.randrange(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 99: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if user_guess < number_to_guess:
            print(f"Attempt No. {attempts}, Too low! Try again.")
        elif user_guess > number_to_guess:
            print(f"Attempt No. {attempts}, Too high! Try again.")
        else:
            print(
                f"Congratulations! You guessed the correct number in the {attempts} attempt.")
            break


while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thanks for playing! Goodbye.")
        break
