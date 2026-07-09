"""
==========================================================
                Modules & Packages
==========================================================

Description:
This file demonstrates how to use Python built-in modules
and user-defined modules. It covers different import
methods and common Python libraries.

----------------------------------------------------------
Topics Covered
----------------------------------------------------------
1. import module
2. import module as alias
3. from module import function
4. from module import *
5. User-Defined Module
6. math Module
7. random Module
8. string Module
9. datetime Module
10. os Module
11. pathlib Module

----------------------------------------------------------
Author
----------------------------------------------------------
Danyal
"""

# ==========================================================
# User Defined Module
# ==========================================================

import mymodule

mymodule.greetings("Danyal")

# ==========================================================
# Import Module
# ==========================================================

import math

number = float(input("\nEnter Number: "))
print("Square Root:", math.sqrt(number))

# ==========================================================
# Import Module as Alias
# ==========================================================

import math as m

number = float(input("\nEnter Another Number: "))
print("Square Root:", m.sqrt(number))

# ==========================================================
# From Import
# ==========================================================

from math import sqrt

print("\nSquare Root of 25:", sqrt(25))

# ==========================================================
# From Import *
# ==========================================================

from math import *

print("Square Root of 4:", sqrt(4))
print("Factorial of 5:", factorial(5))
print("Value of PI:", pi)

# ==========================================================
# Random Module
# ==========================================================

import random

print("\nRandom Number:", random.randint(1, 10))

students = ["Ali", "Danyal", "Hassan", "Izzle"]

winner = random.choice(students)

print("Random Student:", winner)

# ==========================================================
# String Module
# ==========================================================

import string

length = int(input("\nEnter Password Length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for _ in range(length))

print("Generated Password:", password)

# ==========================================================
# Datetime Module
# ==========================================================

from datetime import datetime

now = datetime.now()

print("\nCurrent Date & Time:", now)

# ==========================================================
# OS Module
# ==========================================================

import os

folder = "myfolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("\nFolder Created")
else:
    print("\nFolder Already Exists")

if os.path.exists(folder):
    os.rmdir(folder)
    print("Folder Deleted Successfully")

name = input("\nEnter File or Folder Name: ")

if os.path.exists(name):
    print("Exists")
else:
    print("Does Not Exist")

# ==========================================================
# Pathlib Module
# ==========================================================

from pathlib import Path

filename = Path(input("\nEnter File Name: "))

if filename.exists():
    print("File Exists")
else:
    print("File Does Not Exist")
