"""
=========================================
Python Tuples
Author: Danyal
=========================================
""" 

# =========================================
# 1. Creating Tuples
# =========================================

# Tuple with different data types
fruits = ("apple", "banana", 12, False)
print(fruits)

# Check tuple data type
print(type(fruits))

# Tuple allows duplicate values
f1 = ("apple", "banana", "apple")
print(f1)

# Check tuple length
print(len(f1))

# Tuple with one item (comma is required)
one_item = ("apple",)
print(one_item)

# Create tuple using tuple() constructor
this_tuple = tuple((1, "abc"))
print(this_tuple)


# =========================================
# 2. Access Tuple Items
# =========================================

fruits = ("apple", "banana", "mango")

# Access by index
print(fruits[1])

# Access by range
print(fruits[1:3])

# Negative indexing
print(fruits[-1])

# Check if item exists
if "apple" in fruits:
    print("Apple exists in the tuple.")


# =========================================
# 3. Change Tuple Values
# (Tuples are immutable)
# =========================================

x = ("orange", "mango")

# Convert tuple into list
y = list(x)

# Modify list
y[1] = "banana"
y.append("apple")
y.remove("orange")

# Convert list back to tuple
x = tuple(y)

print(x)


# =========================================
# 4. Add Items to Tuple
# =========================================

colors = ("red", "black", "white")

# Create another tuple
new_color = ("silver",)

# Join tuples
colors += new_color

print(colors)


# =========================================
# 5. Join and Repeat Tuples
# =========================================

tuple1 = ("red", "black", "green")
tuple2 = ("banana", "orange")

# Join tuples
tuple3 = tuple1 + tuple2
print(tuple3)

# Repeat tuple
tuple4 = tuple1 * 2
print(tuple4)


# =========================================
# 6. Unpacking Tuples
# =========================================

colors = ("red", "black", "green")

first, *remaining = colors

print(first)
print(remaining)


# =========================================
# 7. Loop Through Tuple (While Loop)
# =========================================

color = ("red", "blue", "black")

i = 0

while i < len(color):
    print(color[i])
    i += 1


# =========================================
# 8. Loop Through Tuple (For Loop)
# =========================================

color1 = ("red", "blue", "black")

for i in range(len(color1)):
    print(color1[i])

# Direct loop
for item in color1:
    print(item)
