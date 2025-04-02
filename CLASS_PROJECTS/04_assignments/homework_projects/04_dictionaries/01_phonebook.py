import re


def save_phone_book():
    # Phone Book Dictionary
    phone_book = {
        "Zubair": "+92 342-3873626",
        "John": "+1 (408) 555-7890",
        "Ali": "0300-1234567",
        "Sara": "+971-50-2345678",
        "Office": "021-3456789",
        "Emergency": "911",
    }
    print("💖 Welcome to Your Phone Book! 📖")
    while True:
        # Get Input Name
        name = input("\n👤 Please enter the name: ").strip()
        # If No Name Exit from While Loop
        if not name:
            break
        # If Name is Duplicate Show Error and Ask Name Again
        if any(name.lower() == key.lower() for key in phone_book.keys()):
            print("❌ Name already exits enter something else")
            continue
        # While Loop for Phone Number if Name is Accepted
        while True:
            # Get Input Phone Number and Show Allowed Characters
            print("\n📢 Allowed characters for phone number: ✅ 𝟎-𝟗 ❪ ❫ ✚ ━ • & space.")
            phone_number = input("☎️ Please enter the phone number:").strip()
            # If No Phone Number Ask Phone Number Again
            if not phone_number:
                print(
                    "⛔ Phone number cannot be blank! Please enter a valid number.")
                continue
            # Check if Phone Number is Duplicate
            duplicate_number = None
            for key, val in phone_book.items():
                if val == phone_number:
                    duplicate_number = key
            # If Phone Number is Duplicate Show Error
            if duplicate_number:
                print(
                    f"⚠️ Number \"{phone_book[duplicate_number]}\" is already saved as \"{duplicate_number}\".")
                continue
            # Check Allowed Characters for Phone Number
            if re.fullmatch(r"[+]?\d+[0-9()\- .]*", phone_number):
                # Save Phone Number in Dictionary, If Phone Number is Okay with Given COndition
                phone_book[name] = phone_number
                # Exit From Loop of Phone Number
                break
            else:
                # Show Error If Find Name Wrong and Ask Name Again
                print(
                    "❌ Invalid input! Please enter a valid phone number.")
                continue
    # Return Phone Book
    return phone_book


def show_phone_book(phone_book):
    # Show All Phone Book Data
    if phone_book:
        print("\n📖 Phone Book - All Contacts:")
        for index, (name, num) in enumerate(phone_book.items(), start=1):
            print(f"{index}. 👨‍💼 {name}, ☎️ {num}")
    else:
        # if Phone Book is Empty
        print("⚠️ The phone book is empty! Please add contacts first.")


def search_phone_book(phone_book):
    # Get Search Input Text
    search_input = input(
        "\nEnter 👨‍💼 name or ☎️ phone number to search: ").lower().strip()
    show_number = {}
    # Match Search Data
    if search_input:
        for name, num in phone_book.items():
            # IF Matches Add to Show Dictionary
            if search_input in name.lower() or search_input in num:
                show_number[name] = num
    # If Show Book has Data
    if show_number:
        print("\n🔎 Search Results:")
        for index, (name, num) in enumerate(show_number.items(), start=1):
            print(f"{index}. 👨‍💼 {name}, ☎️ {num}")
    else:
        # Show Error If No Data Matches
        print("❌ No matching contact found! Please try again.")


def main():
    phone_book = save_phone_book()
    show_phone_book(phone_book)
    search_phone_book(phone_book)


if __name__ == "__main__":
    main()
