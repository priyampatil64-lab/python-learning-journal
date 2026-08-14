# Day 5 - While Loops, Break & Continue, Nested Loops Examples

# ---------- Basic while loop ----------
count = 1
while count <= 5:
    print(count)
    count += 1        # without this line, the loop would run forever

# ---------- While loop with user-like condition ----------
number = 10
while number > 0:
    print(f"Countdown: {number}")
    number -= 2

# ---------- break statement ----------
# Stop the loop as soon as we find the number 5
numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num == 5:
        print("Found 5! Stopping the loop.")
        break
    print(num)

# ---------- continue statement ----------
# Skip printing even numbers, only print odd ones
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(f"Odd number: {num}")

# ---------- break inside a while loop ----------
i = 0
while True:            # intentionally infinite - break is what stops it
    print(f"i = {i}")
    i += 1
    if i >= 5:
        break

# ---------- Nested loops: multiplication table ----------
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")        # separator after each outer loop iteration

# ---------- Nested loops: pattern printing ----------
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# ---------- Nested loop with break (only breaks the inner loop) ----------
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break        # only stops the inner loop, outer loop continues
        print(f"Outer {i}, Inner {j}")
