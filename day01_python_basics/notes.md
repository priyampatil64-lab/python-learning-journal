# Day 1 - Python Basics
Reference: Engineering in Kannada - Python Zero to Hero (Part 1, 2 & 3)

## Topics covered
- What is Python & why it's popular
- Variables and Data Types
- Type Conversion
- Arithmetic Operators
- Assigning values to multiple variables
- Variable reassignment
- Input / Output
- Comments
- String manipulation

## Notes

### What is Python?
Python is a high-level, interpreted programming language known for its simplicity and readability. It's used for web development (Django, Flask), data science and machine learning (Pandas, TensorFlow), automation/scripting, and general software development.

### Why is Python Popular?
- Easy to learn - simple syntax close to natural language
- Massive community support - lots of tutorials, resources, libraries
- Cross-platform - works on Windows, macOS, Linux
- Versatile - libraries for almost everything

### 1. Variables in Python
Variables store data values. Created when you assign a value to them - no need to declare a type (Python is dynamically typed).
```python
x = 5          # integer
y = "Hello"    # string
```
**Naming rules:** letters, numbers, underscores allowed; must start with a letter or underscore; case-sensitive (`Name` != `name`).

### 2. Data Types
- `int` - integers (1, -3, 100)
- `float` - floating-point numbers (3.14, -0.001)
- `str` - strings ("Hello")
- `bool` - True or False

Use `type()` to check a variable's type.

### 3. Type Conversion
Convert between types using `int()`, `float()`, `str()`, etc.
```python
x = "10"
y = int(x)      # string -> int
z = float(y)    # int -> float
```

### 4. Arithmetic Operators
`+` `-` `*` `/` `//` (floor division) `%` (modulus) `**` (exponent)

### 5. Assigning Values to Multiple Variables
```python
x, y, z = 10, 20, 30      # different values
x = y = z = 100           # same value to all
```

### 6. Variable Reassignment
A variable's value can be changed anytime by assigning it a new value.

### 7. Input / Output
`input()` takes user input (always returns a string - convert with `int()`/`float()` if needed). `print()` displays output. f-strings (`f"Hello, {name}"`) are the readable way to format output.

### 8. Comments
- Single-line: `# comment`
- Multi-line: triple quotes `"""..."""` or `'''...'''`

### 9. String Manipulation
- **Concatenation:** `first_name + " " + last_name`
- **Repetition:** `"Hello! " * 3`
- **Methods:** `upper()`, `lower()`, `strip()`, `replace(old, new)`

See `examples.py` for working code for each topic.
