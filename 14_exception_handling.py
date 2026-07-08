"""
Python Exception Handling Examples
Author: Danyal
Description:
This script demonstrates different types of exception handling in Python,
including:
- NameError
- ZeroDivisionError
- FileNotFoundError
- ValueError
- try-except-else-finally
- Raising custom exceptions
"""

# ==========================================================
# Example 1: NameError
# ==========================================================

try:
    print(x)  # Variable 'x' is not defined.
except NameError:
    print("Error: Variable 'x' is not defined.")

# ==========================================================
# Example 2: ZeroDivisionError
# ==========================================================

try:
    num = 10
    result = num / 0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# ==========================================================
# Example 3: File Handling
# ==========================================================

try:
    with open(r"D:\std.csv", "r") as file:
        data = file.read()
        print("File found successfully.")
except FileNotFoundError:
    print("Error: File not found.")

# ==========================================================
# Example 4: Converting Strings to Integers
# ==========================================================

data = ["25", "30", "NA", "40"]

for value in data:
    try:
        number = int(value)
        print(number)
    except ValueError:
        print(f"Cannot convert '{value}' into an integer.")

# ==========================================================
# Example 5: ValueError
# ==========================================================

try:
    number = int("Danyal")
except ValueError:
    print("Error: Cannot convert text into an integer.")

# ==========================================================
# Example 6: ZeroDivisionError (Specific Exception)
# ==========================================================

try:
    num = 10
    result = num / 0
    print(result)
except ZeroDivisionError:
    print("Error: You divided by zero.")

# ==========================================================
# Example 7: Multiple Except Blocks
# ==========================================================

try:
    print(x)
except NameError:
    print("Error: Variable is not defined.")
except Exception:
    print("An unexpected error occurred.")
finally:
    print("Execution of try-except block is complete.")

# ==========================================================
# Example 8: File Write Operation
# ==========================================================

try:
    file = open("demofile.txt", "r")

    try:
        file.write("Lorem Ipsum")
    except Exception:
        print("Error: Unable to write to the file.")
    finally:
        file.close()

except FileNotFoundError:
    print("Error: File could not be opened.")

# ==========================================================
# Example 9: try - except - else - finally
# ==========================================================

try:
    num = 10
    result = 100 / num

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program finished.")

# ==========================================================
# Example 10: Raising Custom Exceptions
# ==========================================================

x = -1

if x < 0:
    raise Exception("Sorry, numbers below zero are not allowed.")
