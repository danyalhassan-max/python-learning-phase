"""
=========================================================
               PYTHON BASICS FOR BEGINNERS
=========================================================
Author : Danyal
Purpose: Learn the fundamentals of Python programming.
Topics:
1. Printing Output
2. Indentation
3. Comments
4. Multiple Statements
5. end Parameter
6. Variables
7. Type Casting
8. Data Types
9. Case Sensitivity
10. Multiple Assignment
11. Unpacking Collections
12. String Concatenation
13. Global & Local Variables
=========================================================
"""

print("Hello, World!")

if 5 > 2:
    print("Five is greater than two!")
    print("This statement is inside the if block.")

if 2 < 5:
    print("Two is less than five.")

# Multiple statements
print("Hello"); print("Danyal")

# end parameter
print("Hello", end=" ")
print("World")

# Variables
x = "Sal"
print(x)
x = 2
print(x)

# Type Casting
x = str(4)
y = int("4")
z = float(2)
print(x, y, z)

# Data types
a = 5
b = "Danyal"
print(type(a))
print(type(b))

# Case sensitivity
x = 4
X = "Jolly"
print(x)
print(X)

# Multiple assignment
x, y, z = "Apple", "Orange", "Banana"
print(x, y, z)

# One value to multiple variables
x = y = z = "Mango"
print(x, y, z)

# Unpacking
fruits = ("Apple", "Orange", "Banana")
x, y, z = fruits
print(x, y, z)

# Concatenation
x = "Python"
y = " is "
z = "Awesome"
print(x + y + z)
print(x, y, z)

# Global variable
message = "Python is Awesome"
def show_message():
    print(message)
show_message()

# Local variable
def local_example():
    language = "Python"
    print(language)
local_example()

# global keyword
status = "Good"
def change_status():
    global status
    status = "Excellent"
change_status()
print(status)
