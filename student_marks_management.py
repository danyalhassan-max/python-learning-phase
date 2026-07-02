mark_List = []

while True:

    print("\n===================================")
    print(" Student Marks Management System")
    print("===================================")
    print("1. Add Marks")
    print("2. View Marks")
    print("3. Highest Marks")
    print("4. Lowest Marks")
    print("5. Average Marks")
    print("6. Total Students")
    print("7. Remove Marks")
    print("8. Exit")

    number = input("Press the number: ")

    if number == "8":
        print("Program Closed")
        break

    elif number == "1":
        add_marks = input("Please Enter your Marks: ")
        mark_List.append(int(add_marks))
        print("Marks Added Successfully!")

    elif number == "2":
        if len(mark_List) == 0:
            print("No Marks Available!")
        else:
            print("\nStudent Marks")
            for marks in mark_List:
                print(marks)

    elif number == "3":
        if len(mark_List) == 0:
            print("No Marks Available!")
        else:
            print("Highest Marks:", max(mark_List))

    elif number == "4":
        if len(mark_List) == 0:
            print("No Marks Available!")
        else:
            print("Lowest Marks:", min(mark_List))

    elif number == "5":
        if len(mark_List) == 0:
            print("No Marks Available!")
        else:
            print("Average Marks:", sum(mark_List)/len(mark_List))

    elif number == "6":
        print("Total Students:", len(mark_List))

    elif number == "7":
        if len(mark_List) == 0:
            print("Marks Are Not Available!")
        else:
            remove_List = int(input("Enter the marks you want to remove: "))
            if remove_List in mark_List:
                mark_List.remove(remove_List)
                print("Marks Removed Successfully!")
            else:
                print("Marks Not Found!")

    else:
        print("Invalid Choice! Please Try Again.")
