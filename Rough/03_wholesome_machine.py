import random
# List of Affirmation
AFFIRMATION_LIST: list = [
    "I am strong and unstoppable.",
    "Success is within my reach.",
    "I believe in my potential.",
    "Every day, I grow stronger.",
    "I attract positivity and success.",
    "My dreams are becoming reality.",
    "I am confident and fearless.",
    "I create my own happiness.",
    "Challenges make me even stronger.",
    "I am capable of amazing things."
]

# Choice One of Them
AFFIRMATION = random.choice(AFFIRMATION_LIST)


def affirmation_def():
    # Print Randomly_Chosen Affirmation
    print(f"\n👉 ❝ {AFFIRMATION} ❞")
    # Ask Input
    user_input = input("🎯 Type this affirmation exactly: ")
    # Keep Asking till User Type Correct Affirmation
    while AFFIRMATION != user_input:
        # If user Typed Correct but not Follow Letter Casing
        if AFFIRMATION.lower() == user_input.lower():
            print("\n👏 You're very close! Pay attention to letter casing.")
        # If User Typed Wrong
        else:
            print("\n❌ Nope! That’s not correct.")
        # Print Randomly_Chosen Affirmation
        print(f"\n👉 ❝ {AFFIRMATION} ❞")
        # Ask Input Again
        user_input = input("🎯 Type this affirmation exactly: ")
    # Show Success Message when User Typed Correct Value following Case Sensitivity
    print("\n✅ Hmm... You got it right!")


if __name__ == "__main__":
    affirmation_def()
