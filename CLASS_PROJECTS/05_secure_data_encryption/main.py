import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import *
from streamlit_option_menu import option_menu
import os
import json


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - LOADING CONFIG FILE - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Loading config file (Keeps Login and Signup Info)
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

STORE_DATA = "store_data.json"


def load_data():
    # Load Library
    if os.path.exists(STORE_DATA):
        with open(STORE_DATA, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_data(library):
    # Save Library
    with open(STORE_DATA, "w") as file:
        json.dump(library, file, indent=4)


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
    st.markdown(f"<p style='text-align: center; line-height: px; color: gray; letter-spacing:1px;font-weight: 100;'>Welcome Mr./Mrs.<span class='user_display'> {st.session_state["name"]}</span></p>",
                unsafe_allow_html=True)
    # User is logged in
    authenticator.logout('Logout', 'sidebar')  # Logout button
    st.sidebar.write("")
    navigation = st.sidebar.radio(
        "\n\n:gray[Select Navigation:]", ("Store Data", "Retrieve Data",))

    if navigation == "Store Data":
        st.markdown(f"<p style='text-align: center; line-height: 10px; margin-top: 25px; color:violet; font-size: 30px; font-weight: 600'>🚀 Store Data Securely</p>", unsafe_allow_html=True)
        user_data = st.text_area(":gray[Enter Data:]")
        passkey = st.text_input(":gray[Enter Passkey:]", type="password")
        if st.button("Encrypt & Save"):
            st.success("successfull")
            st.code(user_data)
    if navigation == "Retrieve Data":
        st.markdown(f"<p style='text-align: center; line-height: 10px; margin-top: 25px; color:violet; font-size: 30px; font-weight: 600'>🎯 Retrieve Your Data</p>", unsafe_allow_html=True)


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
        st.markdown(f"<p style='text-align: center; line-height: 25px; margin-top: 30px; color:crimson; font-size: 30px; font-weight: 600'>Sign in 👋 to Secure Data</p>", unsafe_allow_html=True)
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
        st.markdown(f"<p style='text-align: center; line-height: 25px; margin-top: 30px; color:crimson; font-size: 30px; font-weight: 600'>Sign up 👋 to Secure Data</p>", unsafe_allow_html=True)
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
            
    </style>
""", unsafe_allow_html=True)
