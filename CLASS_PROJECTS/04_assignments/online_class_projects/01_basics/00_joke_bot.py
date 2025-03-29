PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you!\n🎀 Sophia is heading out to the grocery store.\n🧔🏻 A programmer tells her: get a liter of milk, and if they have eggs, get 12.\n🎀 Sophia returns with 13 liters of milk.\n🧔🏻 The programmer asks why.\n🎀 Sophia replies: 'because they had eggs 🤣'\n"
SORRY: str = "\n🤡 Sorry I only tell jokes."


def main():
    # User Input
    user_input = input(PROMPT)
    if "joke" in user_input:
        # If User Enter "JOKE"
        print(JOKE)
    else:
        # If User Enter anything else "JOKE"
        print(SORRY)


if __name__ == "__main__":
    main()
