# Program to read a file and find the word that appears most frequently

# Dictionary to store word counts
word_counts = dict()

# Take input from user, default to "mbox-short.txt"
filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"

# Open file
with open(filename) as handle:
    for line in handle:
        line = line.rstrip()
        words = line.split()

        # Count each word in the line
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

# Find the most common word
max_word = None
max_count = None
for word, count in word_counts.items():
    if max_count is None or count > max_count:
        max_word = word
        max_count = count

# Print result
print(max_word, max_count)
