# worng
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# from itertools import combinations
# n = int(input())
# N = list(input().split())
# l = len(N)
# K = int(input())
# letter = N[K-1]
# indices = []
# for index, value in enumerate(N):
#     if value == letter:
#         indices.append(index+1)
# print(indices)  
# li = list()
# for _ in range(1,l+1):
#     li.append(_)
# a = list(combinations(li,2))
# print(a)
# total = len(a)
# print(total)
# out = 0
# for i in a:
#         if i[0] in indices or i[1] in indices:
#                 out += 1
# print(out)
# answer = out/total    
# print(f"{answer:.3f}")

# wrong
# from itertools import combinations

# # Read input from STDIN
# n = int(input())
# N = list(input().split())
# K = int(input())

# # Find the letter at index K
# letter = N[K-1]

# # Find indices of the letter in the list
# indices = [index+1 for index, value in enumerate(N) if value == letter]

# # Generate all possible combinations of indices
# all_combinations = list(combinations(range(1, n+1), 2))

# # Count combinations containing the letter
# count = sum(1 for i, j in all_combinations if i in indices or j in indices)

# # Calculate the answer
# answer = count / len(all_combinations)

# # Print the answer with 3 decimal places
# print(f"{answer:.3f}")

# right
from itertools import combinations
N = int(input())
n = input().split()
K = int(input())

contain = 0
total = 0

for i in combinations(n, K):
    print(i)
    if "a" in i:
        contain += 1
    total += 1
print(f"{contain/total:.3f}")
        
