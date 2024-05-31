from itertools import product

# Read input
k, n = map(int, input().split())

# Initialize a list to store the lists of integers
lists = []

# Read the lists of integers and append them to the 'lists' list
for _ in range(k):
    lists.append(list(map(int, input().split()[1:])))

# Initialize the variable to store the maximum result
max_result = 0

# Iterate through all possible combinations of elements from the lists
for combination in product(*lists):
    print(combination)
    # Calculate the sum of squares for the current combination and perform modulo n
    result = sum(x ** 2 for x in combination) % n
    # Update max_result if the current result is greater
    max_result = max(max_result, result)

# Print the maximum result
print(max_result)
