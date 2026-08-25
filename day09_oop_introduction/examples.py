# Day 9 - Object Oriented Programming Introduction Examples

# ---------- A basic class and object ----------
class Dog:
    pass

my_dog = Dog()
print(type(my_dog))          # <class '__main__.Dog'>

# ---------- Class with __init__ constructor and attributes ----------
class Dog:
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age        # instance attribute

my_dog = Dog("Buddy", 3)
print(my_dog.name)            # Buddy
print(my_dog.age)             # 3

# ---------- Class with instance methods ----------
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

my_dog = Dog("Buddy", 3)
my_dog.bark()                 # Buddy says Woof!
my_dog.birthday()             # Buddy is now 4 years old.

# ---------- Creating multiple objects from the same class ----------
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
dog3 = Dog("Bella", 2)

for dog in [dog1, dog2, dog3]:
    dog.bark()

# each object keeps its own independent data
print(dog1.name, dog1.age)    # Buddy 3
print(dog2.name, dog2.age)    # Max 5
print(dog3.name, dog3.age)    # Bella 2

# ---------- A more real-world style example: Student class ----------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 50:
            return "B"
        else:
            return "F"

    def show_details(self):
        print(f"{self.name} scored {self.marks} marks - Grade: {self.get_grade()}")

students = [
    Student("Priyam", 88),
    Student("Asha", 95),
    Student("Ravi", 45)
]

for student in students:
    student.show_details()
