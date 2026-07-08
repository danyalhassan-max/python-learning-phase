"""
=========================================
        Python Dictionaries
=========================================

Topics Covered:
1. Creating Dictionaries
2. Accessing Dictionary Items
3. Dictionary Methods
4. Adding & Updating Items
5. Removing Items
6. Looping Through Dictionaries
7. Copying Dictionaries
8. Nested Dictionaries
"""

# =========================================
# Creating a Dictionary
# =========================================

car = {
    "brand": "Suzuki",
    "name": "Alto",
    "model": 2019,
    "color": ["Red", "White"]
}

print(car)
print(len(car))          # Dictionary length
print(type(car))         # Dictionary type

# =========================================
# Accessing Dictionary Items
# =========================================

print(car["brand"])          # Access using key
print(car.get("name"))       # Access using get()

print(car.keys())            # Display all keys

# =========================================
# Adding New Items
# =========================================

car["price"] = "2100000 PKR"

print(car)

# =========================================
# Dictionary Values & Items
# =========================================

print(car.values())          # Display all values

car["model"] = 2021          # Update value

print(car.values())

print(car.items())           # Display key-value pairs

# =========================================
# Checking if Key Exists
# =========================================

if "model" in car:
    print("Model key exists.")

# =========================================
# Update Dictionary
# =========================================

car.update({"year": 2019})
car.update({"model": 2020})

print(car)

# =========================================
# Remove Dictionary Items
# =========================================

car.pop("year")              # Remove specific key

print(car)

# Note:
# del car["price"]      -> Remove specific key
# car.clear()           -> Remove all items

# =========================================
# Loop Through Dictionary
# =========================================

print("\nDictionary Keys")
for key in car:
    print(key)

print("\nDictionary Values")
for key in car:
    print(car[key])

print("\nUsing values()")
for value in car.values():
    print(value)

print("\nUsing keys()")
for key in car.keys():
    print(key)

print("\nUsing items()")
for key, value in car.items():
    print(key, ":", value)

# =========================================
# Copy Dictionary
# =========================================

copy_one = car.copy()

copy_two = dict(car)

print(copy_one)
print(copy_two)

# =========================================
# Nested Dictionary
# =========================================

person = {

    "info": {
        "name": "Danyal Hassan",
        "address": "Pakistan",
        "age": 21
    },

    "student": {
        "university": "UOS",
        "department": "IT",
        "room": 166
    }

}

print(person)

# Access Nested Dictionary

print(person["info"]["name"])

# =========================================
# Dictionary Inside Dictionary
# =========================================

data = {
    "car": car,
    "person": person
}

print(data)
