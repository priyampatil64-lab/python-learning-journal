# Day 6 - For Loops, Range, Enumerate & Comprehension
Reference: Engineering in Kannada - Python Zero to Hero
- Part 10: "For Loops | Range, Enumerate | Nested Loops"
- Part 11: "Comprehension | List Input | Loops Revision"

## Topics covered
- For loops - syntax and iterating over sequences
- range() function - generating number sequences
- enumerate() function - looping with index + value together
- Nested for loops
- List comprehension (revisited in more depth)
- Taking list input from the user
- Loops revision - for vs while, when to use each

## Notes

### For Loops
A `for` loop iterates over a sequence (list, string, tuple, range, etc.), running the code block once for each item in that sequence - unlike a `while` loop, which runs based on a condition rather than a fixed sequence.

```
for item in sequence:
    # code block
```

### range() Function
`range()` generates a sequence of numbers, commonly used to loop a specific number of times.
- `range(5)` → 0, 1, 2, 3, 4
- `range(1, 6)` → 1, 2, 3, 4, 5
- `range(0, 10, 2)` → 0, 2, 4, 6, 8 (with a step value)

### enumerate() Function
`enumerate()` lets you loop through a sequence while also getting the index of each item, without manually maintaining a counter variable.

```
for index, value in enumerate(my_list):
    ...
```

### Nested For Loops
Same idea as nested while loops - a `for` loop placed inside another `for` loop, where the inner loop completes fully for every single iteration of the outer loop. Common for grids, tables, and patterns.

### List Comprehension
A concise, one-line way to build a list: `[expression for item in iterable if condition]`. It replaces the need to write a full `for` loop with `.append()` calls just to build a list.

### Taking List Input from the User
User input is read as a string with `input()`, so numeric list input usually needs to be split and converted, e.g. using `.split()` and `int()` inside a loop or comprehension.

### For vs While - When to Use Each
- Use a `for` loop when you know the sequence or number of iterations in advance (looping through a list, a fixed range, etc.)
- Use a `while` loop when the number of iterations depends on a condition that isn't known ahead of time (like waiting for specific user input, or running until a value changes).

See `examples.py` for working code for each topic.
