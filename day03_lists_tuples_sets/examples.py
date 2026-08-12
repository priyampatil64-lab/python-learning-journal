# Day 3 - Lists, Tuples & Sets Examples

# ---------- Creating lists ----------
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)

# ---------- Accessing & slicing ----------
print(fruits[0])       # 'apple' - first item
print(fruits[-1])      # 'orange' - last item using negative index
print(fruits[1:3])     # ['banana', 'mango']
print(fruits[::-1])    # reversed list

# ---------- List methods ----------
fruits.append("grape")
print(fruits)           # adds 'grape' at the end

fruits.insert(1, "kiwi")
print(fruits)            # inserts 'kiwi' at index 1

fruits.remove("banana")
print(fruits)            # removes 'banana'

popped = fruits.pop()
print(popped, fruits)    # removes & returns the last item

numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)            # [1, 2, 5, 7, 9]

numbers.reverse()
print(numbers)            # [9, 7, 5, 2, 1]

# ---------- List comprehension ----------
squares = [x ** 2 for x in range(1, 6)]
print(squares)             # [1, 4, 9, 16, 25]

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)        # [2, 4, 6, 8, 10]

# ---------- Tuples ----------
coordinates = (10, 20)
print(coordinates[0])      # 10
print(coordinates[-1])     # 20

colors = ("red", "green", "blue", "red")
print(colors.count("red"))   # 2
print(colors.index("blue"))  # 2

# Tuples are immutable - this line would raise an error if uncommented:
# coordinates[0] = 100

# ---------- Sets ----------
fruit_set = {"apple", "banana", "mango", "apple"}
print(fruit_set)            # duplicates removed automatically

fruit_set.add("kiwi")
print(fruit_set)

fruit_set.discard("banana")
print(fruit_set)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))          # {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b))   # {3, 4}
print(set_a.difference(set_b))     # {1, 2}
