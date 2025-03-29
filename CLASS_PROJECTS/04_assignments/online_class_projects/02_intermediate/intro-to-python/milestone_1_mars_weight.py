MARS_MULTIPLE = 0.378


def mars_on_weight():
    while True:
        try:
            # get Value in FLOAT
            earth_weight = float(input("⚖️ Enter a Weight on Earth 🌎"))
            # Break Loop
            break
        except ValueError:
            # Show Error If User Entered Wrong Value
            print("❌ Invalid input. Enter value in KG e.g. 1.25, 0.25, 5")

    # Calculation Earth Weight by Multiply Mars Weight
    mars_weight = earth_weight * MARS_MULTIPLE
    # Round of Digits
    rounded_mars_weight = round(mars_weight, 2)

    # Print Result
    print(f"⏲️ The equivalent weight on Mars: {rounded_mars_weight}")


if __name__ == "__main__":
    mars_on_weight()
