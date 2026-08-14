# Day 5 - While Loops, Break & Continue, Nested Loops
Reference: Engineering in Kannada - Python Zero to Hero
- Part 9: "While Loops | Break and Continue | Nested Loops"

## Topics covered
- While loops - syntax & how they differ from for loops
- Infinite loops and how to avoid them
- break statement
- continue statement
- Nested loops (a loop inside another loop)

## Notes

### While Loops
A `while` loop repeats a block of code **as long as a condition stays true**. Unlike a `for` loop (which iterates over a known sequence, like a list or a range), a `while` loop is used when you don't know in advance how many times you need to repeat something - it just keeps going until the condition becomes false.

```
while condition:
    # code block
```

### Infinite Loops
If the condition in a `while` loop never becomes false, it runs forever - this is called an infinite loop and usually happens when you forget to update the variable being checked in the condition. Always make sure something inside the loop eventually makes the condition false.

### break Statement
`break` immediately exits the loop entirely, skipping any remaining iterations - even if the loop's condition is still true. Useful when you want to stop as soon as a certain condition is met.

### continue Statement
`continue` skips the rest of the code in the current iteration and jumps straight to the next one, without exiting the loop. Useful when you want to skip specific cases but keep looping.

### Nested Loops
A nested loop is a loop placed inside another loop. The inner loop completes all of its iterations for each single iteration of the outer loop. Commonly used for working with grids, tables, or patterns (like printing a multiplication table or a triangle of stars).

See `examples.py` for working code for each topic.
