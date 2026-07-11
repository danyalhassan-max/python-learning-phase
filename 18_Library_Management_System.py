"""
==========================================================
          Library Management System Using OOP
==========================================================

Description:
A beginner-friendly Library Management System developed
using Object-Oriented Programming (OOP) in Python.

----------------------------------------------------------
Features
----------------------------------------------------------
1. Add Book
2. View Books
3. Search Book
4. Update Book Quantity
5. Remove Book
6. Exit

----------------------------------------------------------
Concepts Used
----------------------------------------------------------
- Class and Object
- Constructor (__init__)
- self Keyword
- Methods
- Lists
- Dictionaries
- CRUD Operations
- Loops
- Conditional Statements

----------------------------------------------------------
Author
----------------------------------------------------------
Danyal
"""


# ==========================================================
# Library Class
# ==========================================================

class Library:

    def __init__(self):
        self.books = []

    # Add a New Book
    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        book_name = input("Enter Book Name: ")
        quantity = int(input("Enter Book Quantity: "))

        book = {
            "id": book_id,
            "name": book_name,
            "quantity": quantity
        }

        self.books.append(book)

        print("Book Added Successfully")

    # View All Books
    def view_books(self):
        if len(self.books) == 0:
            print("No Books Available")
            return

        for book in self.books:
            print("ID:", book["id"])
            print("Name:", book["name"])
            print("Quantity:", book["quantity"])
            print("--------------------")

    # Search Book
    def search_book(self):
        if len(self.books) == 0:
            print("No Books Available")
            return

        found = False
        search_id = int(input("Enter Book ID: "))

        for book in self.books:
            if book["id"] == search_id:
                print("ID:", book["id"])
                print("Name:", book["name"])
                print("Quantity:", book["quantity"])

                found = True
                break

        if not found:
            print("Book Not Found")

    # Update Book Quantity
    def update_quantity(self):
        if len(self.books) == 0:
            print("No Books Available")
            return

        found = False
        search_id = int(input("Enter Book ID: "))

        for book in self.books:
            if book["id"] == search_id:
                new_quantity = int(input("Enter Updated Quantity: "))

                book["quantity"] = new_quantity

                print("Quantity Updated Successfully")

                found = True
                break

        if not found:
            print("Book Not Found")

    # Remove Book
    def remove_book(self):
        if len(self.books) == 0:
            print("No Books Available")
            return

        found = False
        remove_id = int(input("Enter Book ID: "))

        for book in self.books:
            if book["id"] == remove_id:
                self.books.remove(book)

                print("Book Removed Successfully")

                found = True
                break

        if not found:
            print("Book Not Found")


# ==========================================================
# Create Library Object
# ==========================================================

library = Library()


# ==========================================================
# Main Program
# ==========================================================

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Quantity")
    print("5. Remove Book")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.update_quantity()

    elif choice == "5":
        library.remove_book()

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")
