# Day 7 - Functions, Parameters & Local/Global Variables
Reference: Engineering in Kannada - Python Zero to Hero (Part 12)
- Part 12: "Functions, Parameters, Local and Global Variables"

## Topics covered
- Defining and calling functions
- Parameters and arguments
- Default parameter values
- Return values
- Local variables (scope inside a function)
- Global variables (scope outside a function)
- The `global` keyword

## Notes

### Defining and Calling Functions
A function is a reusable block of code that performs a specific task. It's defined once with `def` and can be called (run) as many times as needed, avoiding repeated code.

```
def greet():
    print("Hello!")

greet()   # calling the function
```

### Parameters and Arguments
Parameters are placeholders listed in a function's definition; arguments are the actual values passed in when calling the function.

```
def greet(name):      # 'name' is the parameter
    print(f"Hello, {name}!")

greet("Priyam")        # "Priyam" is the argument
```

### Default Parameter Values
A parameter can have a default value, used automatically if the caller doesn't provide one.

```
def greet(name="Guest"):
    print(f"Hello, {name}!")
```

### Return Values
`return` sends a value back to wherever the function was called from, so it can be stored or used further. A function without `return` implicitly returns `None`.

### Local Variables
A variable created **inside** a function only exists inside that function - this is called local scope. It cannot be accessed from outside the function, and it disappears once the function finishes running.

### Global Variables
A variable created **outside** any function, at the top level of the script, is a global variable - it can be read from anywhere, including inside functions.

### The `global` Keyword
By default, assigning to a variable inside a function creates a new **local** variable, even if a global variable with the same name exists. To modify the actual global variable from inside a function, you must explicitly declare it with the `global` keyword.

```
count = 0

def increment():
    global count
    count += 1
```

See `examples.py` for working code for each topic.
