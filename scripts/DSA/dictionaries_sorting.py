# Demonstrating sorting dictionaries in Python

# Dictionary with some key-value pairs
num = dict()
num['a'] = 10
num['c'] = 3
num['b'] = 20
num['d'] = 10   # values CAN repeat, but keys must be unique

# Show all items as (key, value) pairs
print("Dictionary items:", list(num.items()))

# Sort by keys (alphabetical order)
print("Sorted by keys:", sorted(list(num.items())))

# OR directly loop in sorted order of keys
print("Loop sorted by keys:")
for k, v in sorted(num.items()):
    print(k, v)

# To sort by values, flip (key, value) → (value, key)
tmp = list()
for key, value in num.items():
    tmp.append((value, key))

# Ascending order (smallest value first)
print("Sorted by values (ascending):", sorted(tmp))

# Descending order (largest value first)
print("Sorted by values (descending):", sorted(tmp, reverse=True))
