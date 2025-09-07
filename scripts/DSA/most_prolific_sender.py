# Program to find the sender with the greatest number of mail messages
# Reads 'mbox-short.txt' (or user-specified file)
# Looks for "From " lines → extracts email address → counts frequency
# Finds the email with the maximum count

# Initialize dictionary and helper variables
email_counts = dict()
emails_list = []
max_sender = None
max_count = None

# Take input file name, default to "mbox-short.txt"
filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"

# Open the file
with open(filename) as handle:
    # Collect all lines starting with "From "
    for line in handle:
        if line.startswith("From "):
            emails_list.append(line)

# Build dictionary of email counts
for line in emails_list:
    pieces = line.split()
    email = pieces[1]  # second word is email
    email_counts[email] = email_counts.get(email, 0) + 1

# Find the most prolific committer
for sender, count in email_counts.items():
    if max_sender is None or count > max_count:
        max_sender = sender
        max_count = count

# Print result
print(max_sender, max_count)
