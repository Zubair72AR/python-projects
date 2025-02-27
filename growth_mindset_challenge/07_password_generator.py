import string
import random


def select_password_type():
    # User Input to "Include numbers in the password?"
    include_numbers = input(
        "Include numbers in the password? (Yes/No) [Default: Yes]: "
    ).strip().lower()
    # User Input to "Include special characters?"
    include_special_chars = input(
        "Include special characters? (Yes/No) [Default: Yes]: "
    ).strip().lower()
    # User Input and Error Handling to "Enter password length"
    while True:
        try:
            user_input = input(
                "Enter password length (Minimum 6, Press Enter for default: 6) ").strip()
            password_length = 6 if not user_input else int(user_input)
            if password_length < 6:
                print(
                    "⚠️ Password length must be at least 6 characters. Please try again.")
            else:
                break
        except ValueError:
            print("❌ Invalid input! Please enter a number (e.g., 6, 8, 12).")
    # User Input to "Add any specific word or name?"
    include_text_name = input(
        "Add any specific word or name? Type it or press Enter to skip [Default: No]: "
    ).strip()
    # User Input and Error Handling to "How many passwords should be generated"
    while True:
        try:
            user_input = input(
                "How many passwords should be generated? (Press Enter for default: 5) ").strip()
            number_of_password_generate = 5 if not user_input else int(
                user_input)
            if number_of_password_generate <= 0:
                print("⚠️ Number of passwords must be at least 1.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a number (e.g., 6, 8, 12).")

    # Adding Numbers Special Characters if User Asked for Generating Password
    character_included = string.ascii_letters
    character_included += string.digits if include_numbers in [
        "yes", "y", ""] else ""
    character_included += string.punctuation if include_special_chars in [
        "yes", "y", ""] else ""

    # List to store passwords
    passwords = []

    # Generate passwords
    for _ in range(number_of_password_generate):
        password = include_text_name
        random_words = []
        for _ in range(password_length):
            random_chars = random.choice(character_included)
            random_words.append(random_chars)
        random_string = "".join(random_words)
        password += random_string
        passwords.append(password)

   # Function to Display Details of Generated Password
    def generate_details():
        print("\n>>> Details of Generated Password <<<\n")
        # Number Inclusion
        print("1. ✅ Including Numbers in Password" if include_numbers in [
              "yes", "y", ""] else "1. ❌ Excluding Numbers in Password")
        # Special Characters Inclusion
        print("2. ✅ Including Special Characters in Password" if include_special_chars in [
              "yes", "y", ""] else "2. ❌ Excluding Special Characters in Password")
        # Word/Name Inclusion
        print(
            f"4. 📌 Included Word/Name: '{include_text_name}'" if include_text_name else "4. ❌ No Specific Word/Name Provided")
        # Password Length
        print(f"3. 🔢 Password Length: {password_length} + Length of Provided Word/Name {len(include_text_name)} = {int(password_length) + len(include_text_name)}" if include_text_name else f"3. 🔢 Password Length: {password_length}")
        # Total Passwords Generated
        print(
            f"5. 🔢 Total Passwords Generated: {number_of_password_generate}\n")

    # Call the Function
    generate_details()

    # Showing Created Password to the User by Serial Number
    for index, password in enumerate(passwords, start=1):
        print(f"{index}. {password}")


# Call the Function
select_password_type()
