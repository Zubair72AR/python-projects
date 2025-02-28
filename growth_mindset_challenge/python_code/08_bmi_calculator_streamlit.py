def bmi_calculator():

    # WEIGHT Input and Error Handling if User Enter Wrong Value
    while True:
        try:
            weight = float(input("⚖️ Enter your weight (in KG): "))
            if weight <= 0:
                print(
                    "❌ Weight must be a positive number (e.g., 50, 70, 90). Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value (e.g., 50, 70, 90).")
    # HEIGHT Input and Error Handling if User Enter Wrong Value
    while True:
        try:
            height = float(input("📏 Enter your height (in CM): ")) / 100
            if height <= 0:
                print(
                    "❌ Height must be a positive number (e.g., 150, 165, 180). Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value (e.g., 150, 165, 180).")

    # BMI Calculating
    bmi = weight / (height ** 2)

    # Printing the BMI Results
    print("\n📊 Your BMI Results:")
    print(f"🔢 Your BMI is: {bmi:.2f}")

    # CConditional Result as per User BMI
    if bmi < 18.5:
        print("⚠️ Underweight - You may need to gain some weight for a healthier balance.")
    elif 18.5 <= bmi < 24.9:
        print("✅ Normal Weight - Great! You have a healthy weight. Keep it up! 🎯")
    elif 25 <= bmi < 29.9:
        print("⚠️ Overweight - Consider maintaining a balanced diet and exercise. 🏋️")
    elif 30 <= bmi < 34.9:
        print("🛑 Obese (Class I) - It's recommended to adopt a healthier lifestyle. 🏃‍♂️🥗")
    elif 35 <= bmi < 39.9:
        print("🛑 Obese (Class II) - Increased health risks! Seek professional advice. 👨‍⚕️")
    else:
        print("🚨 Obese (Class III) - High health risk! Please consult a healthcare provider. 🏥")


if __name__ == "__main__":
    bmi_calculator()
