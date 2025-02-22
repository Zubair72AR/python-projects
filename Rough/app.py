import streamlit as st


def self_introduction():
    st.write("Growth Mindset Challenge by Sir Zia Khan")
    st.write("Mad libs Python Project")
    st.title("Self Introduction Form ❤")

    # Name Input
    name = st.text_input("Enter your name:").title()

    # Age Input
    age = st.number_input("Enter your age:", min_value=1, step=1)

    # Gender Input
    gender = st.radio("Select your gender:", ["Boy", "Girl"])

    # Love Input
    loves = st.text_input(
        "Whom/What do you love? e.g. Mama, Papa, Cricket").capitalize()

    # Hobby Input
    hobby = st.text_input(
        "Enter your hobby: e.g. watching history videos").lower()

    # Show Result
    if st.button("Introduce Me!"):
        if name and loves and hobby:
            his_her = "his" if gender.lower() == "boy" else "her"
            he_she = "He" if gender.lower() == "boy" else "She"
            year_label = "year" if age == 1 else "years"

            st.success(f"Meet {name}, {he_she} is {age} {year_label} old {gender.lower()}. Who loves {loves} and enjoys {hobby} in {his_her} free time. {he_she} is always ready for new adventures! 😊")
        else:
            st.error("❌ Barhe Harami ho Beta.")


# Run the app
self_introduction()
