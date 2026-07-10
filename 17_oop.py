"""
=========================================
Python Object-Oriented Programming (OOP)
Part 1: Classes, Objects, Constructors,
Methods, Properties & Playlist
=========================================
"""

# ==================================================
# 1. Class & Object
# ==================================================

class MyClass:
    x = 5


class AnotherClass:
    r = 3
    g = 8


obj1 = MyClass()
print(obj1.x)

obj2 = AnotherClass()
print(obj2.r)
print(obj2.g)

del obj1


# ==================================================
# 2. Empty Class
# ==================================================

class EmptyPerson:
    pass


# ==================================================
# 3. Constructor (__init__)
# ==================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Danyal", 20)

print(person.name)
print(person.age)


# ==================================================
# 4. Multiple Attributes
# ==================================================

class FullName:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


user = FullName("Danyal", "Hassan")

print(user.first_name)
print(user.last_name)


# ==================================================
# 5. Default Parameter
# ==================================================

class PersonWithDefaultAge:
    def __init__(self, name, age=25):
        self.name = name
        self.age = age


person1 = PersonWithDefaultAge("Danyal")
person2 = PersonWithDefaultAge("Hassan", 30)

print(person1.name, person1.age)
print(person2.name, person2.age)


# ==================================================
# 6. Multiple Properties
# ==================================================

class StudentInfo:
    def __init__(self, name, age, city, country, education):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
        self.education = education


student = StudentInfo(
    "Danyal",
    24,
    "Sargodha",
    "Pakistan",
    "BS IT"
)

print(
    student.name,
    student.age,
    student.city,
    student.country,
    student.education
)


# ==================================================
# 7. Class Method Example
# ==================================================

class PersonMethods:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old.")


person = PersonMethods("Danyal", 25)
person.display()


# ==================================================
# 8. Car Class
# ==================================================

class Car:
    def __init__(self, name, company, model):
        self.name = name
        self.company = company
        self.model = model

    def display_car(self):
        print(f"{self.company} {self.name} ({self.model})")


car = Car("Alto", "Suzuki", "2020")
car.display_car()


# ==================================================
# 9. Calling One Method from Another
# ==================================================

class Greeting:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f"Hello, {self.name}"

    def welcome(self):
        message = self.greetings()
        print(f"{message}! Welcome.")


user = Greeting("Danyal Hassan")
user.welcome()


# ==================================================
# 10. Class Properties
# ==================================================

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Danyal", 12)

print(student.name)
print(student.age)


# Modify Property
student.age = 13
print(student.age)


# Add New Property
student.education = "Bachelor"
print(student.education)


# Delete Property
del student.name

# Checking before accessing
if hasattr(student, "name"):
    print(student.name)
else:
    print("The 'name' property has been deleted.")


# ==================================================
# 11. Calculator (Class Methods)
# ==================================================

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print(calc.add(5, 3))
print(calc.multiply(5, 2))


# ==================================================
# 12. Playlist Project
# ==================================================

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")
        else:
            print(f"{song} not found in playlist.")

    def show_songs(self):
        print(f"\nPlaylist: {self.name}")

        if not self.songs:
            print("No songs available.")
            return

        for song in self.songs:
            print(f"- {song}")


my_playlist = Playlist("Favorites")

my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.add_song("Hotel California")

my_playlist.show_songs()

my_playlist.remove_song("Hotel California")

my_playlist.show_songs()

"""
=========================================
Python Object-Oriented Programming (OOP)
Part 2: Inheritance & Polymorphism
=========================================
"""

# ==================================================
# 1. Basic Inheritance
# ==================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")


class Student(Person):
    pass


student = Student("Hassan", 23)
student.print_info()


# ==================================================
# 2. Inheritance using super()
# ==================================================

class PersonWithFullName:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(f"{self.first_name} {self.last_name}")


class StudentWithSuper(PersonWithFullName):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


student = StudentWithSuper("Danyal", "Hassan")
student.print_name()


# ==================================================
# 3. Child Class Adding New Method
# ==================================================

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


dog = Dog("Tommy")

dog.eat()
dog.bark()


# ==================================================
# 4. Child Class with Additional Attribute
# ==================================================

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print(f"Brand: {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_car(self):
        print(f"{self.brand} {self.model}")


car = Car("Toyota", "Corolla")

car.display_brand()
car.display_car()


# ==================================================
# 5. Method Overriding
# ==================================================

class Bird:
    def sound(self):
        print("Bird makes a sound.")


class Parrot(Bird):
    def sound(self):
        print("Parrot says: Hello!")


bird = Bird()
parrot = Parrot()

bird.sound()
parrot.sound()


# ==================================================
# 6. Polymorphism
# ==================================================

class CarMovement:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        print(f"{self.name}: Driving 🚗")


class Boat:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        print(f"{self.name}: Sailing 🚢")


class Plane:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        print(f"{self.name}: Flying ✈️")


car = CarMovement("Toyota", 2025)
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

for vehicle in (car, boat, plane):
    print(f"{vehicle.name} ({vehicle.model})")
    vehicle.move()


# ==================================================
# 7. Another Polymorphism Example
# ==================================================

class Shape:
    def draw(self):
        print("Drawing Shape")


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")


shapes = [Shape(), Circle(), Rectangle()]

for shape in shapes:
    shape.draw()


# ==================================================
# 8. Multi-Level Inheritance
# ==================================================

class GrandParent:
    def show_grandparent(self):
        print("Grandparent Class")


class Parent(GrandParent):
    def show_parent(self):
        print("Parent Class")


class Child(Parent):
    def show_child(self):
        print("Child Class")


child = Child()

child.show_grandparent()
child.show_parent()
child.show_child()


# ==================================================
# 9. Using super() with Extra Attributes
# ==================================================

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee: {self.name}")


class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def details(self):
        print(f"{self.name} manages the {self.department} department.")


manager = Manager("Danyal", "IT")

manager.show()
manager.details()

"""
=========================================
Python Object-Oriented Programming (OOP)
Part 3: Encapsulation, Special Methods,
Class Variables, Static Methods &
Class Methods
=========================================
"""

# ==================================================
# 1. Private Variables (Encapsulation)
# ==================================================

class PersonPrivate:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private variable

    def get_age(self):
        return self.__age


person = PersonPrivate("Danyal", 22)

print(person.name)
print(person.get_age())


# ==================================================
# 2. Protected Variables
# ==================================================

class PersonProtected:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Protected variable


person = PersonProtected("Danyal", 28)

print(person.name)
print(person._age)


# ==================================================
# 3. Public Variables
# ==================================================

class PersonPublic:
    def __init__(self):
        self.first_name = "Danyal"
        self.last_name = "Hassan"


person = PersonPublic()

print(person.first_name)
print(person.last_name)


# ==================================================
# 4. Method Overriding
# ==================================================

class Animal:
    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def sound(self):
        print("Dog is barking.")


dog = Dog()
dog.sound()


# ==================================================
# 5. __str__() Special Method
# ==================================================

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Danyal")

print(student)


# ==================================================
# 6. Class Variables
# ==================================================

class UniversityStudent:
    university = "University of Sargodha"

    def __init__(self, name):
        self.name = name


student1 = UniversityStudent("Danyal")
student2 = UniversityStudent("Hassan")

print(student1.university)
print(student2.university)

print(student1.name)
print(student2.name)


# ==================================================
# 7. Static Methods
# ==================================================

class Math:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Math.add(6, 2))
print(Math.multiply(5, 4))


# ==================================================
# 8. Class Methods
# ==================================================

class School:
    university = "University of Sargodha"

    @classmethod
    def show_university(cls):
        print(cls.university)


School.show_university()


# ==================================================
# 9. Class Variable Example
# ==================================================

class Employee:
    company = "OpenAI"

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name    : {self.name}")
        print(f"Company : {Employee.company}")


emp1 = Employee("Ali")
emp2 = Employee("Ahmed")

emp1.display()
print()

emp2.display()


# ==================================================
# 10. Static Method Example
# ==================================================

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


print(Temperature.celsius_to_fahrenheit(30))


# ==================================================
# 11. Class Method Example
# ==================================================

class Laptop:
    brand = "Dell"

    @classmethod
    def change_brand(cls, new_brand):
        cls.brand = new_brand

    @classmethod
    def show_brand(cls):
        print(f"Brand: {cls.brand}")


Laptop.show_brand()

Laptop.change_brand("HP")

Laptop.show_brand()


# ==================================================
# 12. Summary Example
# ==================================================

class BankAccount:
    bank_name = "ABC Bank"          # Class Variable

    def __init__(self, owner, balance):
        self.owner = owner          # Public Variable
        self.__balance = balance    # Private Variable

    def get_balance(self):
        return self.__balance

    @staticmethod
    def bank_rules():
        print("Minimum balance should be maintained.")

    @classmethod
    def show_bank(cls):
        print(f"Bank: {cls.bank_name}")

    def __str__(self):
        return f"Account Holder: {self.owner}"


account = BankAccount("Danyal", 5000)

print(account)
print(account.get_balance())

BankAccount.bank_rules()
BankAccount.show_bank()
