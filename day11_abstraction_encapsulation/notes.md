# Day 11 - Pillars of OOP: Abstraction & Encapsulation
Reference: Engineering in Kannada - Python Zero to Hero (Part 17A)
- Part 17A: "Pillars of OOP | Abstraction & Encapsulation"

## Topics covered
- The four pillars of OOP (overview)
- Abstraction - hiding complexity, exposing only what's needed
- Encapsulation - bundling data and methods, restricting direct access
- Public, protected, and private attributes in Python
- Getter and setter methods

## Notes

### The Four Pillars of OOP
Object Oriented Programming is generally built on four core principles: **Abstraction**, **Encapsulation**, **Inheritance**, and **Polymorphism**. This session focuses on the first two.

### Abstraction
Abstraction means hiding the complex internal implementation details of something and only exposing the necessary parts to the user. In practice, when you call a method, you don't need to know *how* it works internally - just *what* it does.

Example: when you call `.append()` on a list, you don't need to know how Python resizes the underlying array in memory - you just know it adds an item.

### Encapsulation
Encapsulation means bundling data (attributes) and the methods that operate on that data together inside a class, while restricting direct outside access to some of that data - protecting it from being changed in unintended ways.

### Public, Protected & Private Attributes
Python doesn't have strict access modifiers like some other languages, but follows naming conventions to signal intent:
- `self.name` - **public**, accessible from anywhere
- `self._name` - **protected** (single underscore), a convention meaning "internal use, but not strictly enforced" - accessible, but signals it shouldn't be touched directly from outside
- `self.__name` - **private** (double underscore), triggers Python's name-mangling, making it much harder (though not impossible) to access from outside the class

### Getter and Setter Methods
Since private/protected attributes shouldn't be accessed directly from outside a class, **getter** methods are used to read their value, and **setter** methods are used to update their value safely - often adding validation logic in the setter before allowing a change.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def get_balance(self):         # getter
        return self.__balance

    def set_balance(self, amount): # setter with validation
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")
```

See `examples.py` for working code for each topic.
