# Day 12 - Pillars of OOP: Inheritance & Polymorphism
Reference: Engineering in Kannada - Python Zero to Hero (Part 17B)
- Part 17B: "Pillars of OOP | Inheritance & Polymorphism"

## Topics covered
- Inheritance - creating a new class from an existing class
- Parent (base) class and child (derived) class
- Overriding parent methods in a child class
- Using `super()` to call the parent class's methods
- Polymorphism - same method name, different behavior
- Method overriding as a form of polymorphism

## Notes

### Inheritance
Inheritance lets a new class (the **child** / derived class) reuse the attributes and methods of an existing class (the **parent** / base class), instead of rewriting everything from scratch. The child class automatically gets everything the parent has, and can also add its own new attributes/methods.

```python
class Animal:              # parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):          # child class, inherits from Animal
    pass
```

### Overriding Parent Methods
A child class can **override** (redefine) a method it inherited from the parent, giving it different behavior specific to the child class - while keeping everything else from the parent unchanged.

### Using `super()`
`super()` lets a child class call the parent class's version of a method (like `__init__` or any other method) - useful when you want to reuse the parent's logic and then add extra behavior on top, instead of rewriting the parent's code entirely.

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # reuse Animal's __init__ to set 'name'
        self.breed = breed        # add Dog's own attribute
```

### Polymorphism
Polymorphism means "many forms" - the same method name behaves differently depending on which object it's called on. This makes code more flexible and generic, since you can call the same method name across different classes without needing to know each object's exact type.

### Method Overriding as Polymorphism
The most common form of polymorphism seen here: multiple child classes override the same parent method (like `speak()`) each in their own way, so calling `.speak()` on any of them produces different output automatically, based on which object it actually is.

See `examples.py` for working code for each topic.
