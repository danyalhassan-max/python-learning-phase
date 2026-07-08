"""
=========================================
        Python File Handling Examples
=========================================
"""

import os

# ---------------------------------------
# 1. Read a Text File
# ---------------------------------------

try:
    with open("pyy.txt", "r") as f:
        print("Reading pyy.txt")
        print(f.read())
except FileNotFoundError:
    print("pyy.txt not found.")

# ---------------------------------------
# 2. Read a CSV File
# ---------------------------------------

try:
    with open("StudentsPerformance.csv", "r") as f:
        print("\nReading CSV File")
        print(f.read())
except FileNotFoundError:
    print("StudentsPerformance.csv not found.")

# ---------------------------------------
# 3. Append Data to a File
# ---------------------------------------

with open("pyy.txt", "a") as f:
    f.write("\nHello, New Content Added!")

print("\nAfter Appending:")
with open("pyy.txt", "r") as f:
    print(f.read())

# ---------------------------------------
# 4. Write Mode (Creates or Overwrites)
# ---------------------------------------

with open("writ.txt", "w") as f:
    f.write("This file was created using write mode.")

print("\nwrit.txt Created Successfully!")

# ---------------------------------------
# 5. Write and Read (w+)
# ---------------------------------------

with open("wrt.csv", "w+") as f:
    f.write("male")
    f.seek(0)
    print("\nUsing w+ Mode")
    print(f.read())

# ---------------------------------------
# 6. Append and Read (a+)
# ---------------------------------------

with open("wrt.csv", "a+") as f:
    f.write("\nappend")
    f.seek(0)
    print("\nUsing a+ Mode")
    print(f.read())

# ---------------------------------------
# 7. Overwrite File
# ---------------------------------------

with open("wrt.csv", "w") as f:
    f.write("Oops, File Overwritten!")

print("\nAfter Overwriting:")
with open("wrt.csv", "r") as f:
    print(f.read())

# ---------------------------------------
# 8. Delete a File
# ---------------------------------------

if os.path.exists("writ.txt"):
    os.remove("writ.txt")
    print("\nwrit.txt deleted successfully.")
else:
    print("\nFile does not exist.")

# ---------------------------------------
# 9. Read Lines
# ---------------------------------------

print("\nReadlines Example:")
with open("wrt.csv", "r") as f:
    print(f.readlines())
