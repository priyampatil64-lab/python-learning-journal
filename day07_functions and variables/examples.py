# Day 7 - Functions, Parameters & Local/Global Variables Examples

# ---------- Defining and calling a function ----------
def greet():
    print("Hello!")

greet()

# ---------- Function with a parameter ----------
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Priyam")
greet_person("Learner")

# ---------- Function with multiple parameters ----------
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(5, 3)

# ---------- Default parameter values ----------
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()            # uses default -> "Hello, Guest!"
greet_with_default("Priyam")    # overrides default -> "Hello, Priyam!"

# ---------- Return values ----------
def square(number):
    return number ** 2

result = square(5)
print(result)                   # 25

# using a returned value directly in another expression
total = square(2) + square(3)
print(total)                    # 4 + 9 = 13

# ---------- Local variables ----------
def local_scope_demo():
    message = "I only exist inside this function"   # local variable
    print(message)

local_scope_demo()
# print(message)   # this would raise a NameError - 'message' doesn't exist here

# ---------- Global variables ----------
app_name = "PyLearn"   # global variable

def show_app_name():
    print(f"App name: {app_name}")   # reading a global variable works fine

show_app_name()

# ---------- Modifying a global variable with the 'global' keyword ----------
count = 0

def increment_without_global():
    count = count + 1   # this creates a NEW local variable, doesn't touch the global one
    # NOTE: this line would actually raise an UnboundLocalError if uncommented,
    # because Python sees 'count' being assigned here and treats it as local
    # before it's read.

def increment_with_global():
    global count
    count += 1           # this correctly modifies the global 'count'

increment_with_global()
increment_with_global()
increment_with_global()
print(f"Final count: {count}")   # Final count: 3
