# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s,k = input().split()
s = sorted(s)
a = list(combinations_with_replacement(s,int(k)))
for i in a:
    for j in i:
        print(j,end="")
    print()