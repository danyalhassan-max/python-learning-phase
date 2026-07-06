"""
=========================================================
            Library Management System
=========================================================

Description:
A beginner-friendly console application developed using
Python Lists and Functions.

This project demonstrates CRUD operations:

• Create
• Read
• Update
• Delete

---------------------------------------------------------
Features
---------------------------------------------------------

1. Add Book
2. View Books
3. Search Book
4. Update Book Quantity
5. Remove Book
6. Exit

---------------------------------------------------------
Concepts Used
---------------------------------------------------------

• Python Lists
• Python Dictionaries
• Functions
• CRUD Operations
• Loops
• Conditional Statements
• User Input
• Input Validation

---------------------------------------------------------
Author
---------------------------------------------------------

Danyal
"""

# ==========================================
# Global Book Collection
# ==========================================

library = []


# ==========================================
# Add Book
# ==========================================

def add_book():
    """Add a new book to the library."""

    try:
        book_id = int(input("Enter Book ID: "))

        # Check duplicate ID
        for book in library:
            if book["id"] == book_id:
                print("A book with this ID already exists.")
                return

        title = input("Enter Book Title: ")
        quantity = int(input("Enter Quantity: "))

        book = {
            "id": book_id,
            "title": title,
            "quantity": quantity
        }

        library.append(book)
        print("Book added successfully.")

    except ValueError:
        print("Please enter valid numeric values.")


# ==========================================
# View Books
# ==========================================

def view_books():
    """Display all books."""

    if not library:
        print("No books available.")
        return

    print("\n========== Book Records ==========\n")

    for book in library:
        print(f"Book ID  : {book['id']}")
        print(f"Title    : {book['title']}")
        print(f"Quantity : {book['quantity']}")
        print("-" * 35)


# ==========================================
# Search Book
# ==========================================

def search_book():
    """Search a book using its ID."""

    if not library:
        print("No books available.")
        return

    try:
        book_id = int(input("Enter Book ID: "))

        for book in library:
            if book["id"] == book_id:
                print("\nBook Found\n")
                print(f"Book ID  : {book['id']}")
                print(f"Title    : {book['title']}")
                print(f"Quantity : {book['quantity']}")
                return

        print("Book not found.")

    except ValueError:
        print("Invalid ID.")


# ==========================================
# Update Quantity
# ==========================================

def update_book_quantity():
    """Update the quantity of a book."""

    if not library:
        print("No books available.")
        return

    try:
        book_id = int(input("Enter Book ID: "))

        for book in library:
            if book["id"] == book_id:
                quantity = int(input("Enter New Quantity: "))
                book["quantity"] = quantity
                print("Book quantity updated successfully.")
                return

        print("Book not found.")

    except ValueError:
        print("Invalid input.")


# ==========================================
# Remove Book
# ==========================================

def remove_book():
    """Remove a book using its ID."""

    if not library:
        print("No books available.")
        return

    try:
        book_id = int(input("Enter Book ID: "))

        for book in library:
            if book["id"] == book_id:
                library.remove(book)
                print("Book removed successfully.")
                return

        print("Book not found.")

    except ValueError:
        print("Invalid ID.")


# ==========================================
# Main Menu
# ==========================================

def main():

    while True:

        print("\n========== Library Management System ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Quantity")
        print("5. Remove Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            update_book_quantity()

        elif choice == "5":
            remove_book()

        elif choice == "6":
            print("Program closed successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


# ==========================================
# Program Entry Point
# ==========================================

if __name__ == "__main__":
    main()
