# Day 3 - Lists, Tuples & Sets
Reference: Engineering in Kannada - Python Zero to Hero (Part 5 & Part 6)

## Topics covered
- Creating lists, accessing & slicing
- List methods (append, insert, remove, pop, sort, reverse, etc.)
- List comprehension
- Tuples - creation, immutability, indexing & slicing
- Tuple methods (count, index)
- Sets - creation, uniqueness, set operations
- Set methods (add, remove, union, intersection, difference)

## Notes

### Lists
A list is an ordered, mutable collection that can hold items of different data types, created with square brackets `[ ]`.

### Accessing & Slicing Lists
Works the same way as strings - zero-based indexing, negative indexing from the end, and `list[start:stop:step]` slicing.

### Common List Methods
- `append(x)` - adds an item to the end
- `insert(i, x)` - inserts an item at a given index
- `remove(x)` - removes the first matching item
- `pop(i)` - removes and returns the item at index `i` (last item if no index given)
- `sort()` - sorts the list in place
- `reverse()` - reverses the list in place
- `clear()` - removes all items

### List Comprehension
A concise way to create lists in a single line: `[expression for item in iterable if condition]`.

### Tuples
A tuple is an ordered, **immutable** collection created with parentheses `( )`. Once created, its items cannot be changed, added, or removed.

### Tuple Methods
- `count(x)` - counts occurrences of `x`
- `index(x)` - returns the index of the first occurrence of `x`

### Sets
A set is an unordered collection of **unique** items created with curly braces `{ }` or `set()`. Duplicates are automatically removed.

### Common Set Methods & Operations
- `add(x)` - adds an item
- `remove(x)` - removes an item (raises an error if missing)
- `discard(x)` - removes an item without raising an error
- `union()` / `|` - combines two sets
- `intersection()` / `&` - common items between sets
- `difference()` / `-` - items in one set but not the other

See `examples.py` for working code for each topic.
