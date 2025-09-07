# Program: Count email distribution by hour from mbox file

# Ask user for file name (default to mbox-short.txt if none entered)
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = dict()

# Process each line of the file
for line in fh:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()

        # Extract hour from the timestamp
        time_str = words[5]          # e.g., "09:14:16"
        hour = time_str.split(":")[0]  # e.g., "09"

        # Count frequency of each hour
        count[hour] = count.get(hour, 0) + 1

# --- Sorting by frequency (Top 10 hours) ---
tmp = []
for hour, freq in count.items():
    tmp.append((freq, hour))

tmp = sorted(tmp, reverse=True)  # sort by frequency (highest first)

rank = 11
for freq, hour in tmp[:10]:
    rank -= 1
    print(f"TOP {rank}th common hour: {hour} {freq}")

# --- Alternative method: dynamic list comprehension ---
# print(sorted([(freq, hour) for hour, freq in count.items()], reverse=True))

# --- Sorting by hour (ascending by key) ---
print("\nSorted by hour:")
for hour, freq in sorted(count.items()):
    print(hour, freq)
