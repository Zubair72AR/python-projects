import random


def play_game():
    # Range of Selection
    number_to_guess = random.randrange(1, 10)
    # Number of Attempts
    attempts = 0

    while True:
        # Take user input for guess
        try:
            user_guess = int(input("Guess a number between 1 and 10: "))
        # If user put invalid input Show error message
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        # Increase attempts count
        attempts += 1

        # If user put Too Low Value
        if user_guess < number_to_guess:
            print(f"Attempt No. {attempts}, Too low! Try again.")
        # If user put Too High Value
        elif user_guess > number_to_guess:
            print(f"Attempt No. {attempts}, Too high! Try again.")
        # If user put Correct Value
        else:
            print(
                f"Congratulations! You guessed the correct number in the {attempts} attempt.")
            break


# If user Wants to play again
while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thanks for playing! Goodbye.")
        break
