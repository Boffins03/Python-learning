import re

# Check if the regular expression is valid and matches the pattern .*\\+
def check(regex):
    pattern = r'^.*\\\+?$'
    if re.match(pattern, regex):
        return True
    else:
        return False
    # return bool(re.search(r'\.\*\\\+', regex))

# Example regular expressions
regex1 = ".*\+" # True
regex2 = "[a-zA-Z0-9,.' ]+" # True
regex3 = "/^(?!\.)(?=.)[d-\.]$/" # False
regex4 = "[0-9]++" # False
regex5 = "[0-9]" # True
regex6 = "123" # True
regex7 = "2"  # True
regex8 = ".*+" # False
# Check the regular expressions
print("Regex 1:", check(regex1))
print("Regex 2:", check(regex2))
print("Regex 3:", check(regex3))
print("Regex 4:", check(regex4))
print("Regex 5:", check(regex5))
print("Regex 6:", check(regex6))
print("Regex 7:", check(regex7))
print("Regex 8:", check(regex8))
