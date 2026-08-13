# Day 4 - Dictionaries & If-Else Examples

# ---------- Creating a dictionary ----------
student = {
    "name": "Priyam",
    "age": 20,
    "course": "Python"
}
print(student)

# ---------- Accessing values ----------
print(student["name"])          # 'Priyam' - direct access
print(student.get("age"))       # 20 - safe access
print(student.get("grade"))     # None - key doesn't exist, no error

# ---------- Adding & updating ----------
student["grade"] = "A"          # adds a new key-value pair
print(student)

student["age"] = 21             # updates an existing value
print(student)

# ---------- Removing items ----------
del student["grade"]
print(student)

popped_value = student.pop("course")
print(popped_value, student)     # returns 'Python' and removes it

# ---------- Dictionary methods ----------
print(student.keys())            # dict_keys(['name', 'age'])
print(student.values())          # dict_values(['Priyam', 21])
print(student.items())           # dict_items([('name', 'Priyam'), ('age', 21)])

# ---------- Merging with update() ----------
extra_info = {"course": "Python", "level": "Beginner"}
student.update(extra_info)
print(student)

# ---------- Looping through a dictionary ----------
for key, value in student.items():
    print(f"{key}: {value}")

# ---------- If, elif, else ----------
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 50:
    print("Grade: B")
else:
    print("Grade: F")

# ---------- Comparison operators ----------
a = 10
b = 20
print(a == b)   # False
print(a != b)   # True
print(a < b)    # True

# ---------- Logical operators ----------
age = 22
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print("No class today")

# ---------- Nested if statements ----------
username = "priyam"
password = "python123"

if username == "priyam":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("User not found")
