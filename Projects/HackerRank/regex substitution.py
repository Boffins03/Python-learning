# N = int(input())

# # Read input lines until EOF
# text = []
# for _ in range(N):
#     line = input()
#     text.append(line.rstrip())
# # Process each line to replace `&&` with `and` and `||` with `or`
# processed_text = []
# check = True
# for line in text:
#     for _ in  line:
#         if _ == "#":
#             check = False
#             break
#     if check == False:
#         processed_text.append(line)
#     else:
#         line = line.replace(' && ', ' and ').replace(' || ', ' or ')
#         processed_text.append(line)
#         check = True


# # Print the processed lines with preserved indentation
# for line in processed_text:
#     print(line)

import re

N = int(input())

# Read input lines until EOF
text = []
for _ in range(N):
    line = input()
    text.append(line.rstrip())

# Process each line to replace `&&` with `and` and `||` with `or`
processed_text = []
for line in text:
    # Use regular expressions to replace `&&` and `||` with boundaries to avoid partial replacements
    line = re.sub(r'(?<=\s)&&(?=\s)', 'and', line)
    line = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', line)
    processed_text.append(line)

# Print the processed lines with preserved indentation
for line in processed_text:
    print(line)

