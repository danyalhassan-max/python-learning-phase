student_id=set()

while True:
    print("1.Add Student ID")
    print("2.View Student IDs")
    print("3.Remove Student ID")
    print("4.Count Student IDs")
    print("5.Exit")
    choice=input("Enter your choice: ")

    if choice=="5":
        print("Program Closed")
        break
    elif choice=="1":
        student_id.add(int(input("Enter Student ID: ")))
    elif choice=="2":
        if not student_id:
            print("No Student IDs Found")
        else:
            for sid in student_id:
                print(sid)
    elif choice=="3":
        if not student_id:
            print("No Student IDs Available")
        else:
            rid=int(input("Enter ID to remove: "))
            if rid in student_id:
                student_id.remove(rid)
                print("Student ID Removed")
            else:
                print("Student ID Not Found")
    elif choice=="4":
        print("Total Student IDs:",len(student_id))
