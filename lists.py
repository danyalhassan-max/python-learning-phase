"""
Python Lists Basics
Author: Danyal

This file contains beginner-friendly examples of Python Lists.
"""

# ============================================
# 1. Creating Lists
# ============================================

fruit_list = ["apple", "orange", "mango", "banana", "grapes"]
print(fruit_list)

# Duplicate values are allowed
my_fruit_list = ["apple", "orange", "mango", "apple", "apple", "banana", "grapes"]
print(my_fruit_list)

# Length of list
print(len(my_fruit_list))

# Different data types
mixed_list = ["Danyal", 11, True]
print(mixed_list)
print(type(mixed_list))
print(type(my_fruit_list))

# List constructor
list2 = list(("Apple", "Orange"))
print(list2)

# ============================================
# 2. Accessing List Items
# ============================================

colors = ["red", "white", "blue", "black", "orange", "yellow", "silver"]

print(colors[2])
print(colors[2:4])
print(colors[-6:-2])
print(colors[-3])

# Check if item exists
fruits = ["apple", "orange", "grapes"]

if "apple" in fruits:
    print("Apple is in the fruit list.")

# ============================================
# 3. Changing List Items
# ============================================

colors[1] = "half white"
print(colors)

colors[2:4] = ["dark", "mango"]
print(colors)

colors[1:2] = ["white", "full white"]
print(colors)

colors.insert(2, "watermelon")
print(colors)

# ============================================
# 4. Adding Items
# ============================================

items = ["blue", "black", "orange"]

items.append("mango")
print(items)

items.insert(1, "dark")
print(items)

more_items = ["apple", "grapes", "banana"]

items.extend(more_items)
print(items)

# ============================================
# 5. Removing Items
# ============================================

color_list = ["red", "white", "blue", "black", "black", "orange", "yellow", "silver"]

color_list.remove("white")
print(color_list)

color_list.remove("black")
print(color_list)

color_list.pop(1)
color_list.pop()
print(color_list)

del color_list[0]
print(color_list)

# ============================================
# 6. Loop Through a List
# ============================================

loop_list = ["apple", "grapes", "orange"]

for item in loop_list:
    print(item)

for i in range(len(loop_list)):
    print(loop_list[i])

j = 0
while j < len(loop_list):
    print(loop_list[j])
    j += 1

[print(item) for item in loop_list]

# ============================================
# 7. Sorting Lists
# ============================================

numbers = [1, 2, 3, 4, 3, 11, 34, 67, 212, 2]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

def my_function(n):
    return abs(n - 50)

my_list = [1, 43, 6, 50, 7, 34, 2, 76, 43, 562]
my_list.sort(key=my_function)
print(my_list)

# ============================================
# 8. Copy Lists
# ============================================

original = ["apple", "banana", "cherry"]

copy1 = original.copy()
print(copy1)

copy2 = list(original)
print(copy2)

copy3 = original[:]
print(copy3)

# ============================================
# 9. Join Lists
# ============================================

list1 = ["a", "b"]
list2 = [1, 2, 4]

list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)

print(list1)

list2.extend(list1)
print(list2)
