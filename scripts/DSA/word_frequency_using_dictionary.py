# Word Frequency Counter

# Dictionary to store word counts
count = dict()

print("Enter a line of text: ")
line = input('')

# Split input into words
words = line.split()

print('Words:', words)
print('Counting...')

# Count occurrences of each word
for word in words:
    count[word] = count.get(word, 0) + 1

# Print dictionary with counts
print(count)

# Print each word with its count
for word in count:
    print(word, count[word])

# Print dictionary views
print(list(count))          # list of keys
print(list(count.keys()))   # explicit list of keys
print(list(count.values())) # list of values
print(list(count.items()))  # list of key-value tuples

# Iterate through key-value pairs
for key, value in count.items():
    print(key, value)
