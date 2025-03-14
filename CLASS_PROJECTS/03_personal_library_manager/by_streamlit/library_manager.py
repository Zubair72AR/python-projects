import streamlit as st

# Main Title
st.markdown(f"<p style='text-align: center; line-height: 5px; color: gray; text-transform: capitalize; letter-spacing: 8px; font-weight: 100'>Welcome to your</p>",
            unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; line-height: 5px;'>📖 Personal Library Manager</h1>",
            unsafe_allow_html=True)
# Main Menu Navigation
navigation_menu = ["Add a book",
                   "Remove a book",
                   "Search for a book",
                   "Display all books",
                   "Display statistics",
                   "Exit",]
# Button to Navigate the Page
selected_option = st.sidebar.radio(
    "Choose an option:", navigation_menu)


def Add_book():
    pass


def Remove_book():
    pass


def Search_book():
    pass


def Display_books():
    pass


def Display_statistics():
    pass


def Exit():
    pass
