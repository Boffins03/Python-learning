import re

def find_substrings_with_vowels(input_string):
    pattern = r'(?<=[bcdfghjklmnpqrstvwxyz])[aeiouAEIOU]{2,}(?=[bcdfghjklmnpqrstvwxyz])'
    substrings = re.findall(pattern, input_string)
    if substrings:
        print('\n'.join(substrings))
    else:
        print(-1)

# Example usage
input_string = input()
find_substrings_with_vowels(input_string)
