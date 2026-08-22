# Day 8 - Lambda Functions, Recursion, *args/**kwargs Examples

# ---------- Lambda functions ----------
square = lambda x: x ** 2
print(square(5))                     # 25

add = lambda a, b: a + b
print(add(3, 4))                     # 7

# lambda used with sorted()
students = [("Priyam", 85), ("Asha", 92), ("Ravi", 78)]
sorted_by_score = sorted(students, key=lambda student: student[1], reverse=True)
print(sorted_by_score)

# lambda used with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)                       # [2, 4, 6, 8, 10]

# lambda used with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)                  # [2, 4]

# ---------- Recursion ----------
def factorial(n):
    if n == 0 or n == 1:      # base case - stops the recursion
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))           # 120

def fibonacci(n):
    if n <= 1:                # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # recursive case

fib_sequence = [fibonacci(i) for i in range(8)]
print(fib_sequence)           # [0, 1, 1, 2, 3, 5, 8, 13]

# ---------- *args ----------
def add_all(*args):
    print(f"Received: {args}")   # args is a tuple
    return sum(args)

print(add_all(1, 2, 3))          # 6
print(add_all(10, 20, 30, 40))   # 100

# ---------- **kwargs ----------
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Priyam", age=20, course="Python")

# ---------- Combining *args and **kwargs ----------
def full_demo(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

full_demo(1, 2, 3, name="Priyam", active=True)

# ---------- HackerRank-style practice problem 1: Sum of digits (recursion) ----------
def sum_of_digits(n):
    if n == 0:                 # base case
        return 0
    return (n % 10) + sum_of_digits(n // 10)   # recursive case

print(sum_of_digits(12345))    # 1+2+3+4+5 = 15

# ---------- HackerRank-style practice problem 2: Filter and transform names ----------
names = ["priyam", "ASHA", "Ravi", "meena"]
formatted_names = list(map(lambda name: name.capitalize(), names))
print(formatted_names)         # ['Priyam', 'Asha', 'Ravi', 'Meena']
