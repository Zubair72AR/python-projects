import json
import os


# Name of library
library_file = os.path.join(os.path.dirname(__file__), "library.txt")


def load_library():
    # Open File is Exist
    if os.path.exists(library_file):
        with open(library_file, "r") as file:
            return json.load(file)

    return []


def save_library(library):
    # Open File and Add Data
    with open(library_file, "w") as file:
        json.dump(library, file, indent=4)


def add_book(library):
    # Add New Book Data Step by Step
    # Add Title
    while True:
        title: str = input("Enter the book title: ")
        if title:
            break
        print(f"Title cannot be blank. Please enter the book title again.")
    # Add Author Name
    while True:
        author: str = input("Enter the author: ")
        if author:
            break
        print(f"Author cannot be blank. Please enter the author name again.")
    # Add Year of Publish
    while True:
        try:
            year: int = int(input("Enter the publication year: "))
            break
        except ValueError:
            print("⚠️ Please enter a valid year (e.g., 2025).")
    # Add Genre
    while True:
        genre: str = input("Enter the genre: ")
        if genre:
            break
        print(f"Genre cannot be blank. Please enter the genre again.")
    # Add Read or Unread
    read: str = input("Have you read this book? (yes/no): ").lower()
    # Convert True or False
    read: bool = True if read in ["yes", "y"] else False
    # Add Received Data into Dict
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read,
    }
    # Append and Call Save Function
    library.append(new_book)
    save_library(library)
    # Added Successfully info for User
    print(f"Book \"{title}\" added successfully.")


def remove_book(library):
    remove_file = input("Enter the title of the book to remove: ").lower()
    initial_length = len(library)
    library = [book for book in library if book["title"].lower() !=
               remove_file]
    if len(library) < initial_length:
        save_library(library)
        print(f'Book {remove_file} removed successfully.')
    else:
        print(f'Book {remove_file} not found in the library.')


def search_book(library):
    print("Search by: \n1. Title  \n2. Author")
    search_type = input("Enter your choice: ").lower()
    if search_type in ["1", "title"]:
        search_type = "title"
    elif search_type in ["2", "author"]:
        search_type = "author"
    else:
        print("Invalid choice.")
        return
    search_query = input(f"Enter the {search_type}: ").lower()
    result = [book for book in library if search_query in book[search_type].lower()]
    if result:
        print("Matching Books: ")
        for index, book in enumerate(result, start=1):
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {book['read']}")
    else:
        print(f"No books found for '{search_query}' in {search_type}.")


def display_book(library):
    if not library:
        print("No books in the library.")
        return
    print("\nLibrary Books:")
    for index, book in enumerate(library, start=1):
        print(
            f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {book['read']}")


def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * \
        100 if total_books > 0 else 0
    print(f"\nTotal books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%")


def main():
    library = load_library()
    print("Welcome to your Personal Library Manager!")
    menu = """
    1. Add a book  
    2. Remove a book  
    3. Search for a book  
    4. Display all books  
    5. Display statistics  
    6. Exit  
    """
    while True:
        print(menu)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_book(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
