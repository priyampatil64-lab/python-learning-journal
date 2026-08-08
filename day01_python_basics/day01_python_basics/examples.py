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
a, b, c = 10, 20, 30
print(a, b, c)

# Same value to multiple variables
x = y = z = 100
print(x, y, z)

# ---------- Variable Reassignment ----------
score = 50
print("Before:", score)
score = 75
print("After:", score)

# ---------- Type Conversion ----------
num_str = "123"
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
# print("Hello,", user_name)

# ---------- String Manipulation ----------
message = "Learning Python is fun"
print(message.upper())          # LEARNING PYTHON IS FUN
print(message.lower())          # learning python is fun
print(message.replace("fun", "awesome"))
print(message.split())          # splits into list of words
print(message[0:8])             # slicing: "Learning"
print(len(message))             # length of string
print(message + " every day")   # concatenation
