# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
A = list()
B = list()
for i in range(int(n)):
    A.append(input())

for i in range(int(m)):
    B.append(input())

for i in B:
    for index,value in enumerate(A):
        if value == i:
            print(index+1,end=" ")
    print()        

# short
from collections import defaultdict
# Read input
n, m = map(int, input().split())

# Initialize defaultdict to store the indices of strings
indices = defaultdict(list)

# Read list A
for _ in range(n):
    indices[input()].append(_ + 1)

# Read list B
for _ in range(m):
    string_b = input()
    # Print indices of string_b in A, or -1 if not found
    print(*indices[string_b] or [-1])
