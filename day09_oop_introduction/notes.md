# Day 9 - Object Oriented Programming Introduction
Reference: Engineering in Kannada - Python Zero to Hero (Part 15)
- Part 15: "Object Oriented Programming Introduction"

## Topics covered
- What is Object Oriented Programming (OOP)?
- Classes and objects
- The `__init__` constructor method
- Instance attributes
- Instance methods
- The `self` keyword
- Creating multiple objects from the same class

## Notes

### What is Object Oriented Programming?
OOP is a programming style built around **objects** - real-world "things" that bundle together data (attributes) and behavior (methods) into a single unit. Instead of writing separate variables and functions everywhere, related data and logic are grouped together, making code more organized and reusable.

### Classes and Objects
- A **class** is a blueprint/template that defines what attributes and methods its objects will have.
- An **object** (also called an instance) is an actual thing created from that class, with real values filled in.

```
class Dog:
    pass

my_dog = Dog()   # my_dog is an object (instance) of the Dog class
```

### The `__init__` Constructor
`__init__` is a special method that runs automatically whenever a new object is created from a class. It's used to set up the object's initial attributes.

```
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Instance Attributes
Attributes are variables that belong to a specific object, storing data unique to that object (e.g. each `Dog` object has its own `name` and `age`).

### The `self` Keyword
`self` refers to the specific object the method is being called on. It's always the first parameter of instance methods (including `__init__`), and it's how an object accesses its own attributes and other methods.

### Instance Methods
Instance methods are functions defined inside a class that operate on a specific object's data, always taking `self` as their first parameter.

```
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")
```

### Creating Multiple Objects
Multiple objects can be created from the same class, each with its own independent set of attribute values, even though they share the same structure and methods defined by the class.

See `examples.py` for working code for each topic.
