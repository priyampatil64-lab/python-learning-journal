# Day 4 - Dictionaries & If-Else
Reference: Engineering in Kannada - Python Zero to Hero (Part 7 & Part 8)
- Part 7: "Dictionaries in Python | Access and Modify elements in a dictionary"
- Part 8: "If, else and elif Statements in Python | Conditional Operators"

## Topics covered
- Creating dictionaries, key-value pairs
- Accessing, adding, updating & removing dictionary items
- Dictionary methods (keys, values, items, get, update, pop)
- Looping through dictionaries
- If, elif, else conditional statements
- Comparison & logical operators in conditions
- Nested if statements

## Notes

### Dictionaries
A dictionary is an unordered, mutable collection of **key-value pairs**, created with curly braces `{ }`. Keys must be unique and immutable (strings, numbers, tuples); values can be anything.

### Accessing & Modifying Dictionary Items
- `dict[key]` - access a value by its key (raises an error if the key doesn't exist)
- `dict.get(key)` - access a value safely, returns `None` (or a default) if the key is missing
- `dict[key] = value` - add a new key-value pair or update an existing one
- `del dict[key]` - removes a key-value pair

### Common Dictionary Methods
- `keys()` - returns all keys
- `values()` - returns all values
- `items()` - returns all key-value pairs as tuples
- `update(other_dict)` - merges another dictionary into this one
- `pop(key)` - removes a key and returns its value

### Looping Through a Dictionary
Use `for key, value in dict.items():` to loop through both keys and values at once.

### If, Elif, Else
Conditional statements let the program make decisions and run different code blocks depending on whether a condition is `True` or `False`.
- `if condition:` - runs if the condition is true
- `elif condition:` - checked only if the previous `if`/`elif` was false
- `else:` - runs if none of the above conditions were true

### Comparison Operators
`==`, `!=`, `>`, `<`, `>=`, `<=` - used to compare values inside conditions.

### Logical Operators
`and`, `or`, `not` - used to combine multiple conditions into one.

### Nested If Statements
An `if` statement placed inside another `if` (or `elif`/`else`) block, used when a decision depends on more than one level of conditions.

See `examples.py` for working code for each topic.
