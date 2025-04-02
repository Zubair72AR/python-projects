import random


def number_guessing():
    min_num = 1  # MIN Number to Track
    max_num = 50  # MAX Number
    attempt = 1  # ATTEMPTS to Track Number of Tries
    # WELCOME Message
    print("Welcome to the Number Guessing Game! 🎯")
    print(f"👁️ Try to guess my secret number between {min_num} to {max_num}.")
    # Generate RANDOM SECRETE Number
    secret_num = random.randint(min_num, max_num)
    # While Loop for Correct Input
    while True:
        try:
            # Get User Input with (MIN to MAX number details)
            guess = int(
                input(f"\nEnter your guess ({min_num} ↔️ {max_num}): "))
            # If Correct Input Break Loop
            break
        except ValueError:
            print(
                f"🔴 Invalid Input! Please enter a number between ({min_num} ↔️ {max_num}). Try again!")

    # If User Guess in the First Try Print Message and Exit from Function
    if secret_num == guess:
        # Print Success Message
        print(
            f"\n🏅 Incredible! You nailed \"{secret_num}\" in just one attempt!")
        # Exit if Guessed in very first try
        return
    # if not Guess Keep Asking Again
    while secret_num != guess:
        # if Secret Number is Lower Then Guessed Number
        if secret_num < guess:
            # Print High Message
            print(f"🔼 Oops! Too 🔥 high. Try a lower number!")
            # Change MAX Number Value
            max_num = guess
        else:
            # Print Lower Message
            print(f"🔽 Oops! Too ❄️ low. Try a higher number!")
            # Change MIN Number Value
            min_num = guess
        # While Loop for Correct Input
        while True:
            try:
                # Get User Input again with (MIN to MAX number details)
                guess = int(
                    input(f"\nEnter your guess ({min_num} ↔️ {max_num}): "))
                # If Correct Input Break Loop
                break
            except ValueError:
                print(
                    f"🔴 Invalid Input! Please enter a number between ({min_num} ↔️ {max_num}). Try again!")
        # Increase Attempt by 1
        attempt += 1
    # if Guess Number Print the Success Message also Number of Attempts
    print(
        f"\n🏅 Bravo! You cracked the number \"{secret_num}\" in {attempt} attempts!")


if __name__ == "__main__":
    number_guessing()
