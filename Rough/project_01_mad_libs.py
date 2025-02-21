def self_Introduction():

    # NAME Input
    name = ' '.join(input("Please enter your name: ").split()).title()

    # AGE Input
    while True:

        # Check if age is entered in the number
        try:
            age = int(input("Please enter your age: "))

            # Check if age is greater than 0
            if age > 0:
                break
            else:
                print("❌ Age must be greater than 0.")
        except ValueError:
            print("❌ Please enter valid age.")

    # GENDER Input
    while True:
        gender = input("Please enter your gender boy/girl: ").lower().strip()

        # Check if gender is either boy or girl
        if gender in ["boy", "girl"]:
            break
        else:
            print("❌ Please enter boy or girl.")

    # LOVE or LIKE Input
    loves = input("Whom/What do you Love: ").lower().strip()

    # HOBBY Input
    hobby = input("Please enter your hobby: ").lower().strip()

    # Gender setting up (his/her or he/she) based on user input GENDER
    his_her = "his" if gender == "boy" else "her"
    he_she = "He" if gender == "boy" else "She"

    # Setting up age (singular or plural) based on user input AGE
    year_label = "year" if age == 1 else "years"

    # Printing the self-introduction message with user inputs
    print(f"\"Meet {name}, {he_she} is {age} {year_label} old {gender}. Who loves {loves} and enjoys {hobby} in {his_her} free time. {he_she} is always ready for new adventures!\" 😊")


# Calling the function
self_Introduction()
