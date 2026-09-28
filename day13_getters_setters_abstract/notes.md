# Day 13 - Getters/Setters, Overloading & Overriding, Abstract Class
Reference: Engineering in Kannada - Python Zero to Hero (Part 18)
- Part 18: "Getters Setters, Overloading & Overriding, Abstract Class"

## Topics covered
- Getters and setters (including the `@property` decorator)
- Method overloading in Python
- Operator overloading with dunder methods
- Method overriding
- Abstract classes using the `abc` module
- Abstract methods

## Notes

### Getters and Setters
A **getter** reads the value of a private attribute and a **setter** updates it, usually with validation. Python's `@property` decorator lets you do this while still using clean attribute-style syntax (`obj.age` instead of `obj.get_age()`).

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):          # getter
        return self.__age

    @age.setter
    def age(self, value):   # setter with validation
        if value > 0:
            self.__age = value
```

### Overloading
Overloading means one name behaving differently based on the inputs.
- **Method overloading:** Python does *not* support true overloading by signature (if you define two methods with the same name, the last one wins). Instead, we use default arguments or `*args` to handle different numbers of inputs in one method.
- **Operator overloading:** special "dunder" methods like `__add__`, `__str__`, `__eq__` let objects of your own class work with operators such as `+` and `==`.

### Overriding
When a child class defines a method with the same name as one in its parent class, the child's version **overrides** the parent's. Calling the method on a child object runs the child's version.

### Abstract Class
An abstract class is a class that cannot be instantiated directly. It acts as a blueprint that forces child classes to implement certain methods. In Python, this is done with the `abc` module (`ABC` and `@abstractmethod`).

### Abstract Methods
An abstract method is declared in the abstract class with no real implementation. Every child class **must** override it, otherwise Python raises a `TypeError` when you try to create an object of that child class.

See `examples.py` for working code for each topic.
