"""
==========================================================
                Library Management System
==========================================================

Description:
A beginner-friendly console application developed using
Python Lists and Dictionaries. This project demonstrates
CRUD (Create, Read, Update, Delete) operations for
managing a collection of books.

----------------------------------------------------------
Features
----------------------------------------------------------
1. Add Book
2. View Books
3. Search Book
4. Update Book Quantity
5. Remove Book
6. Exit Program

----------------------------------------------------------
Concepts Used
----------------------------------------------------------
• Python Lists
• Python Dictionaries
• Lists of Dictionaries
• CRUD Operations
• while Loop
• for Loop
• if / elif / else
• append()
• remove()
• len()
• break
• User Input
• Dictionary Operations

----------------------------------------------------------
Author
----------------------------------------------------------
Danyal
"""

lab_mang = []

while True:

    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Quantity")
    print("5. Remove Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ==========================================
    # Exit Program
    # ==========================================

    if choice == "6":
        print("Program Closed Successfully.")
        break

    # ==========================================
    # Add Book
    # ==========================================

    elif choice == "1":

        add_id = int(input("Enter Book ID: "))
        add_title = input("Enter Book Title: ")
        add_quan = int(input("Enter Quantity: "))

        book = {
            "id": add_id,
            "title": add_title,
            "quantity": add_quan
        }

        lab_mang.append(book)

        print("Book Added Successfully.")

    # ==========================================
    # View Books
    # ==========================================

    elif choice == "2":

        if len(lab_mang) == 0:
            print("No Books Available.")

        else:

            print("\n========== Book Records ==========\n")

            for x in lab_mang:

                print("Book ID   :", x["id"])
                print("Title     :", x["title"])
                print("Quantity  :", x["quantity"])
                print("--------------------------------")

    # ==========================================
    # Search Book
    # ==========================================

    elif choice == "3":

        found = False

        if len(lab_mang) == 0:
            print("No Books Available.")

        else:

            search_id = int(input("Enter Book ID: "))

            for x in lab_mang:

                if x["id"] == search_id:

                    print("\nBook Found\n")

                    print("Book ID   :", x["id"])
                    print("Title     :", x["title"])
                    print("Quantity  :", x["quantity"])

                    found = True
                    break

        if found == False:
            print("Book Not Found.")

    # ==========================================
    # Update Book Quantity
    # ==========================================

    elif choice == "4":

        found = False

        if len(lab_mang) == 0:
            print("No Books Available.")

        else:

            enter_id = int(input("Enter Book ID: "))

            for x in lab_mang:

                if x["id"] == enter_id:

                    update_quan = int(input("Enter New Quantity: "))

                    x["quantity"] = update_quan

                    print("Quantity Updated Successfully.")

                    found = True
                    break

        if found == False:
            print("Book Not Found.")

    # ==========================================
    # Remove Book
    # ==========================================

    elif choice == "5":

        found = False

        if len(lab_mang) == 0:
            print("No Books Available.")

        else:

            ent_id = int(input("Enter Book ID: "))

            for x in lab_mang:

                if x["id"] == ent_id:

                    lab_mang.remove(x)

                    print("Book Removed Successfully.")

                    found = True
                    break

        if found == False:
            print("Book Not Found.")

    # ==========================================
    # Invalid Choice
    # ==========================================

    else:
        print("Invalid Choice. Please Try Again.")
