# adjective noun verb
SENTENCE_START: str = "Panaversity is fun! I learned to program and used Python to create my "


def main():
    # Taking inputs from the user to complete the sentence
    adjective: str = input("Please enter an adjective: ")
    noun: str = input("Please enter a noun: ")
    verb: str = input("Please enter a verb: ")

    # Constructing and displaying the final sentence
    full_sentence: str = f"{SENTENCE_START}{adjective} {noun} {verb}!"
    print(full_sentence)


if __name__ == '__main__':
    main()
