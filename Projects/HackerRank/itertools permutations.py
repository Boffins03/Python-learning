# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,k = input().split()
a = list(permutations(s,int(k)))
for i in sorted(a):
    for j in i:
        print(j,end="")
    print()    