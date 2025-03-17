import streamlit as st
import json
import os

# Define library file path
library_file = "library.json"

book_color = ["#EC3E37", "#75088B", "#FB8600", "#34A853",
              "#FD5C9D", "#833A21", "#FBBC05", "#0357AF"]


def load_library():
    # Load Library
    if os.path.exists(library_file):
        with open(library_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_library(library):
    # Save Library
    with open(library_file, "w") as file:
        json.dump(library, file, indent=4)


# Save it into List
library = load_library()

# Main Title
st.markdown(f"<p style='text-align: center; line-height: 5px; color: gray; letter-spacing: 8px; font-weight: 100'>Welcome to your</p>",
            unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; line-height: 5px;'>📖 Personal Library Manager</h1>",
            unsafe_allow_html=True)
# Main Menu Navigation
navigation_menu = ["Add a book",
                   "Remove a book",
                   "Search for a book",
                   "Display all books",
                   "Display statistics",]
# Button to Navigate the Page
selected_option = st.sidebar.radio(
    "Choose an option:", navigation_menu)
# Add a Book
if selected_option == navigation_menu[0]:
    # SubHeading for Add a Book
    st.markdown(f"<h5 style='text-align: center; line-height: 15px; margin-top: 20px;color: #AC92EB; font-weight: 400'>Enter book details and add them to your collection</h5>", unsafe_allow_html=True)
    # Inputs for Adding New Book in the Columns
    col1_add, col2_add = st.columns([1, 1])
    # Input for Title
    with col1_add:
        add_title = st.text_input(":gray[Enter the book title:]",
                                  placeholder="e.g. AI Revolution")
    # Input for Author Name
    with col2_add:
        add_author = st.text_input(
            ":gray[Enter the author:]", placeholder="e.g. John Doe")
    col3_add, col4_add = st.columns([1, 1])
    # Input for Year
    with col3_add:
        add_year = st.number_input(":gray[Enter the publication year:]",
                                   min_value=1900, max_value=2100, step=1, format="%d", placeholder="e.g. 2025")
    # Input for Genre
    with col4_add:
        add_genre = st.text_input(":gray[Enter the genre:]",
                                  placeholder="e.g. Science Fiction")
    add_read = st.checkbox(":gray[Have you read this book?]", value=True)
    # Save New Book Button
    if st.button(":green[✚ Add Book]"):
        # Check if Title is Duplicate
        is_duplicate = False
        for book in library:
            if book["title"].lower() == add_title.lower():
                is_duplicate = True
                break
        # Validate Inputs (Ensure all fields are filled)
        if add_title and add_author and add_genre and add_year:
            if is_duplicate:
                st.error("❌ Book title already exists! Try a different title.")
            else:
                # Create a new book entry
                new_book = {
                    "title": add_title,
                    "author": add_author,
                    "year": add_year,
                    "genre": add_genre,
                    "read": add_read
                }
                # Append and Save
                library.append(new_book)
                save_library(library)
                # Success Message
                st.success(f"✅ Book ❝{add_title}❞ added successfully!")
        else:
            st.error("❌ Please fill in all fields before adding the book.")

# Remove a book
if selected_option == navigation_menu[1]:
    # SubHeading for Remove a book
    st.markdown(f"<h5 style='text-align: center; line-height: 15px; margin-top: 15px;color: #4FC1E8; font-weight: 400'>Select a book to remove from the library</h5>", unsafe_allow_html=True)
    # if Library is Empty
    if not library:
        st.markdown(
            f"<div style='display: flex;justify-content: center;align-items: center;background: linear-gradient(135deg, red, green);padding: 20px 10px; margin: 30px 0px; border-radius: 5px;color: white;font-weight: 100;'>⊘ The library is currently empty. Add a book to get started.</div>", unsafe_allow_html=True)
    else:
        # Get Input of Book to be Remove
        remove_book = st.text_input(":gray[Enter the title of the book to remove:]",
                                    placeholder="e.g. AI Revolution")
        # Check Initial Length
        initial_len = len(library)
        # Remove Book Button
        if st.button(":red[✘ Remove Book]"):
            # For Loop for Checking if Book Available
            new_library = [
                book for book in library if book["title"] != remove_book]
            # If User Keeps Blank Input
            if not remove_book:
                st.error(
                    "❌ Title cannot be blank. Please enter the book title again.")
            # if Find Length
            elif len(new_library) < initial_len:
                # Save new Library
                save_library(new_library)
                st.success(f"✅ Book ❝{remove_book}❞ removed successfully.")
            else:
                st.error(f"❌ Book ❝{remove_book}❞ not found in the library.")

    # Search for a book
if selected_option == navigation_menu[2]:
    # SubHeading for Search for a book
    st.markdown(f"<h5 style='text-align: center; line-height: 15px; margin-top: 15px;color: #A0D568; font-weight: 400'>Find books by title or author</h5>", unsafe_allow_html=True)
    # if Library is Empty
    if not library:
        st.markdown(
            f"<div style='display: flex;justify-content: center;align-items: center;background: linear-gradient(135deg, red, green);padding: 20px 10px; margin: 30px 0px; border-radius: 5px;color: white;font-weight: 100;'>⊘ The library is currently empty. Add a book to get started.</div>", unsafe_allow_html=True)
    else:
        # Get Input of Book to be Searched
        search_book = st.text_input(":gray[Search for a book by title, author, genre or year:]",
                                    placeholder="e.g. AI Revolution").lower()
        # Remove Book Button
        if st.button(":orange[🔍︎ Search Book]"):
            # For Loop
            display_search_books = [
                book for book in library if (
                    search_book in book["title"].lower() or
                    search_book in book["author"].lower() or
                    search_book in book["genre"].lower() or
                    # Convert year to string for partial matching
                    search_book in str(book["year"])
                )
            ]
            if not search_book:
                st.error(
                    "❌ Please enter a book title, author, genre, or year to search.")
            # IF finds book in search then show
            elif len(display_search_books) > 0:
                # Display in the columns
                display_col = st.columns([1, 1, 1])
                # For Loop to Display
                for index, book in enumerate(display_search_books, start=1):
                    # Get Index of Column and Display
                    col_index = (index - 1) % 3
                    color_index = (index-1) % 8
                    read_unread = "🟢 Read" if book["read"] else "🔴 Unread"
                    with display_col[col_index]:
                        # Displaying Book
                        st.markdown(
                            f"""<div style=" background-color: white; border-radius: 5px; padding: 25px; text-align: center; margin: 8px 0px; font-weight: 100; font-size: 10px; position: relative; height: 270px; overflow: hidden;"><div style=" background-color: {book_color[color_index]}; width: 100%; height: 15%; position: absolute; top: 0; left: 0;"></div><p style="font-size: 25px; color: {book_color[color_index]}; font-weight: 900; text-transform: uppercase;  line-height:22px;  position: relative; top: 5.2%;">{book["title"]}</p><span style="color: gray; margin-top:50px;">Author</span><p style="font-size: 10px; color: #222222; line-height: 5px; ">{book["author"]}</p><span style="color: gray">Genre</span><p style="font-size: 10px;color: #222222; line-height: 5px;">{book["genre"]}</p><p style=" position: absolute; left: 50%; transform: translate(-50%); bottom: 5%; font-size: 25px; line-height: 35px; color: #111111; border-radius: 5px 0px 0px 5px; font-weight: 700;">{book["year"]}</p></div><p>{read_unread}</p><div style=" background-color: {book_color[color_index]}; width: 100%; height: 3px; position: absolute; bottom: 15%; left: 0;" ></div>""", unsafe_allow_html=True)
            # if not find in the Search
            elif len(display_search_books) == 0:
                st.error(
                    "❌ No matching books found. Please try a different title, author, genre, or year.")
# Display all books
if selected_option == navigation_menu[3]:
    # SubHeading for Display all books
    st.markdown(f"<h5 style='text-align: center; line-height: 15px; margin-top: 15px;color: #FFCE54; font-weight: 400'>View your entire book collection</h5>", unsafe_allow_html=True)
    # if Library is Empty
    if not library:
        st.markdown(
            f"<div style='display: flex;justify-content: center;align-items: center;background: linear-gradient(135deg, red, green);padding: 20px 10px; margin: 30px 0px; border-radius: 5px;color: white;font-weight: 100;'>⊘ The library is currently empty. Add a book to get started.</div>", unsafe_allow_html=True)
    else:
        # Display in the columns
        display_col = st.columns([1, 1, 1])
        # For Loop to Display
        for index, book in enumerate(library, start=1):
            # Get Index of Column and Display
            col_index = (index - 1) % 3
            color_index = (index-1) % 8
            read_unread = "🟢 Read" if book["read"] else "🔴 Unread"
            with display_col[col_index]:
                # Displaying Book
                st.markdown(
                    f"""<div style=" background-color: white; border-radius: 5px; padding: 25px; text-align: center; margin: 8px 0px; font-weight: 100; font-size: 10px; position: relative; height: 270px; overflow: hidden;"><div style=" background-color: {book_color[color_index]}; width: 100%; height: 15%; position: absolute; top: 0; left: 0;"></div><p style="font-size: 25px; color: {book_color[color_index]}; font-weight: 900; text-transform: uppercase;  line-height:22px;  position: relative; top: 5.2%;">{book["title"]}</p><span style="color: gray; margin-top:50px;">Author</span><p style="font-size: 10px; color: #222222; line-height: 5px; ">{book["author"]}</p><span style="color: gray">Genre</span><p style="font-size: 10px;color: #222222; line-height: 5px;">{book["genre"]}</p><p style=" position: absolute; left: 50%; transform: translate(-50%); bottom: 5%; font-size: 25px; line-height: 35px; color: #111111; border-radius: 5px 0px 0px 5px; font-weight: 700;">{book["year"]}</p></div><p>{read_unread}</p><div style=" background-color: {book_color[color_index]}; width: 100%; height: 3px; position: absolute; bottom: 15%; left: 0;" ></div>""", unsafe_allow_html=True)

# Display statistics
if selected_option == navigation_menu[4]:
    # SubHeading for Display statistics
    st.markdown(f"<h5 style='text-align: center; line-height: 15px; margin-top: 15px;color: #ED5564; font-weight: 400'>Check total books and reading progress</h5>", unsafe_allow_html=True)
    # if Library is Empty
    if not library:
        st.markdown(
            f"<div style='display: flex;justify-content: center;align-items: center;background: linear-gradient(135deg, red, green);padding: 20px 10px; margin: 30px 0px; border-radius: 5px;color: white;font-weight: 100;'>⊘ The library is currently empty. Add a book to get started.</div>", unsafe_allow_html=True)
    else:
        # Total Length
        total_books = len(library)
        # Read Book Length
        read_books = len([book for book in library if book["read"] == True])
        # Percentage
        percentage_read = (read_books / total_books) * \
            100 if total_books > 0 else 0

        display_statics = st.columns([1, 1, 1])
        with display_statics[0]:
            st.write(f"📚 :gray[Total books:]")
            st.title(f"{len(library)}")
        with display_statics[1]:
            st.write(f"📜 :gray[Books read:]")
            st.title(f"{read_books}")
        with display_statics[2]:
            st.write(f"📊 :gray[Percentage read:]")
            st.title(f"{percentage_read:.2f}%")

# CSS Properties if Required
st.markdown("""
    <style>
        input::placeholder {font-size: 14px !important; font-weight: 100 !important;}
    </style>
""", unsafe_allow_html=True)


# Footer
st.markdown("""<p style="color: #2f3038; text-align:center;">Made with ❤ by Zubair Ahmed</p>""",
            unsafe_allow_html=True)
