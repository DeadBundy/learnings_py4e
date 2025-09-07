# Extract email addresses from lines starting with "From "

# Ask for a file name, default to "mbox-short.txt" if blank
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

# Open the file
fh = open(fname)

count = 0
lines_with_from = []

# Read each line and check for "From " at the beginning
for line in fh:
    if line.startswith("From "):
        count += 1
        lines_with_from.append(line)

# Split each "From " line and print the second word (the email address)
for line in lines_with_from:
    pieces = line.split()
    print(pieces[1])
