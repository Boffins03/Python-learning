# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
A=set(map(int,input().split()))
n=int(input())
for i in range(n):
    c,d=input().split()
    C=set(map(int,input().split()))
    if c=='intersection_update':
        A.intersection_update(C)
                
    elif c=='update':
        A.update(C)
                    
    elif c=='symmetric_difference_update':
        A.symmetric_difference_update(C)
    
    elif c=='difference_update':
        A.difference_update(C)
            
s=sum(A)
   
print(s)   
