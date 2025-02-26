import random


def play_game():
    options = ["rock", "paper", "scissors"]
    attempts = 0

    while True:
        user_choice = input(
            "Choose rock, paper, or scissors: ").strip().lower()
        if user_choice not in options:
            print("Invalid choice. Please select rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        attempts += 1

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print(f"Thanks for playing! Total rounds played: {attempts}")
            break


play_game()
