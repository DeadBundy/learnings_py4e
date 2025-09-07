"""
romeo_words.py
---------------
Reads a text file, extracts all unique words,
and prints them in sorted order.

Example:
    python romeo_words.py
    (default file: romeo.txt)
"""

def main():
    # Ask for file name (default: romeo.txt)
    fname = input("Enter file name: ").strip()
    if not fname:
        fname = "romeo.txt"

    try:
        file_handle = open(fname, "r")
    except FileNotFoundError:
        print(f"Error: File '{fname}' not found.")
        return

    unique_words = []

    for line in file_handle:
        words = line.split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)

    unique_words.sort()
    print(unique_words)


if __name__ == "__main__":
    main()
