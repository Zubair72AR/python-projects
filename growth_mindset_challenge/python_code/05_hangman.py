import random

# Dictionary containing categories and their respective word lists
suggested_words_list = {
    "Color": ["black", "white", "red", "green", "yellow"],
    "Fruit": ["mango", "apple", "grapes", "banana", "strawberry"],
    "Vegetables": ["carrot", "potato", "tomato", "spinach", "onion"],
    "Country": ["india", "usa", "china", "japan", "russia"]
}

# Randomly select a category and a word
random_category, words_list = random.choice(list(suggested_words_list.items()))
random_word = random.choice(words_list)

# Vowels to be revealed in the hint
vowels = {"a", "e", "i", "o", "u"}

# Generate hint with vowels revealed and other letters as "_"
hint = [letter if letter in vowels else "_" for letter in random_word]

# Game variables
lives_remaining = 3
guessed_letters = set()

# Display initial hint
print(f"\nHint..! Category: {random_category}")
print(" ".join(hint).upper())


def main():
    global lives_remaining

    while lives_remaining > 0 and "_" in hint:
        user_input = input("\nGuess a letter (except vowels): ").lower()

        # Validate input
        if len(user_input) != 1 or not user_input.isalpha() or user_input in guessed_letters or user_input in vowels:
            print("❌ Invalid input! Enter a single new consonant.")
            continue

        guessed_letters.add(user_input)

        if user_input in random_word:
            # Reveal guessed letter in hint
            for index, letter in enumerate(random_word):
                if letter == user_input:
                    hint[index] = user_input
            print("✅ Correct!", " ".join(hint).upper())
        else:
            lives_remaining -= 1
            print(f"❌ Wrong guess! Lives remaining: {lives_remaining}")

    # Game result
    if "_" not in hint:
        print(f"\n🎉 Congratulations! You guessed the word: {random_word}")
    else:
        print(f"\n💀 Game over! The correct word was: {random_word}")


if __name__ == "__main__":
    main()
