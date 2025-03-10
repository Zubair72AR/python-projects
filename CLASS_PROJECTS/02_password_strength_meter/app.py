import streamlit as st
from streamlit_option_menu import option_menu
import re
import string
import random

# Page Title and Fav icon
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
)
# Main Menu
selected = option_menu(
    menu_title=None,
    options=["Check Strength", "Random Password", "Custom Password"],
    icons=["shield-check", "dice-5", "pencil"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>> Function Check Password Strength <<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def check_password_strength(password):
    rating = 0  # Track Rating Numbers
    suggestions = []  # If finds Password Weak
    strength_level = ""  # Password Strength Level
    # Length Check
    if len(password) >= 8:
        rating += 1
    else:
        suggestions.append("❌ Be at least 8 characters long")
    # Upper & Lowercase Check
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        rating += 1
    else:
        suggestions.append("❌ Include both uppercase and lowercase letters")
    # Digit Check
    if re.search(r"\d", password):
        rating += 1
    else:
        suggestions.append("❌ Add at least one number (0-9).")
    # Special Character Check
    if re.search(r"[!@#$%^&*<=>?]", password):
        rating += 1
    else:
        suggestions.append(
            "❌ Include at least one special character (!@#$%^&*).")
    # Blacklist Common Passwords
    blacklist = ["password", "123456", "123", "abc", "xyz", "qwerty",
                 "abc123", "admin", "welcome", "passw0rd", "iloveyou", "football"]
    # FOR LOOP for Checking Blacklisted Words
    common_words = None
    for bad_word in blacklist:
        if re.search(bad_word, password, re.IGNORECASE):
            common_words = bad_word
            rating -= 1
            break
    if common_words:
        suggestions.append(
            f"❌ Your password contains a weak word or pattern -> \"{common_words}\". Please choose a stronger password.")
    # Strength of Password as per Rating
    if rating == 4:
        strength_level = "✅ Strong Password! 🔥"
    elif rating == 3:
        strength_level = "⚠️ Moderate Password - Consider adding more security features."
    else:
        strength_level = "❌ Weak Password - Improve it using the suggestions below."

    # Return strength rating (0 to 4), suggestions, and strength level
    return rating, suggestions, strength_level


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>> Check Strength <<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if selected == "Check Strength":
    st.markdown("<h1 style='text-align: center; color:#ef233c;' >Password Strength Meter</h1>",
                unsafe_allow_html=True)  # Main Title
    st.markdown("<h5 style='text-align: center; color:gray;' >Make Your Password Stronger Than Hackers!</h5>",
                unsafe_allow_html=True)  # Subtitle
    # Get user input
    password = st.text_input(
        "🔒 Enter Your Password:", placeholder="e.g., Imran_Khan@804", type="password", help="🔹 Use at least 8 characters\n🔹 Include uppercase, lowercase, numbers & symbols\n🔹 Avoid common words")
    # calling function and storing into variables
    rating, suggestions, strength_level = check_password_strength(password)
    # If user press button to check password strength
    if st.button("Check Password Strength"):
        # Check if Password Contains any Space
        if " " in password:
            # Show Error
            st.error(
                "⚠️ Your password contains spaces. Some systems do not allow spaces in passwords.")
            # Show Tip to Use UnderScore instead of Space
            st.markdown(
                "<p style='background:#173928; padding: 8px 16px; border-radius: 5px;' >Tip: Use an underscore \"_\" instead of spaces for better compatibility.</p>", unsafe_allow_html=True)
        elif password:
            # Show strength message
            if rating == 4:
                st.success(strength_level)
                st.code(password, language="plaintext")
            elif rating == 3:
                st.info(strength_level)
            else:
                st.error(strength_level)
            # Show progress bar based on strength
            st.progress(rating / 4)  # Normalizing to a 0-1 scale
            # Show suggestions
            if suggestions:
                st.warning("\n\n".join(suggestions))
        # Show Error if User didn't entered a value
        else:
            st.error("❌ Please enter a password to check its strength.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>> Random Password <<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if selected == "Random Password":
    st.markdown("<h1 style='text-align: center; color:#ef233c;' >Random Password Generator</h1>",
                unsafe_allow_html=True)  # Main Title
    st.markdown("<h5 style='text-align: center; color:gray;' >Get a hack-proof password in one click!</h5>",
                unsafe_allow_html=True)  # Subtitle
    # Length for Generating Random Password
    random_password_length = st.slider(
        "Choose Password Length:", min_value=8, max_value=20, value=12, help="🔹 Recommended: At least 12 characters\n🔹 Longer passwords are more secure")
    # Generate Random Password
    if st.button("Generate Random Password"):
        # Dividing Length (50% LETTERS), (30% DIGITS) and (20% SPECIAL CHARACTERS)
        rand_letter_len = round(random_password_length * 0.5)
        rand_num_len = round(random_password_length * 0.3)
        rand_special_chars_len = random_password_length - (
            rand_letter_len + rand_num_len)
        # Assign List for Random Password
        random_password = []
        # FOR LOOP for Generating 6 Random Passwords
        for _ in range(6):
            # Add Letters as per Provided Qty(50%).
            rand_letter = "".join(random.choice(string.ascii_letters)
                                  for _ in range(rand_letter_len))
            # Add Digits as per Provided Qty(30%).
            rand_num = "".join(random.choice(string.digits)
                               for _ in range(rand_num_len))
            # Add Special Characters as per Provided Qty(20%).
            rand_special_chars = "".join(random.choice(
                "[!@#$%^&*<=>?]") for _ in range(rand_special_chars_len))
            # Assign Variable for LETTERS + DIGITS + SPECIAL CHARACTERS
            password = (rand_letter + rand_special_chars +
                        rand_num).capitalize()
            # Append in List
            random_password.append(password)
        # Print Result in 3 Columns and 2 Rows
        cols = st.columns(3)
        for index, password in enumerate(random_password):
            col_index = index % 3
            with cols[col_index]:
                # Password with Copy Button
                st.code(password, language="plaintext")
        # Show Result - With Details of Included Characters in Passwords
        st.markdown(f"""
                    <p style="text-align: center;color: gray; font-size: 14px; font-weight: 500; line-height: 30px;">🔐Password includes: <code style="font-weight: bold; font-size: 16px;">1</code> uppercase +  
                    <code style="font-weight: bold; font-size: 16px;">{rand_letter_len - 1}</code> lowercase + 
                    <code style="font-weight: bold; font-size: 16px;">{rand_special_chars_len}</code> symbols + <code style="font-weight: bold; font-size: 16px;">{rand_num_len}</code> digits = Total Length 
                    <code style="font-weight: bold; font-size: 16px;">{random_password_length}</code></p>""", unsafe_allow_html=True)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>> Custom Password <<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if selected == "Custom Password":
    st.markdown("<h1 style='text-align: center; color:#ef233c;' >Custom Password Generator</h1>",
                unsafe_allow_html=True)  # Main Title
    st.markdown("<h5 style='text-align: center; color:gray;' >Create your perfect password. Customize strength, length & characters!</h5>",
                unsafe_allow_html=True)  # Subtitle
    # Length for Generating Custom Password
    custom_password_length = st.slider(
        "Choose Password Length:", min_value=5, max_value=20, value=8, help="🔹 Recommended: At least 12 characters\n🔹 Longer passwords are more secure")
    # Click if need to Include Numbers
    include_numbers = st.checkbox(
        "Include numbers in the password?", value=True)
    # Click if need to Include Symbols
    include_special_chars = st.checkbox(
        "Include special characters?", value=True)
    # Get user input
    include_text_name = st.text_input(
        "Enter a specific word or name (optional)? :gray[(*This will extend your password length.*)]", "", placeholder="e.g. Imran_Khan, SirZia, ameen", help="This word will be included in your password.")
    # Function to Generate Custom Password

    def select_password_type(custom_password_length, include_numbers, include_special_chars, include_text_name):
        custom_password = []
        include_uppercase = ""
        include_lowercase = ""
        Add_random_words_len = 0
        # If Finds Length more then 1 and A to Z letters in the User Input
        if re.search(r"[a-zA-Z]", include_text_name) and len(include_text_name) > 1:
            letters_length = 0
            # If Finds Uppercase and Lowercase Both
            if re.search(r"[a-z]", include_text_name) and re.search(r"[A-Z]", include_text_name):
                letters_length = 0
            # Check if User Put Digits or Symbols in the First 2 Index
            elif re.search(r"[a-zA-Z]", include_text_name[0]) and re.search(r"[a-zA-Z]", include_text_name[1]):
                include_text_name = include_text_name.capitalize()
            # If Doesn't Find Uppercase add Uppercase
            elif not re.search(r"[A-Z]", include_text_name):
                include_uppercase = random.choice(string.ascii_uppercase)
                letters_length = 1
            # If Doesn't Find Lowercase add Lowercase
            elif not re.search(r"[a-z]", include_text_name):
                include_lowercase = random.choice(string.ascii_lowercase)
                letters_length = 1
            custom_password_length = custom_password_length - letters_length
            # Adjust Length and Divide into DIgits Symbols
            if include_numbers and include_special_chars:
                special_char_length = round(custom_password_length * 0.40)
                numbers_length = custom_password_length - special_char_length
                Add_random_words_len = 0
            elif include_numbers and not include_special_chars:
                special_char_length = 0
                numbers_length = custom_password_length
                Add_random_words_len = 0
            elif include_special_chars and not include_numbers:
                special_char_length = custom_password_length
                numbers_length = 0
                Add_random_words_len = 0
            else:
                special_char_length = 0
                numbers_length = 0
                Add_random_words_len = custom_password_length
            # FOR LOOP for Generating 6 Custom Passwords
            for _ in range(6):
                # Add Random Words If Digits and Symbols both are not Included
                Add_random_words = "".join(random.choice(
                    string.ascii_letters) for _ in range(Add_random_words_len))
                # Add Symbols
                special_char = "".join(random.choice(
                    "[!@#$%^&*<=>?]") for _ in range(special_char_length))
                # Add Digits
                numbers = "".join(random.choice(string.digits)
                                  for _ in range(numbers_length))
                # Assign Variable for LETTERS + DIGITS + SPECIAL CHARACTERS
                password = (include_uppercase + include_text_name +
                            include_lowercase + special_char + numbers + Add_random_words)
                # Append in List
                custom_password.append(password)

        else:
            # Adjust Length and Divide into DIgits Symbols
            if include_numbers and include_special_chars:
                letters_length = round(custom_password_length * 0.50)
                special_char_length = round(custom_password_length * 0.20)
                numbers_length = custom_password_length - \
                    (special_char_length + letters_length)
            elif include_numbers and not include_special_chars:
                letters_length = round(custom_password_length * 0.6)
                special_char_length = 0
                numbers_length = custom_password_length - letters_length
            elif include_special_chars and not include_numbers:
                letters_length = round(custom_password_length * 0.6)
                special_char_length = custom_password_length - letters_length
                numbers_length = 0
            else:
                letters_length = custom_password_length
                special_char_length = 0
                numbers_length = 0
            # FOR LOOP for Generating 6 Custom Passwords
            for _ in range(6):
                # Add Letters
                letters = "".join(random.choice(string.ascii_lowercase)
                                  for _ in range(letters_length))
                # Add Digits
                numbers = "".join(random.choice(string.digits)
                                  for _ in range(numbers_length))
                # Add Symbols
                special_char = "".join(random.choice(
                    "[!@#$%^&*<=>?]") for _ in range(special_char_length))
                # Assign Variable for LETTERS + DIGITS + SPECIAL CHARACTERS
                password = (letters +
                            special_char + numbers + include_text_name).capitalize()
                # Append in List
                custom_password.append(password)
        # If Condition User Didn't Use Space
        if " " not in include_text_name:
            # Print Result in 3 Columns and 2 Rows
            custom_cols = st.columns(3)
            for index, cus_password in enumerate(custom_password):
                custom_col_index = index % 3
                with custom_cols[custom_col_index]:
                    # Password with Copy Button
                    st.code(cus_password, language="plaintext")
            # Show Result - With Details of Included Characters in Passwords
            if include_text_name:
                st.markdown(f"""
                        <p style="text-align: center;color: gray; font-size: 14px; font-weight: 500; line-height: 30px;">✅ Your Input: <code style="font-weight: bold; font-size: 16px;">{include_text_name}</code> = <code style="font-weight: bold; font-size: 16px;">{len(include_text_name)}</code> characters +</p>""", unsafe_allow_html=True)
            st.markdown(f"""
                        <p style="text-align: center;color: gray; font-size: 14px; font-weight: 500; line-height: 30px;">📌 Added: <code style="font-weight: bold; font-size: 16px;">{letters_length + Add_random_words_len}</code> letters + <code style="font-weight: bold; font-size: 16px;">{special_char_length}</code> special characters + <code style="font-weight: bold; font-size: 16px;">{numbers_length}</code> digits = Total Password Length <code style="font-weight: bold; font-size: 16px;">{len(password)}</code></p>""",
                        unsafe_allow_html=True)
    # Button for Generating Random Password
    if st.button("Generate Random Password"):
        select_password_type(custom_password_length, include_numbers,
                             include_special_chars, include_text_name)
    # Check if Input Contains any Space
    if " " in include_text_name:
        # Show Error
        st.error(
            "⚠️ Your word or name contains spaces. Some systems do not allow spaces in passwords.")
        # Show Tip to Use UnderScore instead of Space
        st.markdown(
            "<p style='background:#173928; padding: 8px 16px; border-radius: 5px;' >Tip: Use an underscore \"_\" instead of spaces for better compatibility.</p>", unsafe_allow_html=True)

# Footer
st.markdown("""<p style="color: #2f3038; text-align: center">Made with ❤ by Zubair Ahmed</p>""",
            unsafe_allow_html=True)
