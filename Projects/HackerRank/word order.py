# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
word = dict()
for i in range(n):
    a = input()
    if a in word.keys():
        word[a] += 1
    else:    
        word[a] = 1
print(len(word.keys()))
for value in word.values():
    print(value,end=" ")

from collections import defaultdict

n = int(input())
word = defaultdict(int)

# Read input and count occurrences
for _ in range(n):
    word[input()] += 1

# Print the number of distinct words
print(len(word))

# Print the counts of occurrences
print(*word.values(), end=" ")
