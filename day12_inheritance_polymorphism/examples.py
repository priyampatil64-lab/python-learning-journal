# Day 12 - Pillars of OOP: Inheritance & Polymorphism Examples

# ---------- Basic inheritance ----------
class Animal:                    # parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):                # child class - inherits from Animal
    pass


dog = Dog("Buddy")
dog.speak()                       # Buddy makes a sound. (inherited, unchanged)

# ---------- Overriding a parent method ----------
class Cat(Animal):
    def speak(self):              # overrides Animal's speak() method
        print(f"{self.name} says Meow!")


cat = Cat("Whiskers")
cat.speak()                       # Whiskers says Meow! (overridden behavior)

# ---------- Using super() to reuse the parent's __init__ ----------
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # reuse Animal's __init__ to set 'name'
        self.breed = breed         # add Dog's own extra attribute

    def speak(self):
        print(f"{self.name} the {self.breed} says Woof!")


dog = Dog("Buddy", "Golden Retriever")
dog.speak()                        # Buddy the Golden Retriever says Woof!

# ---------- Polymorphism: same method name, different behavior ----------
class Bird(Animal):
    def speak(self):
        print(f"{self.name} says Tweet!")


animals = [Dog("Buddy", "Labrador"), Cat("Whiskers"), Bird("Tweety")]

for animal in animals:
    animal.speak()          # same method call, different output per object type

# ---------- Polymorphism with a shared parent method call ----------
class Shape:
    def area(self):
        return 0   # default, meant to be overridden


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)


shapes = [Square(4), Circle(3)]

for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area()}")
