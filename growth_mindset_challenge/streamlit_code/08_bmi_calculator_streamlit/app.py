import streamlit as st


def bmi_calculator():
    st.title("⚖️ BMI Calculator")

    # User Input
    weight = st.number_input(
        "Enter your weight (in KG):", min_value=1.0, step=0.1)
    height = st.number_input("Enter your height (in CM):",
                             min_value=50.0, step=0.1) / 100

    # Button to Calculate BMI
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            st.write(f"📊 **Your BMI is: {bmi:.2f}**")

            # BMI Categories
            if bmi < 18.5:
                st.write("⚠️ Underweight - You may need to gain some weight.")
            elif 18.5 <= bmi < 24.9:
                st.write("✅ Normal Weight - Great! You are healthy. 🎯")
            elif 25 <= bmi < 29.9:
                st.write("⚠️ Overweight - Try to maintain a balanced diet. 🏋️")
            else:
                st.write("🛑 Obese - Consider a healthier lifestyle. 🏃‍♂️")
        else:
            st.error("❌ Please enter valid values.")


# Run App
bmi_calculator()
