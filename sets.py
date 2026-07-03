"""
=========================================
Python Sets
Author: Danyal
=========================================
"""

# =========================================
# 1. Creating Sets
# =========================================

# Create a simple set
my_set = {"Danyal", "Hassan", "Student"}
print(my_set)

# Sets do not allow duplicate values
duplicate_set = {"Apple", "Banana", "Apple", "Orange"}
print(duplicate_set)

# True and 1 are considered the same value
# False and 0 are considered the same value
mixed_set = {"Danyal", "Hassan", "Student", 1, True, 2, False, 0}
print(mixed_set)

# Check length
print(len(mixed_set))

# Check data type
print(type(mixed_set))

# Create a set using the set() constructor
constructor_set = set(("Banana", "Mango"))
print(constructor_set)


# =========================================
# 2. Access Set Items
# =========================================

my_set = {"Danyal", "Hassan", "Student"}

# Check if an item exists
print("Danyal" in my_set)

# Loop through a set
for item in my_set:
    print(item)


# =========================================
# 3. Add Items
# =========================================

my_set = {"Danyal", "Hassan", "Student"}
new_set = {"Department", "Year"}

# Add a single item
my_set.add("Roll No")
print(my_set)

# Add multiple items
my_set.update(new_set)
print(my_set)


# =========================================
# 4. Remove Items
# =========================================

# Remove a specific item
my_set.remove("Student")
print(my_set)

# Remove without error if item doesn't exist
my_set.discard("ABC")
print(my_set)

# Remove a random item
removed_item = my_set.pop()
print("Removed Item:", removed_item)
print(my_set)

# Copy a set
copy_set = my_set.copy()
print(copy_set)

# Clear all items
copy_set.clear()
print(copy_set)


# =========================================
# 5. Join Sets
# =========================================

s1 = {"a", "b", "c"}
s2 = {1, 2, 4}
s3 = {"apple", "orange"}
s4 = {"red", "blue"}

# Join using |
s5 = s1 | s2
print(s5)

# Join using union()
s6 = s1.union(s2, s3, s4)
print(s6)

# Join multiple sets
s7 = s1 | s5 | s6
print(s7)

# Join a set with a list
x = {"a", "b"}
y = ["c", "d"]

z = x.union(y)
print(z)


# =========================================
# 6. Set Operations
# =========================================

fruits = {"apple", "banana", "orange"}
colors = {"red", "blue", "orange"}

# Intersection
common_items = fruits.intersection(colors)
print(common_items)

# Intersection using &
common_items2 = fruits & colors
print(common_items2)

# Update the original set with common values
temp = fruits.copy()
temp.intersection_update(colors)
print(temp)

# Difference
difference_items = fruits.difference(colors)
print(difference_items)

# Symmetric Difference
symmetric_items = fruits.symmetric_difference(colors)
print(symmetric_items)


# =========================================
# 7. Frozen Set
# =========================================

# Immutable Set
frozen = frozenset(("a", "b"))

print(frozen)
print(type(frozen))