import re

def first_repeating_character(expression):
    match = re.search(r'([a-zA-Z0-9])\1+', expression)
    if match:
        print(match.group(1))
    else:
        print(-1)

# Example usage
expression = input()
first_repeating_character(expression)
