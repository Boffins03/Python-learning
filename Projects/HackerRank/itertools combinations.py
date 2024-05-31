# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,k = input().split()
s = sorted(s)
for _ in range(1,int(k)+1):
    a = list(combinations(s,_))
    for i in sorted(a):
        for j in i:
            print(j,end="")
        print()    