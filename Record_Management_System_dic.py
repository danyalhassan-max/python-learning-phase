"""
=========================================
    Student Record Management System
=========================================

Features:
1. Add Student
2. View Students
3. Search Student
4. Update Marks
5. Remove Student
6. Total Students
7. Exit

Concepts Used:
- Lists
- Dictionaries
- Loops
- Conditional Statements
- CRUD Operations
"""

student_dic = []

while True:

    print("\n========== Student Record Management ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Remove Student")
    print("6. Total Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # =========================================
    # Exit Program
    # =========================================

    if choice == "7":
        print("Program Closed Successfully.")
        break

    # =========================================
    # Add Student
    # =========================================

    elif choice == "1":

        add_id = int(input("Enter Student ID: "))
        add_name = input("Enter Student Name: ")
        add_marks = int(input("Enter Student Marks: "))

        student = {
            "id": add_id,
            "name": add_name,
            "marks": add_marks
        }

        student_dic.append(student)

        print("Student Added Successfully.")

    # =========================================
    # View Students
    # =========================================

    elif choice == "2":

        if len(student_dic) == 0:
            print("No Student Records Available.")

        else:

            print("\nStudent Records\n")

            for x in student_dic:

                print("Student ID    :", x["id"])
                print("Student Name  :", x["name"])
                print("Student Marks :", x["marks"])
                print("--------------------------------")

    # =========================================
    # Search Student
    # =========================================

    elif choice == "3":

        found = False

        search_id = int(input("Enter Student ID: "))

        for x in student_dic:

            if x["id"] == search_id:

                print("\nStudent Found\n")

                print("Student ID    :", x["id"])
                print("Student Name  :", x["name"])
                print("Student Marks :", x["marks"])

                found = True
                break

        if found == False:
            print("Student Not Found.")

    # =========================================
    # Update Student Marks
    # =========================================

    elif choice == "4":

        found = False

        id_marks = int(input("Enter Student ID: "))

        for x in student_dic:

            if x["id"] == id_marks:

                update_marks = int(input("Enter Updated Marks: "))

                x["marks"] = update_marks

                found = True

                print("Marks Updated Successfully.")

                break

        if found == False:
            print("Student Not Found.")

    # =========================================
    # Remove Student
    # =========================================

    elif choice == "5":

        found = False

        enter_id = int(input("Enter Student ID: "))

        for x in student_dic:

            if x["id"] == enter_id:

                student_dic.remove(x)

                found = True

                print("Student Removed Successfully.")

                break

        if found == False:
            print("Student Not Found.")

    # =========================================
    # Total Students
    # =========================================

    elif choice == "6":

        if len(student_dic) == 0:
            print("No Student Records Available.")

        else:
            print("Total Students :", len(student_dic))

    # =========================================
    # Invalid Choice
    # =========================================

    else:
        print("Invalid Choice. Please try again.")
