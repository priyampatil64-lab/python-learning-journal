# Day 6 - For Loops, Range, Enumerate & Comprehension Examples

# ---------- Basic for loop ----------
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# ---------- for loop with range() ----------
for i in range(5):
    print(f"i = {i}")             # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(f"i = {i}")             # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(f"i = {i}")             # 0, 2, 4, 6, 8 (step of 2)

# ---------- for loop with enumerate() ----------
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# enumerate with a custom starting index
for index, fruit in enumerate(fruits, start=1):
    print(f"Item {index}: {fruit}")

# ---------- Nested for loops ----------
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")

# ---------- List comprehension ----------
squares = [x ** 2 for x in range(1, 6)]
print(squares)                    # [1, 4, 9, 16, 25]

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)               # [2, 4, 6, 8, 10]

# list comprehension using enumerate
indexed_fruits = [f"{i}:{fruit}" for i, fruit in enumerate(fruits)]
print(indexed_fruits)

# ---------- Taking list input from the user ----------
# Example: user types "10 20 30 40" and we convert it to a list of integers
# raw_input = input("Enter numbers separated by space: ")
# numbers = [int(x) for x in raw_input.split()]
# print(numbers)

# Simulated version (without actual input, for demonstration)
raw_input_simulated = "10 20 30 40"
numbers = [int(x) for x in raw_input_simulated.split()]
print(numbers)                    # [10, 20, 30, 40]

# ---------- for vs while revision ----------
# for loop - use when the number of iterations is known
for i in range(3):
    print(f"For loop iteration {i}")

# while loop - use when it depends on a condition
count = 0
while count < 3:
    print(f"While loop iteration {count}")
    count += 1
