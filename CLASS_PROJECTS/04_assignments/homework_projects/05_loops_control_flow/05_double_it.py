def double_value():
    while True:
        try:
            # Get Correct Input Value
            current_value = int(
                input("🔢 Type a number between (1 ↔️ 9): "))
            # if Value is Positive Break the Loop
            if 0 < current_value < 10:
                break
            else:
                # If User Entered 0 or Negative Value
                print("⛔ Oops! Please enter a positive number between (1 ↔️ 9).")
        except ValueError:
            # If User Entered Other then Numbers
            print("❌ Invalid input! Please enter a numeric value.")
    # CURRENT VALUE is less then 100
    while current_value < 100:
        print(f"({current_value} x 2)", end=" = ")
        # CURRENT VALUE Keep multiplying by 2
        current_value *= 2
        # Print Updated Value
        print(current_value)


if __name__ == "__main__":
    double_value()
