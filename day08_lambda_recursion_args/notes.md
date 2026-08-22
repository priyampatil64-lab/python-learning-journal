# Day 8 - Lambda Functions, Recursion, *args/**kwargs & HackerRank Practice
Reference: Engineering in Kannada - Python Zero to Hero
- Part 13: "Lambda Functions, Recursion, args and kwargs"
- Part 14A: "HackerRank Problem Solving - 1 | Certificate"

## Topics covered
- Lambda functions (anonymous functions)
- Recursion - functions that call themselves
- Base case and recursive case
- *args - variable number of positional arguments
- **kwargs - variable number of keyword arguments
- Applying these concepts by solving practice problems on HackerRank

## Notes

### Lambda Functions
A lambda function is a small, anonymous (unnamed) function defined in a single line using the `lambda` keyword, typically used for short operations where writing a full `def` function would be overkill.

```
square = lambda x: x ** 2
```

Commonly used with functions like `map()`, `filter()`, and `sorted()` where a quick, throwaway function is needed.

### Recursion
Recursion is when a function calls **itself** to solve a smaller version of the same problem, continuing until it reaches a stopping point.

- **Base case:** the condition that stops the recursion (without this, the function would call itself forever and crash with a `RecursionError`)
- **Recursive case:** the part where the function calls itself with a smaller/simpler input, moving closer to the base case each time

### *args - Variable Positional Arguments
`*args` lets a function accept **any number of positional arguments**, collecting them into a tuple inside the function.

```
def add_all(*args):
    return sum(args)

add_all(1, 2, 3, 4)   # works with any number of arguments
```

### **kwargs - Variable Keyword Arguments
`**kwargs` lets a function accept **any number of keyword arguments**, collecting them into a dictionary inside the function.

```
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Priyam", age=20)
```

### HackerRank Practice
Applied the above concepts (and earlier fundamentals) by solving beginner problems on HackerRank's Python track, which also awards a certificate on completion. This is a good habit alongside LeetCode - HackerRank problems tend to be more syntax/fundamentals-focused, while LeetCode leans more toward interview-style DSA problems.

See `examples.py` for working code for each concept, plus a couple of HackerRank-style practice problems solved using them.
