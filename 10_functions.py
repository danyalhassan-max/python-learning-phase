# ==========================================
# Python Functions
# ==========================================

# ------------------------------------------
# 1. Basic Function
# ------------------------------------------

def my_function():
    print("Hello World")


my_function()
my_function()


# Why use functions?
# - Reusable code
# - Avoid repetition
# - Easier maintenance


# ------------------------------------------
# 2. Function with Return Value
# ------------------------------------------

def temp_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(temp_to_celsius(77))
print(temp_to_celsius(45))


# ------------------------------------------
# 3. Returning Data
# ------------------------------------------

def greetings():
    return "Hello"


message = greetings()
print(message)


# ------------------------------------------
# 4. Empty Function
# ------------------------------------------

def empty_function():
    pass


# ------------------------------------------
# 5. Parameters and Arguments
# ------------------------------------------

def print_name(first_name):
    print(first_name, "Hassan")


print_name("Danyal")
print_name("Izzle")


def greet(name):
    print("Hello", name)


greet("Email")


def full_name(first_name, last_name):
    print(first_name, last_name)


full_name("Izzle", "Hassan")


# ------------------------------------------
# 6. Default Parameter
# ------------------------------------------

def welcome(name="Guest"):
    print("Hello", name)


welcome("Danyal")
welcome()
welcome("Hassan")


# ------------------------------------------
# 7. Keyword & Positional Arguments
# ------------------------------------------

def animal_info(animal, name):
    print("I have a", animal)
    print("My", animal, "name is", name)


animal_info(animal="Dog", name="Buddy")
animal_info("Cat", "Mano")


def pet_info(animal, name, age):
    print("Animal:", animal)
    print("Name:", name)
    print("Age:", age)


pet_info("Dog", name="Max", age=5)


# ------------------------------------------
# 8. Passing Lists
# ------------------------------------------

def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)


fruits = ["Banana", "Apple", "Mango"]
print_fruits(fruits)


# ------------------------------------------
# 9. Passing Dictionary
# ------------------------------------------

def person_info(person):
    print("Name:", person["name"])
    print("Age:", person["age"])


person = {
    "name": "Emil",
    "age": 25
}

person_info(person)


# ------------------------------------------
# 10. Returning Values
# ------------------------------------------

def add(x, y):
    return x + y


print(add(5, 3))


def get_fruits():
    return ["Apple", "Mango", "Orange"]


fruit_list = get_fruits()
print(fruit_list[0])


def get_numbers():
    return 5, 8


x, y = get_numbers()
print(x)
print(y)


# ------------------------------------------
# 11. Positional-only Parameter
# ------------------------------------------

def positional_example(name, /):
    print("Hello", name)


positional_example("Emil")


# ------------------------------------------
# 12. Keyword-only Parameter
# ------------------------------------------

def keyword_example(*, name):
    print("Hello", name)


keyword_example(name="Danyal")


# ------------------------------------------
# 13. Combination of Positional & Keyword
# ------------------------------------------

def combine(a, b, /, *, c, d):
    return a + b + c + d


print(combine(6, 8, c=9, d=2))


# ------------------------------------------
# 14. *args
# ------------------------------------------

def favorite_colors(*colors):
    print("Favorite Color:", colors[1])


favorite_colors("Red", "Black", "White")


def show_colors(*colors):
    print(type(colors))
    print("Second Color:", colors[1])
    print("All Colors:", colors)


show_colors("Brown", "Black", "White")


def greet_many(greeting, *names):
    for name in names:
        print(greeting, name)


greet_many("AoA", "Hassan", "Danyal")


# ------------------------------------------
# 15. Practical Examples using *args
# ------------------------------------------

def sum_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(sum_numbers(12, 3, 5))


def subtract_numbers(*numbers):
    total = numbers[0]
    for number in numbers[1:]:
        total -= number
    return total


print(subtract_numbers(20, 2, 5))


def max_number(*numbers):
    if not numbers:
        return None

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


print(max_number(4, 3, 6, 2))


# ------------------------------------------
# 16. **kwargs
# ------------------------------------------

def student_info(**details):
    print("Name:", details["name"])
    print("Age:", details["age"])
    print(details)


student_info(name="Danyal", age=19)


def full_info(**data):
    print("First Name:", data["name"])
    print("Last Name:", data["surname"])


full_info(name="Danyal", surname="Hassan")


def display_student(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


display_student(
    name="Danyal",
    department="IT",
    gpa=3.2
)


# ==========================================
# Local and Global Scope
# ==========================================

# ------------------------------------------
# 17. Local Scope
# ------------------------------------------

def local_scope():
    x = 5
    print(x)


local_scope()


# Nested Function

def outer_function():
    x = 5

    def inner_function():
        print(x)

    inner_function()


outer_function()


# ------------------------------------------
# 18. Global Scope
# ------------------------------------------

x = 30


def show_global():
    print(x)


show_global()
print(x)


# Same Variable Name

y = 5


def local_variable():
    y = 3
    print(y)


local_variable()
print(y)


# Using global Keyword

def change_global():
    global x
    x = 9
    print(x)


change_global()
print(x)


x = 300


def modify_global():
    global x
    x = 200


modify_global()
print(x)


# ==========================================
# Recursion
# ==========================================

# Countdown

def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)


countdown(5)


# Factorial

def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


print(factorial(5))
