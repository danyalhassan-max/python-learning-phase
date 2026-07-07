import os

FILE_NAME = "student.txt"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        pass


while True:
    print("\n====== Student Management System ======")
    print("1. Add Student Record")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Total Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ---------------- Add Student ----------------
    if choice == "1":
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        student_marks = input("Enter Student Marks: ")

        with open(FILE_NAME, "a") as f:
            f.write(f"{student_id},{student_name},{student_marks}\n")

        print("Student Added Successfully!")

    # ---------------- View Students ----------------
    elif choice == "2":

        with open(FILE_NAME, "r") as f:
            records = f.readlines()

        if not records:
            print("No student records found.")

        else:
            print("\nStudent Records")
            print("-" * 35)

            for line in records:
                student = line.strip().split(",")

                print(f"ID    : {student[0]}")
                print(f"Name  : {student[1]}")
                print(f"Marks : {student[2]}")
                print("-" * 35)

    # ---------------- Search Student ----------------
    elif choice == "3":

        search_id = input("Enter Student ID: ")
        found = False

        with open(FILE_NAME, "r") as f:

            for line in f:
                student = line.strip().split(",")

                if student[0] == search_id:
                    print("\nStudent Found")
                    print("ID   :", student[0])
                    print("Name :", student[1])
                    print("Marks:", student[2])

                    found = True
                    break

        if not found:
            print("Student Not Found.")

    # ---------------- Remove Student ----------------
    elif choice == "4":

        remove_id = input("Enter Student ID to Remove: ")

        students = []
        found = False

        with open(FILE_NAME, "r") as f:

            for line in f:
                student = line.strip().split(",")

                if student[0] != remove_id:
                    students.append(line)
                else:
                    found = True

        with open(FILE_NAME, "w") as f:
            f.writelines(students)

        if found:
            print("Student Removed Successfully!")
        else:
            print("Student Not Found.")

    # ---------------- Total Students ----------------
    elif choice == "5":

        with open(FILE_NAME, "r") as f:
            records = f.readlines()

        print("Total Students:", len(records))

    # ---------------- Exit ----------------
    elif choice == "6":

        print("Program Closed.")
        break

    else:
        print("Invalid Choice! Please select 1-6.")
