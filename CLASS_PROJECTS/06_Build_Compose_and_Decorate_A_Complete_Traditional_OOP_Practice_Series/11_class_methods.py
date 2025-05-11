"""
11. Class Methods
Assignment:
Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
"""


class Book:  # Class
    total_books = 0  # Class Variable to track total books

    def __init__(self, title: str):  # Constructor
        self.title = title  # Save title
        Book.increment_book_count()  # Call class method when book is added

    @classmethod
    def increment_book_count(cls):  # Class Method
        cls.total_books += 1  # Increase book count

    def show_title(self):  # Instance Method
        print(f"Book Title: {self.title}")


book1 = Book("Python Basics")  # Add 1st Book
book1.show_title()
print(f"Total Books: {Book.total_books}")  # Check Book Count

book2 = Book("Advanced Python")  # Add 2nd Book
book2.show_title()

print(f"Total Books: {Book.total_books}")  # Check Book Count
