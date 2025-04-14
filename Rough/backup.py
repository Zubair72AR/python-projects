import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, firestore
import requests

try:
    # Initialize Firebase (with error handling to avoid multiple initializations)
    if not firebase_admin.get_app():
        cred = credentials.Certificate(
            "encrypt-6b476-84ed9a6550de.json"
        )
        firebase_admin.initialize_app(cred)
except ValueError:
    pass  # App already initialized

# Initialize Firestore
db = firestore.client()

st.session_state
# Initialize session state
if "user" not in st.session_state:
    st.session_state.user = {"email": "", "uid": "",
                             "display_name": "", "id_token": ""}
if "page" not in st.session_state:
    st.session_state.page = "login"

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#           MAIN PAGE HEADING AND INFO
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Page Title and Fav icon
st.set_page_config(
    page_title="Secure Data Encryption",
    page_icon="🛡️",
)
# Main Title
st.markdown(f"<p style='text-align: center; line-height: 5px; color: gray; letter-spacing: 8px; font-weight: 100'>Welcome to your</p>",
            unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; line-height: 5px;'>🛡️ Secure Data Encryption</h1>",
            unsafe_allow_html=True)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#           LOGIN and SIGNUP
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if not st.session_state.user["email"]:
    if st.session_state.page["login"]:
        st.markdown(f"<p style='text-align: center; line-height: 25px; margin-top: 30px; color:crimson; font-size: 30px; font-weight: 600'>Sign in 👋 to Secure Data</p>", unsafe_allow_html=True)
        # Social Media Accounts
        st.markdown(f"""<div class="div_social"><a  class="social_icon" href="https://www.linkedin.com/in/zubair-ahmed-06aa13194/" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a><a  class="social_icon" href="https://github.com/Zubair72AR" target="_blank"><i class="fa-brands fa-github"></i></a><a  class="social_icon" href="https://wa.link/mbzvkr" target="_blank"><i class="fa-brands fa-whatsapp"></i></a><a  class="social_icon" href="https://www.behance.net/zubairar72" target="_blank"><i class="fa-brands fa-behance"></i></a><a  class="social_icon" href="https://www.pinterest.com/ikramjan717/" target="_blank"><i class="fa-brands fa-pinterest-p"></i></a></div>""", unsafe_allow_html=True)

        def login(email, password):
            api_key = "AIzaSyBW5aIWzO80HgndScaRu_IgEQObAo37ph4"
            url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": True
            }
            try:
                response = requests.post(url, json=payload)
                if response.ok:
                    data = response.json()
                    st.session_state.user = {
                        "uid": data["localId"],
                        "email": data["email"],
                        "display_name": data.get("displayName", ""),
                        "id_token": data["idToken"]
                    }
                    return True
                st.error("Invalid email or password")
                return False
            except:
                st.error("Login failed. Please try again.")
                return False

        user_email = st.text_input(":gray[💌 Email:]",
                                   placeholder="e.g. testmail@gmail.com")
        user_password = st.text_input(":gray[🔒 Password:]",
                                      placeholder="e.g. mypassword$123", type="password")

        # Login button
        if st.button("🚀 LOGIN"):
            if user_email and user_password:
                if login(user_email, user_password):
                    st.success(
                        f"Logged in as {st.session_state.user['email']}!")
            else:
                st.error("Please fill in all fields.")
        signup_page = st.checkbox("Don't have an account? Sign up here")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#           ENCRYPTING DATA
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#           FOOTER
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
st.markdown("""<p style="color: #2f3038; text-align:center;">Made with ❤ by Zubair Ahmed</p>""",
            unsafe_allow_html=True)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#           CSS PROPERTIES and LINKS
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Link of Font Awesome Icons
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">',
    unsafe_allow_html=True
)
st.markdown("""
    <style>
            input::placeholder {font-size: 14px !important; font-weight: 100 !important;}
.div_social {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}
.social_icon {
  border: 1px solid gray;
            color: gray !important;
  width: 40px;
  height: 40px;
  display: grid;
  place-items: center;
  border-radius: 50%;
text-decoration: none !important;
}
            
    </style>
""", unsafe_allow_html=True)


# Verify token to maintain login state (optional, for robustness)
def verify_token():
    if st.session_state.user["id_token"]:
        try:
            # Use Firebase Admin SDK to verify token
            decoded_token = auth.verify_id_token(
                st.session_state.user["id_token"])
            return decoded_token["email"] == st.session_state.user["email"]
        except:
            st.session_state.user = {
                "email": "", "uid": "", "display_name": "", "id_token": ""}
            return False
    return False


# Check login status
is_logged_in = st.session_state.user["email"] and verify_token()
