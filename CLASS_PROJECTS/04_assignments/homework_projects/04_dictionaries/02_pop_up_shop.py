def fruits_market():
    # Fruits Dictionary
    fruits = {
        "Apple": {"price": 320, "unit": "kg", "emoji": "🍏"},
        "Orange": {"price": 180, "unit": "dozen", "emoji": "🍊"},
        "Banana": {"price": 140, "unit": "dozen", "emoji": "🍌"},
        "Mango": {"price": 210, "unit": "kg", "emoji": "🥭"},
        "Grapes": {"price": 360, "unit": "kg", "emoji": "🍇"},
        "Pineapple": {"price": 90, "unit": "piece", "emoji": "🍍"},
        "Strawberry": {"price": 400, "unit": "kg", "emoji": "🍓"},
        "Cherry": {"price": 600, "unit": "kg", "emoji": "🍒"},
        "Watermelon": {"price": 40, "unit": "kg", "emoji": "🍉"},
        "Kiwi": {"price": 15, "unit": "piece", "emoji": "🥝"}
    }
    # Total
    total_cost = 0
    # Track PURCHASED FRUITS
    purchased = {}
    # Track Not PURCHASED FRUITS
    not_purchased = {}
    # WELCOME Message
    print("📢 WELCOME TO FRUITS MARKET 😃")
    # For Loop to Ask Order QTY
    for fruit, val in fruits.items():
        # While Loop Keep Asking if Finds an Error
        while True:
            try:
                # Fruits Name and Price for User
                print(
                    f'\n⋆ \"{val["emoji"]} {fruit}\" cost is Rs.{val["price"]} per {val["unit"]}.')
                # Ask for QTY to Order
                qty_input = input(
                    f'🛒 How many {val["unit"]} would you like to buy? (e.g., ✔️ 1, 2, 5, or ❌ 0): ').strip()
                # If no QTY Break and Exit
                if not qty_input:
                    # Add Not Purchased Fruits Data
                    not_purchased[fruit] = val
                    break
                # Make FLOAT to QTY Input
                qty = float(qty_input)
                # If QTY Greater Then Zero
                if qty > 0:
                    # Add Purchased Fruits Data
                    purchased[fruit] = {
                        "price": val["price"], "unit": val["unit"], "emoji": val["emoji"], "qty": qty}
                    # Add QTY * Price to TOTAL COST
                    total_cost += val["price"] * qty
                else:
                    # Add Not Purchased Fruits Data
                    not_purchased[fruit] = val
                # Break if Find FLOAT Input
                break
            except ValueError:
                # if User put STRING Show Error and ask Again
                print(
                    "❌ Invalid input! Please enter a valid number (e.g., ✔️ 1, 2, 5, or ❌ 0).")
    # Total Cost
    print(f"\n💰 Your total shopping cost is Rs {total_cost:.2f}")

    # List of Purchased Items
    print(f"\n✅ List of Purchased Items.")
    for index, (fruit, val) in enumerate(purchased.items(), start=1):
        total = val["price"] * val["qty"]
        print(
            f'{index}. \"{val["emoji"]} {fruit}\", Rs {val["price"]}/{val["unit"]}, ordered Qty:{val["qty"]} = Total {total:.2f}')

    # List of Not Ordered Items
    print(f"\n❌ Skipped Items (Not Purchased)")
    for index, (fruit, val) in enumerate(not_purchased.items(), start=1):
        print(
            f'{index}. \"{val["emoji"]} {fruit}\", Rs {val["price"]}/{val["unit"]}.')

    # Thanks Message
    print("\nThank You 😊❣️\n")


if __name__ == "__main__":
    fruits_market()
