# Day 13 - Getters/Setters, Overloading & Overriding, Abstract Class Examples

from abc import ABC, abstractmethod

# ---------- Getters and setters with @property ----------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age          # private attribute

    @property
    def age(self):                # getter
        return self.__age

    @age.setter
    def age(self, value):         # setter with validation
        if value > 0:
            self.__age = value
        else:
            print("Age must be positive.")


p = Person("Priyam", 20)
print(p.age)          # 20 (uses the getter)
p.age = 21            # uses the setter
print(p.age)          # 21
p.age = -5            # rejected by validation
print(p.age)          # still 21

# ---------- Method "overloading" using default arguments ----------
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()
print(calc.add(5))          # 5
print(calc.add(5, 3))       # 8
print(calc.add(5, 3, 2))    # 10

# ---------- Method "overloading" using *args ----------
class Adder:
    def add(self, *args):
        return sum(args)


adder = Adder()
print(adder.add(1, 2))            # 3
print(adder.add(1, 2, 3, 4, 5))   # 15

# ---------- Operator overloading with dunder methods ----------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):     # makes the + operator work on Points
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):      # makes == work on Points
        return self.x == other.x and self.y == other.y

    def __str__(self):            # controls what print() shows
        return f"({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)                    # (4, 6)
print(p1 == Point(1, 2))          # True

# ---------- Method overriding ----------
class Animal:
    def speak(self):
        print("Some generic sound")


class Dog(Animal):
    def speak(self):              # overrides Animal.speak
        print("Woof!")


Animal().speak()                  # Some generic sound
Dog().speak()                     # Woof!

# ---------- Abstract class and abstract methods ----------
class Shape(ABC):
    @abstractmethod
    def area(self):               # must be implemented by child classes
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)


shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area()}")

# An abstract class cannot be instantiated directly
try:
    s = Shape()
except TypeError as e:
    print("Error:", e)

# A child that forgets to implement the abstract method also fails
class BadShape(Shape):
    pass

try:
    b = BadShape()
except TypeError as e:
    print("Error:", e)
