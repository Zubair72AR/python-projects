import random


def computer_guess():
    low = 1
    high = 10
    # Number of Attempts
    attempts = 0

    print("Think of a number between 1 and 10, and the computer will try to guess it.")

    while True:
        # Computer's guess
        guess = random.randint(low, high)
        attempts += 1
        print(f"Computer's guess: {guess}")

        # User feedback
        feedback = input(
            "Please Enter \"H\" if too high, \"L\" if too low, or \"C\" if correct: ").strip().lower()

        if feedback == "l":
            low = guess + 1
        elif feedback == "h":
            high = guess - 1
        elif feedback == "c":
            print(f"The computer guessed your number in {attempts} attempts!")
            break
        else:
            print("Please enter only 'high', 'low', or 'correct'.")


# Option to play again
def play():
    while True:
        computer_guess()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    play()
