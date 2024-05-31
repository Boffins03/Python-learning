# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
n = int(input())
answer = False
for i in range(n):
    n = set(map(int,input().split()))
    if n == n.intersection(A):
        if len(n) == n.intersection(A):
            answer = False 
            break
        else:
            answer = True
    else:
        answer = False
        break

print(answer)                    

