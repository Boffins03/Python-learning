import re

S = input()
k = input()

pattern = re.compile(re.escape(k))  # Use re.escape to handle any special characters in k
matches = pattern.finditer(S)

found = False  # Flag to track if any matches are found

for match in matches:
    start = match.start()
    end = match.end()
    gap = end - start
    add = len(k) - 1
    if gap > add:
        while start < end:
            if S[start:start+len(k)] == k:
                print(f"({start}, {start + add})")
            if add == 0:
                start += gap
            else:
                start += add
    found = True  # Set the flag to True when a match is found

if not found:  # Check the flag after the loop
    print((-1, -1))
