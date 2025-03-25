import streamlit as st

# Main Title
st.markdown(f"""<div style=" display: flex; align-items: center; justify-content: center; gap: 8px; color: gray; letter-spacing: 1px;
      ">Class Assignments by:<div style=" display: flex; align-items: center; justify-content: center; gap: 5px;"><a  style="color: #0a66c2" href="https://www.linkedin.com/in/aliaftabsheikh/" target="_blank"><i class="fa-brands fa-linkedin"></i></a><a  style="color: white" href="https://github.com/aliaftabsheikh" target="_blank"><i class="fa-brands fa-github"></i><i class="fa-brands fa-square-github"></i></a>Ali Aftab Sheikh,</div><div style=" display: flex; align-items: center; justify-content: center; gap: 5px;"><a style="color: #0a66c2" href="https://www.linkedin.com/in/developerbilalkhan/" target="_blank" ><i class="fa-brands fa-linkedin"></i></a><a  style="color: white" href="https://github.com/Muhammad-Bilal90" target="_blank"><i class="fa-brands fa-github"></i><i class="fa-brands fa-square-github"></i></a>Muhammad Bilal</div></div>""", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; line-height: 10px; margin-bottom: 15px;'>🎯 Problem Solving Challenges 🚀</h1>",
            unsafe_allow_html=True)


# Link of Font Awesome Icons
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">',
    unsafe_allow_html=True
)

# Sidebar Menu
st.sidebar.write("🚀 Select an Assignment:")
problem_type = st.sidebar.radio("", [":gray[Problem 1:] \n\n:green[Reverse a String]",
                                     ":gray[Problem 2:] \n\n:red[Count Vowels in a String]", ":gray[Problem 3:] \n\n:blue[Sum of Digits]"])


if problem_type == ":gray[Problem 1:] \n\n:green[Reverse a String]":
    # SubHeading
    st.markdown(
        "<h5 style='text-align: center;color: #AC92EB;'>1️⃣ Reverse a String</h5>",
        unsafe_allow_html=True)
    # Get User Input to reverse
    user_input01 = st.text_input(
        ":gray[Enter a string to reverse:]", placeholder="e.g., Hello World")
    # If User Press Button
    if st.button("Reverse a String"):
        # Color for CSS Styling
        rainbow_color = ["#FED402", "#FBAE18", "#F7901E", "#EE5626", "#FF0000",
                         "#C41A7E", "#642C90", "#1F2593", "#1560AE", "#00A4C5", "#14B04B", "#88C540"]
        # If User Provided Value
        if user_input01:
            # Reverse by Using Slicing
            reversed_simple_text = user_input01[::-1]
            # Loop Append List
            styled_original_str = []
            for index, r_str in enumerate(user_input01):
                # Getting Index number for Colors CSS Style
                color_str = rainbow_color[index % len(rainbow_color)]
                # First and Last numbering
                index = "First" if index == 0 else (
                    "Last" if index == len(user_input01) - 1 else index + 1)
                # Handling Spaces
                r_str = "󠀠" if r_str == " " else r_str
                # CSS Styling
                num = f"<div style='text-align: center;background-color: #262730;font-size: 15px; font-weight: 400; border-radius: 5px; width:40px;'>{index}<span style='line-height: 42px; background-color: {color_str}; font-size: 30px; border-radius: 5px; color:white; font-weight: 600; width:100%; display:grid; place-items: center;'>{r_str.upper()}</span></div>"
                styled_original_str.append(num)
            # Join Original Sequence for Display
            original_str = "".join(styled_original_str)
            # Join Reversed Sequence
            reversed_str = "".join(styled_original_str[::-1])

            # Display Result
            st.write(f":gray[Here’s Your Reversed Text:]")
            # Reversed Text for Copying
            st.code(reversed_simple_text)
            # Original Text Characters breakdown
            st.write(f":gray[❤️ Original Text Breakdown:]")
            st.markdown(f"""<div class="display_div">{original_str}</div>""",
                        unsafe_allow_html=True)
            # Reversed Text Characters breakdown
            st.write(f":gray[🔥 Reversed Text Breakdown:]")
            st.markdown(f"""<div class="display_div">{reversed_str}</div>""",
                        unsafe_allow_html=True)

        else:
            st.error("❌ Please enter a valid string to reverse.")
if problem_type == ":gray[Problem 2:] \n\n:red[Count Vowels in a String]":
    # SubHeading
    st.markdown(
        "<h5 style='text-align: center;color: #AC92EB;'>2️⃣ Count Vowels in a String</h5>",
        unsafe_allow_html=True)
    # get User Input
    user_input02 = st.text_input(
        ":gray[Enter a string to count vowels:]", placeholder="e.g., Apple")
    # BUtton Pressed
    if st.button("Count Vowels in a String"):
        if user_input02:
            # Vowels in Dicts
            vowels_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
            # 5 Colors Combo to Display Vowels
            five_color = ["#D81920", "#F25822",
                          "#FDAF16", "#03A652", "#008dd0"]
            # For Loop for Provided Value
            for v in user_input02.lower():
                # Check Each Word Include Vowels
                if v in vowels_count:
                    # if Find Vowels increase Value by 1
                    vowels_count[v] += 1

            # Get Sum of All Vowels
            total_vowels = sum(vowels_count.values())
            st.markdown(
                f"""<div class="display_div">❤️ There are <span style='padding: 2px 10px; background-color: #1A159E; border-radius: 5px; color:white;font-weight: 600;'>{total_vowels}</span>Vowels in the <span style='padding: 2px 10px; background-color: crimson; border-radius: 5px;color:white;'>{user_input02}</span></div>""", unsafe_allow_html=True)
            st.write(f":gray[⭒ ⭒ ⭒ ⭒ ⭒ ⭒ ]")
            st.write(f":gray[Breakdown of vowels:]")
            # #262730 gray #0E1117 dark
            all_vowels = []
            for (vowels, qty), color in zip(vowels_count.items(), five_color):
                is_visible = "0.1" if qty == 0 else "1"
                active_color = "white"
                vowels_data = f"<div style='display: flex; justify-content: space-between; align-items: center; width: 60px; background-color: {active_color}; opacity:{is_visible}; border-radius: 5px; over-flow: hidden;'><span style='font-size: 20px; font-weight: 600; border-radius: 5px; color: {color}; display: grid; place-items: center; width: 40px'>{vowels.upper()}</span><span style=' background-color: {color}; font-size: 20px; font-weight: 600; border-radius: 5px; color: {active_color}; display: grid; place-items: center; width: 40px'>{qty}</span></div>"
                all_vowels.append(vowels_data)
            display_vowels = " ✩ ".join(all_vowels)
            st.markdown(f"""<div class="display_div">{display_vowels}</div>""",
                        unsafe_allow_html=True)

        else:
            st.error("❌ Please enter a valid string to count vowels.")
if problem_type == ":gray[Problem 3:] \n\n:blue[Sum of Digits]":
    # SubHeading
    st.markdown(
        "<h5 style='text-align: center;color: #AC92EB;'>3️⃣ Sum of Digits</h5>",
        unsafe_allow_html=True)
    # Number Input Field (Default value: 12345)
    user_input03 = st.number_input(
        ":gray[Enter a number to sum its digits:]", min_value=1, step=1, value=12345)
    if st.button("Sum of Digits"):
        if user_input03:
            # Store Variable
            total = 0
            # 6 Colors Combo to Display Numbers
            six_color = ["#D81920", "#F25822",
                         "#FDAF16", "#03A652", "#008dd0", "#444DA3"]
            # Variable to Displaying Number in CSS Style for Better UI Experience
            styled_numbers = []
            # For Loop
            for index, value in enumerate(str(user_input03)):
                # total Variable = Updated total Variable + Iteration Num of Integer
                total += int(value)
                # Track Colors Index 0 to 5 Number for Repeating Colors
                color = six_color[index % len(six_color)]
                # Add CSS Styling to Each Numbers
                num = f"<span style=' background-color: {color}; font-size: 20px; font-weight: 6; padding: 1px 10px; border-radius: 3px; color: white;'>{value}</span>"
                styled_numbers.append(num)
            # make One Color + For Matching Sequence of Colors
            total_color = six_color[(index + 1) % len(six_color)]
            # Display CSS Styled Number by Joining "+" Sign
            display_sum = "+".join(styled_numbers)
            # Include Total with "=" Sign and also CSS Colors for Total
            display_sum += f"=<span style=' background-color: {total_color}; font-size: 20px; font-weight: 6; padding: 1px 20px; border-radius: 3px; color: white;'>{total}</span>"
            # Display Result
            st.write(f":gray[Calculated Sum of Digits:]")
            st.markdown(f"""<div class="display_div">{display_sum}</div>""",
                        unsafe_allow_html=True)

        else:
            st.error("❌ Please enter a valid number to sum digits.")


# CSS Properties if Required
st.markdown("""
    <style>
.display_div{display: flex; flex-wrap: wrap; justify-content: start;align-items: center;gap: 6px; color:gray; margin-bottom:6px;}
    </style>
""", unsafe_allow_html=True)


# Footer
st.markdown("""<p style="color: #2f3038; text-align:center;">Made with ❤ by Zubair Ahmed</p>""",
            unsafe_allow_html=True)
