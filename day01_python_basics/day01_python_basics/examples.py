# Day 1 - Python Basics Examples

# ---------- Comments ----------
# This is a single-line comment
"""
This is a multi-line comment / docstring
often used to describe what a script does.
"""

# ---------- Variables & Data Types ----------
name = "Priyam"        # str
age = 21                # int
height = 5.6             # float
is_student = True        # bool

print(type(name), type(age), type(height), type(is_student))

# ---------- Assigning multiple variables at once ----------
x, y, z = 10, 20, 30
print(x, y, z)

# Same value to multiple variables
a = b = c = 100
print(a, b, c)

# ---------- Variable Reassignment ----------
score = 50
print("Before:", score)
score = 75
print("After:", score)

# ---------- Type Conversion ----------
num_str = "10"
num_int = int(num_str)        # str -> int
num_float = float(num_int)    # int -> float
back_to_str = str(num_float)  # float -> str
print(num_int, num_float, back_to_str)

# ---------- Arithmetic Operators ----------
p, q = 10, 3
print("Addition:", p + q)
print("Subtraction:", p - q)
print("Multiplication:", p * q)
print("Division:", p / q)
print("Floor Division:", p // q)
print("Modulus:", p % q)
print("Exponent:", p ** q)

# ---------- Input / Output ----------
# Uncomment to try interactively:
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# print("Hello, " + user_name + "! You are " + str(user_age) + " years old.")
# print(f"Hello, {user_name}! You are {user_age} years old.")   # f-string version

# ---------- String Manipulation ----------
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name   # concatenation
print(full_name)

greeting = "Hello! " * 3                    # repetition
print(greeting)

message = "  Hello, World!  "
print(message.strip())                      # removes leading/trailing spaces
print(message.upper())                      # HELLO, WORLD!
print(message.lower())                      # hello, world!
print(message.replace("World", "Python"))   # Hello, Python!
