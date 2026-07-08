"""
Simple Calculator using Exception Handling

Author: Danyal

Description:
This program performs:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

It demonstrates the use of:
- try
- except
- else
- finally
- raise
"""

# ==========================================================
# Calculator Program
# ==========================================================

while True:

    # Display Menu
    print("\n========== Simple Calculator ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # ======================================================
    # Exit Program
    # ======================================================

    if choice == "5":
        print("Program Closed.")
        break

    # ======================================================
    # Addition
    # ======================================================

    elif choice == "1":

        try:
            first_number = int(input("Enter First Number: "))
            second_number = int(input("Enter Second Number: "))

            result = first_number + second_number

        except ValueError:
            print("Invalid input! Please enter numbers only.")

        else:
            print("Result:", result)

        finally:
            print("Addition Completed.")

    # ======================================================
    # Subtraction
    # ======================================================

    elif choice == "2":

        try:
            first_number = int(input("Enter First Number: "))
            second_number = int(input("Enter Second Number: "))

            result = first_number - second_number

        except ValueError:
            print("Invalid input! Please enter numbers only.")

        else:
            print("Result:", result)

        finally:
            print("Subtraction Completed.")

    # ======================================================
    # Multiplication
    # ======================================================

    elif choice == "3":

        try:
            first_number = int(input("Enter First Number: "))
            second_number = int(input("Enter Second Number: "))

            result = first_number * second_number

        except ValueError:
            print("Invalid input! Please enter numbers only.")

        else:
            print("Result:", result)

        finally:
            print("Multiplication Completed.")

    # ======================================================
    # Division
    # ======================================================

    elif choice == "4":

        try:
            first_number = int(input("Enter First Number: "))
            second_number = int(input("Enter Second Number: "))

            # Raise a custom exception if a negative number is entered
            if first_number < 0 or second_number < 0:
                raise Exception("Negative numbers are not allowed.")

            result = first_number / second_number

        except ValueError:
            print("Invalid input! Please enter numbers only.")

        except ZeroDivisionError:
            print("Cannot divide by zero.")

        except Exception as error:
            print(error)

        else:
            print("Result:", result)

        finally:
            print("Division Completed.")

    # ======================================================
    # Invalid Choice
    # ======================================================

    else:
        print("Invalid choice! Please select a number between 1 and 5.")
