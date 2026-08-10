# Day 2 - Strings & Operators Examples

# ---------- Accessing string characters ----------
text = "Python"
print(text[0])       # 'P' - first character
print(text[5])       # 'n' - last character
print(text[-1])      # 'n' - last character using negative index
print(text[-6])      # 'P' - first character using negative index

# ---------- String slicing ----------
message = "Learning Python"
print(message[0:8])      # "Learning"
print(message[9:])       # "Python" (from index 9 to end)
print(message[:8])       # "Learning" (from start to index 8)
print(message[::-1])     # reverses the whole string
print(message[0:8:2])    # every 2nd character from index 0 to 8

# ---------- Escape sequences ----------
print("Line1\nLine2")          # newline
print("Name:\tPriyam")         # tab
print("She said \"Python is fun\"")  # double quotes inside string
print('It\'s a great day')     # single quote inside string
print("C:\\Users\\Priyam")     # backslash

# ---------- Assignment operators ----------
num = 10
num += 5   # num = num + 5
print(num)   # 15
num -= 3
print(num)   # 12
num *= 2
print(num)   # 24
num //= 5
print(num)   # 4

# ---------- Comparison operators ----------
a, b = 10, 20
print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a >= b)   # False

# ---------- Logical operators ----------
x, y = True, False
print(x and y)   # False
print(x or y)    # True
print(not x)     # False

# ---------- Membership operators ----------
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)       # True
print("grape" not in fruits)   # True

# ---------- Bitwise operators ----------
p, q = 6, 3          # binary: 110, 011
print(p & q)   # AND -> 2
print(p | q)   # OR  -> 7
print(p ^ q)   # XOR -> 5
print(~p)      # NOT -> -7
print(p << 1)  # left shift -> 12
print(p >> 1)  # right shift -> 3

# ---------- Arithmetic operators ----------
m, n = 15, 4
print(m + n)   # 19
print(m - n)   # 11
print(m * n)   # 60
print(m / n)   # 3.75
print(m // n)  # 3
print(m % n)   # 3
print(m ** n)  # 50625
