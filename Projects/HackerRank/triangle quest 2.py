# int
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")    
    print()    
# str
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
ans = list()
for i in range(1,N+1):
    for j in range(1,i+1):
        ans.append(str(j))
    for j in range(i-1,0,-1):
        ans.append(str(j))    
    ans.append("\n")

ans.pop()
a = "".join(ans)
print(a)        
# direct
for i in range(1, int(input()) + 1):
    print(((10 ** i - 1) // 9) ** 2)
      