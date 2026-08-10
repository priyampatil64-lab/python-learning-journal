# Day 2 - Strings & Operators
Reference: Engineering in Kannada - Python Zero to Hero (Part 3 & Part 4)

## Topics covered
- Accessing string characters
- String slicing
- Escape sequences
- Operators: Assignment, Comparison, Logical, Membership, Bitwise, Arithmetic

## Notes

### Accessing String Characters
Access individual characters using zero-based indexing. Negative indexing counts from the end of the string (-1 is the last character).

### Slicing Strings
Extract a substring using `string[start:stop]`. `start` is inclusive, `stop` is exclusive. Leaving `start` or `stop` blank slices from the beginning or to the end.

### Escape Sequences
Special characters in strings starting with a backslash `\`:
- `\n` - new line
- `\t` - tab space
- `\\` - backslash

### 1. Assignment Operators
Used to assign values to variables. `=` is the simplest; compound versions combine an arithmetic operation with assignment.
`=` `+=` `-=` `*=` `/=` `%=`

### 2. Comparison Operators
Compare two values and return `True` or `False`.
`==` `!=` `>` `<` `>=` `<=`

### 3. Logical Operators
Combine conditional statements.
- `and` - True if both conditions are true
- `or` - True if at least one condition is true
- `not` - reverses the logical state

### 4. Membership Operators
Test whether a value exists in a sequence (list, string, tuple).
- `in` - True if value is found
- `not in` - True if value is not found

### 5. Bitwise Operators
Operate on the binary representation of integers.
`&` (AND) `|` (OR) `^` (XOR) `~` (NOT) `<<` (left shift) `>>` (right shift)

### 6. Arithmetic Operators
`+` `-` `*` `/` `//` (floor division) `%` (modulus) `**` (exponent)

See `examples.py` for working code for each topic.
