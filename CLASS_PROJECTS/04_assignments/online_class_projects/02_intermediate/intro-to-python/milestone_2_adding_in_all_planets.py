MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0


def mars_on_weight():
    while True:
        try:
            # get Value in FLOAT
            earth_weight = float(input("⚖️ Enter a Weight on Earth 🌎: "))
            # Break Loop
            break
        except ValueError:
            # Show Error If User Entered Wrong Value
            print("❌ Invalid input. Enter value in KG e.g. 1.25, 0.25, 5")

    # Get Planet Name
    planet = input("🪐 Enter a planet: ")

    # Determine the gravitational constant for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        # can assume user types in one of these planets, so this can be an else instead of elif
        gravity_constant = NEPTUNE_GRAVITY

    # Calculation Earth Weight by Multiply Selected Planet
    planetary_weight = earth_weight * gravity_constant
    # Round of Digits
    rounded_planetary_weight = round(planetary_weight, 2)

    # Print Result
    print(f"⏲️ The equivalent weight on {planet}: {rounded_planetary_weight}")


if __name__ == "__main__":
    mars_on_weight()
