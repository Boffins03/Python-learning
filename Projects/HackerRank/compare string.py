from itertools import groupby

# Input string
s = input()

# Group characters by count
groups = [(len(list(g)), int(k)) for k, g in groupby(s)]

# Print each group in the specified format
for count, char in groups:
    print(f"({count}, {char})", end=" ")
