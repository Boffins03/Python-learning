# average of list's number
a=list()
b=0
i=0
d=0
print("Enter no.")
while b==0:
    n=input()
    if n=='':
        break
    else:
        a.append(int(n))
    
c=int(len(a))    
for i in range(c):
   d+=a[i]
   
sum=d/c   
print(sum)
    
  
