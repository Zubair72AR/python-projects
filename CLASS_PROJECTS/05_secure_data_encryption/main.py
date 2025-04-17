import streamlit as st
import os
import json
import yaml
import hashlib
from yaml.loader import SafeLoader
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from streamlit_authenticator.utilities import *
import time

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - LOADING CONFIG FILE & JSON STORAGE FILE - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Loading config file (Keeps Login and Signup Info)
# Get the full path to the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the config.yaml file
config_path = os.path.join(script_dir, 'config.yaml')

# Loading the config file
with open(config_path, 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)


# Data Storage File Name
STORE_DATA = "store_data.json"


def load_data():
    # Load Data
    if os.path.exists(STORE_DATA):
        with open(STORE_DATA, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}


def save_data(Data):
    # Save Data
    with open(STORE_DATA, "w") as file:
        json.dump(Data, file, indent=4)


# Load Data When App runs
stored_data = load_data()
# Make Session State of Attempt
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
# Reset failed attempts and when logged out
if st.session_state.get("authentication_status") is None:
    st.session_state.failed_attempts = 0
    st.session_state.lock_start_time = 0

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - FUNCTIONS for HASHING AND ENCRYPT & DECRYPT - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def hashing_passkey(passkey):
    # Function to hash passkey using PBKDF2
    salt = os.urandom(16)  # Always generate a new salt
    hashed_passkey = hashlib.pbkdf2_hmac(
        'sha256', passkey.encode(), salt, 100000)
    return b64encode(salt + hashed_passkey).decode()


def verify_passkey(stored_hash, passkey):
    # Function to verify the plain-text passkey
    try:
        decoded = b64decode(stored_hash)
        salt, stored_hashed_passkey = decoded[:16], decoded[16:]
        hashed_passkey = hashlib.pbkdf2_hmac(
            'sha256', passkey.encode(), salt, 100000)
        return stored_hashed_passkey == hashed_passkey
    except:
        return False


# Key Generate or Load
if not os.path.exists("secret.key"):
    KEY = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(KEY)
else:
    with open("secret.key", "rb") as key_file:
        KEY = key_file.read()

cipher = Fernet(KEY)


def encrypt_text(text):
    # Encrypt Data
    try:
        encrypted = cipher.encrypt(text.encode())
        return encrypted.decode()
    except:
        st.error("❌ Failed to encrypt data.")
        return None


def decrypt_text(encrypted_text):
    # Decrypt Data
    try:
        encrypted_bytes = encrypted_text.encode()
        decrypted = cipher.decrypt(encrypted_bytes)
        return decrypted.decode()
    except:
        st.error("❌ Failed to decrypt. Invalid data or passkey.")
        return None


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - PAGE TITLE - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
st.markdown(f"<p style='text-align: center; line-height: 1px; color: #666;font-weight: 100; font-size:14px;'>Use this app to securely store and retrieve data using unique passkeys</p>",
            unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; line-height: 5px;'>🛡️ Secure Data Encryption</h1>",
            unsafe_allow_html=True)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - HOME PAGE IF USER LOGGED IN - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Check authentication status
if st.session_state.get('authentication_status'):
    # Welcome User when logged in
    st.markdown(
        f"<p style='text-align: center; line-height: px; color: gray; letter-spacing:1px;font-weight: 100;'>Welcome Mr./Mrs.<span class='user_display'> {st.session_state['name']}</span></p>", unsafe_allow_html=True)
    # User is logged in
    authenticator.logout('Logout', 'sidebar')  # Logout button
    # Navigation Links
    st.sidebar.write("")
    navigation = st.sidebar.radio(
        "\n\n:gray[Select Navigation:]", ("Store Data", "Retrieve Data",))

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # - - - - - - - - - - STORE DATA - - - - - - - - - -
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if navigation == "Store Data":
        st.markdown(f"<p style='text-align: center; line-height: 10px; margin-top: 25px; color:violet; font-size: 30px; font-weight: 600'>🚀 Store Data Securely</p>", unsafe_allow_html=True)
        # Input for Data Storage and Passkey
        user_added_text = st.text_area(":gray[Enter Data:]")
        user_added_passkey = st.text_input(
            ":gray[Enter Passkey:]", type="password")
        # Button to Encrypt and Storage Data
        if st.button("Encrypt & Save Data"):
            # Check if User Provide Data if Not Then Show Error of Blank Inputs
            if not user_added_text:
                st.error("Please enter the data to be stored.")
            elif not user_added_passkey:
                st.error("Passkey cannot be blank.")
            else:
                # Encrypt Data
                encrypted_text = encrypt_text(user_added_text)
                if encrypted_text:  # Only proceed if encryption succeeded
                    # Hashing Passkey
                    hashed_passkey = hashing_passkey(user_added_passkey)
                    username = st.session_state['username']
                    # make New Entry Dictionary
                    new_entry = {"encrypted_text": encrypted_text,
                                 "passkey": hashed_passkey}

                    # Check If User is New and Storage data in the NEW DICTIONARY by user NAME
                    if username not in stored_data:
                        stored_data[username] = [new_entry]
                        save_data(stored_data)
                        st.success("Data Stored Successfully! ✅")
                        st.code(new_entry["encrypted_text"])
                    else:
                        # If User Exists already
                        duplicate_data = False
                        # Check if Entered Data or Passkey is Duplicate Give Error
                        for entry in stored_data[username]:
                            previous_passkeys = entry["passkey"]
                            if_duplicate_passkey = verify_passkey(
                                previous_passkeys, user_added_passkey)
                            previous_text = entry["encrypted_text"]
                            decrypted_previous_text = decrypt_text(
                                previous_text)
                            # Warning for Data DUPLICATE and Exit from Loop
                            if decrypted_previous_text == user_added_text:
                                duplicate_data = True
                                st.warning("⚠️ Data already exists!")
                                break
                            # Warning for Passkey DUPLICATE and Exit from Loop
                            elif if_duplicate_passkey:
                                duplicate_data = True
                                st.warning("🔑 Passkey already exists!")
                                break

                        if not duplicate_data:
                            # if DATA and PASSKEY are OK APPEND data SAME USER NAME
                            stored_data[username].append(new_entry)
                            save_data(stored_data)
                            st.success("Data Stored Successfully! ✅")
                            st.write(
                                ":gray[**🚀 Your Encrypted Data:** Copy and save this data safely! You will need this encrypted code to retrieve your original data later.]")
                            st.code(new_entry["encrypted_text"])

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # - - - - - - - - - - RETRIEVE DATA - - - - - - - - - -
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if navigation == "Retrieve Data":
        # If FAILED ATTEMPTS >= 3 SHOW LOGOUT BUTTON ONLY with TIMER
        if st.session_state.failed_attempts > 2:
            if st.session_state.lock_start_time == 0:
                # GET TIME & Save it in the SESSION STATE
                st.session_state.lock_start_time = time.time()

            # Show Login Info or Timer
            st.markdown(
                f"<div class='red_gradients'>🔒 You have used 3 incorrect attempts. Please logout and login again to retrieve your data.</div>", unsafe_allow_html=True)

            lock_duration = 300  # in Seconds
            # Placeholder to Show TIME in THE SAME Line
            placeholder = st.empty()

            while True:
                # Get Remaining Time
                elapsed = time.time() - st.session_state.lock_start_time
                remaining = lock_duration - elapsed

                if remaining > 0:
                    # Make Minutes and Seconds
                    minutes = int(remaining // 60)
                    seconds = int(remaining % 60)
                    # Show Time
                    placeholder.write(
                        f"<div style='display: flex;justify-content: center;align-items: center;gap:10px;font-size: 85px;font-weight: 800;line-height: 40px;margin-bottom:20px;'>{minutes:02d}:{seconds:02d}</div>",
                        unsafe_allow_html=True
                    )
                    time.sleep(1)  # Update every second
                else:
                    # When Timer Finishes - > Reset Attempts to Zero and TIME Reset
                    st.session_state.failed_attempts = 0
                    del st.session_state.lock_start_time  # Reset timer
                    st.rerun()
        else:
            st.markdown(f"<p style='text-align: center; line-height: 10px; margin-top: 25px; color:violet; font-size: 30px; font-weight: 600'>🎯 Retrieve Your Data</p>", unsafe_allow_html=True)
            # Input for Data Retrieve and Passkey
            user_encrypted_data = st.text_area(":gray[Enter Encrypted Data:]")
            user_provided_passkey = st.text_input(
                ":gray[Enter Passkey:]", type="password")
            if st.button("Decrypt Data"):
                # Check if User Provide Data if Not Then Show Error of Blank Inputs
                if not user_encrypted_data:
                    st.error("Please enter Encrypted Data to Retrieve.")
                elif not user_provided_passkey:
                    st.error("Passkey cannot be blank.")
                else:
                    username = st.session_state['username']
                    # Check if User Dont Have Data
                    if username not in stored_data or not stored_data[username]:
                        st.error("No data found for this user.")
                    else:
                        found = False
                        for entry in stored_data[username]:
                            previous_passkeys = entry["passkey"]
                            # Hash Passkey to Match with Stored Passkey
                            hashed_passkey = verify_passkey(
                                previous_passkeys, user_provided_passkey)
                            previous_text = entry["encrypted_text"]
                            # Check if Stored Data and Pass key are SAME
                            if previous_text == user_encrypted_data and hashed_passkey:
                                decrypted_previous_text = decrypt_text(
                                    previous_text)
                                # Show Success Message and DATA and Exit from Loop
                                if decrypted_previous_text:
                                    st.success(
                                        "Decrypted Data Successfully! ✅")
                                    st.write(":gray[Your Encrypted Data:]")
                                    st.code(decrypted_previous_text,
                                            language=None)
                                    st.session_state.failed_attempts = 0  # Reset attempts
                                    found = True
                                    break
                        if not found:
                            # If User Provide Wrong Inputs Show "FAILED ATTEMPTS"
                            st.session_state.failed_attempts += 1
                            remaining = 3 - st.session_state.failed_attempts
                            st.error(
                                f"❌ Incorrect passkey! Attempts remaining {remaining}")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - LOGIN AND SIGNUP PAGE IF USER LOGGED OUT - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
else:
    # Menu
    selected = option_menu(
        menu_title=None,
        options=["Login", "Signup"],
        icons=["shield-check", "person-plus"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )
    # Social Media Accounts
    st.markdown(f"""<div class="div_social"><a  class="social_icon" href="https://www.linkedin.com/in/zubair-ahmed-06aa13194/" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a><a  class="social_icon" href="https://github.com/Zubair72AR" target="_blank"><i class="fa-brands fa-github"></i></a><a  class="social_icon" href="https://wa.link/mbzvkr" target="_blank"><i class="fa-brands fa-whatsapp"></i></a><a  class="social_icon" href="https://www.behance.net/zubairar72" target="_blank"><i class="fa-brands fa-behance"></i></a><a  class="social_icon" href="https://www.pinterest.com/ikramjan717/" target="_blank"><i class="fa-brands fa-pinterest-p"></i></a></div>""", unsafe_allow_html=True)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # - - - - - - - - - - LOGIN PAGE - - - - - - - - - -
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if selected == "Login":
        st.markdown(f"<p style='text-align: center; line-height: 25px; margin-top: 30px; color:violet; font-size: 30px; font-weight: 600'>Sign in 👋 to Secure Data</p>", unsafe_allow_html=True)
        # Creating a login widget
        try:
            authenticator.login()
            if st.session_state.get('authentication_status') is False:
                st.error('Username/password is incorrect')
            elif st.session_state.get('authentication_status') is None:
                st.warning('Please enter your username and password')
        except LoginError as e:
            st.error(e)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # - - - - - - - - - - SIGNUP PAGE - - - - - - - - - -
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if selected == "Signup":
        st.markdown(f"<p style='text-align: center; line-height: 25px; margin-top: 30px; color:violet; font-size: 30px; font-weight: 600'>Sign up 👋 to Secure Data</p>", unsafe_allow_html=True)
        # Creating a new user registration widget
        try:
            (email_of_registered_user,
             username_of_registered_user,
             name_of_registered_user) = authenticator.register_user()
            if email_of_registered_user:
                st.success('User registered successfully')
                # Save config file after successful registration
                with open('config.yaml', 'w', encoding='utf-8') as file:
                    yaml.dump(config, file, default_flow_style=False,
                              allow_unicode=True)
        except RegisterError as e:
            st.error(e)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - FOOTER - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
st.markdown("""<p style="color: #2f3038; text-align:center;">Made with ❤ by Zubair Ahmed</p>""",
            unsafe_allow_html=True)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - CSS STYLING AND LINKS - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Link of Font Awesome Icons
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">',
    unsafe_allow_html=True
)
st.markdown("""
    <style>
            input::placeholder {font-size: 14px !important; font-weight: 100 !important;}
        .user_display{
  color: #ff4b4b;
font-size: 20px; 
  font-weight: 900;
            text-transform:uppercase;
  
}
.div_social {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
            
}
            
.social_icon {
  border: 1px solid #ff4b4b;
            color: #ff4b4b !important;
  width: 35px;
  height: 35px;
  display: grid;
  place-items: center;
  border-radius: 50%;
text-decoration: none !important;
             transition: all 0.5s ease-in;
            
}
            .div_social .social_icon:hover {
            color: white !important;
            background-color: #ff4b4b;
  border-radius: 50%;
            scale: 1.15;
}
            .red_gradients{
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, red, crimson);
            padding: 20px 10px;
            margin: 50px 0px; 
            border-radius: 5px;
            color: white;
            font-weight: 600;}
            
    </style>
""", unsafe_allow_html=True)
