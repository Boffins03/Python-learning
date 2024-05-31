# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
ans = list()
for i in range(T):
    a = int(input())
    A = set(map(int,input().split()))
    b = int(input())
    B = set(map(int,input().split()))
    if A == A.intersection(B):
        ans.append("True")
    else:
        ans.append("False")
        
for _ in ans:
    print(_)            