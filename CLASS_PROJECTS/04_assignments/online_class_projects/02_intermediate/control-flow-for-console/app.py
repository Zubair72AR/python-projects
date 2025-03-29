import random

ROUNDS = 5  # Total Round
# Round Text Print with Emoji Number
round_emoji = {1: "⚬ Round 1️⃣", 2: "⚬ Round 2️⃣",
               3: "⚬ Round 3️⃣", 4: "⚬ Round 4️⃣", 5: "⚬ Round 5️⃣", }


def lower_higher_game():
    # Welcome
    print("Welcome to the High-Low Game! 🎲")
    print("---------------------------------")

    # >>> MILESTONE 5 <<< keep track of your score
    your_score = 0

    # >>> MILESTONE 4 <<< Play multiple rounds
    for i in range(1, ROUNDS + 1):
        # >>> MILESTONE 1 <<< Generate the random numbers and print them out
        computer_number: int = random.randint(1, 100)
        your_number: int = random.randint(1, 100)

        # Show ROund NUmber & User Number to Guess
        print(f"\n{round_emoji[i]}")
        print(f"🎯 Your number is: \"{your_number}\"")

        # >>> MILESTONE 2 <<< Get user input for their choice
        print(
            "Do you think your number is higher or lower than the computer's?")
        user_input = input(
            "H / Higher, L / Lower :").lower().strip()

        # >>> MILESTONE 3 <<< Map out all the ways to win the round
        lower_correct: bool = (
            user_input == "lower" or user_input == "l") and your_number < computer_number
        higher_correct: bool = (
            user_input == "higher" or user_input == "h") and your_number > computer_number

        # Lower Corrects
        if lower_correct:
            print(f"✅ Right! Lower was correct. Computer: {computer_number}")
            # >>> MILESTONE 5 <<< keep track of your score
            your_score += 1
        # If Higher Corrects
        elif higher_correct:
            print(f"✅ Right! Higher was correct. Computer: {computer_number}")
            # >>> MILESTONE 5 <<< keep track of your score
            your_score += 1
        else:
            # If COmputer Wins
            print(f"❌ Oops! Wrong guess. Computer's number: {computer_number}")

        # >>> MILESTONE 5 <<< keep track of your score
        print(f"\n📊 Your Score: \"{your_score}\" out of {i}.")

    # WINNER Announcement
    winner = "🏅 YOU WON 👑" if your_score >= 3 else "🥇 COMPUTER WON 🔥"
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"The Winner is : {winner}")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


if __name__ == "__main__":
    lower_higher_game()
