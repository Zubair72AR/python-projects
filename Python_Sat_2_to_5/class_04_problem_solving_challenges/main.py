import streamlit as st

# Main Title
st.markdown(f"""<div style=" display: flex; align-items: center; justify-content: center; gap: 8px; color: gray; letter-spacing: 1px;
      ">Class Assignments by:<div style=" display: flex; align-items: center; justify-content: center; gap: 5px;"><a  style="color: #0a66c2" href="https://www.linkedin.com/in/aliaftabsheikh/" target="_blank"><i class="fa-brands fa-linkedin"></i></a><a  style="color: white" href="https://github.com/aliaftabsheikh" target="_blank"><i class="fa-brands fa-github"></i><i class="fa-brands fa-square-github"></i></a>Ali Aftab Sheikh,</div><div style=" display: flex; align-items: center; justify-content: center; gap: 5px;"><a style="color: #0a66c2" href="https://www.linkedin.com/in/developerbilalkhan/" target="_blank" ><i class="fa-brands fa-linkedin"></i></a><a  style="color: white" href="https://github.com/Muhammad-Bilal90" target="_blank"><i class="fa-brands fa-github"></i><i class="fa-brands fa-square-github"></i></a>Muhammad Bilal</div></div>""", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; line-height: 5px;'>🎯 Problem Solving Challenges 🚀</h1>",
            unsafe_allow_html=True)


# Link of Font Awesome Icons
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">',
    unsafe_allow_html=True
)

st.sidebar.write("🚀 Select an Assignment:")
problem_type = st.sidebar.radio("", [":gray[Problem 1:] \n\n:green[Reverse a String]",
                                     ":gray[Problem 2:] \n\n:red[Count Vowels in a String]", ":gray[Problem 3:] \n\n:blue[Sum of Digits]"])


if problem_type == ":gray[Problem 1:] \n\n:green[Reverse a String]":
    # SubHeading
    st.markdown(
        "<h5 style='text-align: center;color: #AC92EB;'>1️⃣ Reverse a String</h5>",
        unsafe_allow_html=True)
if problem_type == ":gray[Problem 2:] \n\n:red[Count Vowels in a String]":
    # SubHeading
    st.markdown(
        "<h5 style='text-align: center;color: #AC92EB;'>2️⃣ Count Vowels in a String</h5>",
        unsafe_allow_html=True)
if problem_type == ":gray[Problem 3:] \n\n:blue[Sum of Digits]":
    # SubHeading
    st.markdown(
        "<h5 style='text-align: center;color: #AC92EB;'>3️⃣ Sum of Digits</h5>",
        unsafe_allow_html=True)
