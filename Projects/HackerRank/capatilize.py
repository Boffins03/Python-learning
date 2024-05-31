import re

def capitalize_words_except_numbers(input_str):
    # Split the input string into words using regular expression
    words = re.findall(r'\b\d*\w+\b', input_str)

    # Capitalize the first character of each word that doesn't start with digits
    capitalized_words = [word.capitalize() if not word[0].isdigit() else word for word in words]

    # Join the words back together preserving the original spaces
    output_str = ""
    for i, word in enumerate(words):
        output_str += capitalized_words[i]
        # Add the original space after the word if it was present
        if i < len(words) - 1:
            output_str += input_str[len(output_str):input_str.find(words[i+1], len(output_str))] 

    return output_str

# Example usage:
input_string = "hello 12abc world. this   is 123 test"
result = capitalize_words_except_numbers(input_string)
print(result)
