# Day 10 - Constructors and the `self` Keyword
Reference: Engineering in Kannada - Python Zero to Hero
Video: https://www.youtube.com/watch?v=at9RaJC3Jsg

## Topics covered
- The `__init__()` constructor in depth
- Using `self` in class methods
- Creating multiple objects with different attributes
- Optional (default) parameters in constructors

## Notes

### The `__init__()` Constructor
The `__init__()` method is a special method that initializes an object when it's created - it runs automatically the moment a new instance of a class is made. Its purpose is to set the initial state of the object by defining its attributes.

```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
```

### Using `self` in Class Methods
`self` refers to the specific instance of the class, allowing a method to access that object's own attributes and other methods. It's automatically passed as the first argument to every instance method. While `self` is just a naming convention (technically any name would work), sticking with `self` keeps code readable and consistent with everyone else's Python code.

### Creating Multiple Objects with Different Attributes
Passing different values to `__init__()` when creating each object means every object can hold its own unique set of attribute values, even though they all come from the same class blueprint.

### Optional (Default) Parameters in Constructors
A constructor parameter can have a default value, used automatically when the caller doesn't provide one - handy for attributes that are often the same across objects but occasionally need to be overridden.

```python
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author
```

See `examples.py` for working code for each topic, plus the homework problems (Movie class, Employee class) solved at the bottom.
