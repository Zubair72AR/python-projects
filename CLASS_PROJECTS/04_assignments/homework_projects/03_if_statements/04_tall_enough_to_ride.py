MINIMUM_HEIGHT: int = 75


def main():
    while True:
        try:
            # Ask Height and AGain Ask After 1 loop
            height = input("📌 Enter your height. (or ⛔ press Enter to exit): ")
            # If Blank Exit
            if not height:
                print("👋 Goodbye!")
                break
            # COnvert into Float
            height = float(height)
            # if Height is Positive Numbers
            if height > 0:

                if height >= MINIMUM_HEIGHT:
                    # if Value Matches Allow User
                    print("✅ You're tall enough to ride!")
                else:
                    # if Value Does not matches not Allow
                    print("❌ You're not tall enough to ride, 🍀 but maybe next year!")
            else:
                # If value is not Positive
                print("Height must be greater than 0.")
        except ValueError:
            # if user put any Text or Other then NUmbers
            print("🚨 Invalid input! Please enter a valid number, e.g., 75, 100.")


if __name__ == '__main__':
    main()
