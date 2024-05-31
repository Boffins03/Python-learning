a=list(input("Enter a list:"))
def double(a:list)->list:
    for i in range(len(a)):
        a[i]=int(a[i])*2
    print(a)
double(a)        

string=input("Enter a str:")
def count(a:str):
    b=a.split(" ")
    print(b)
    return len(b)

count=lambda string:(string.split())
x=count(string)
print(len(x))

a=input("Enter")
c=a.split()
def sum(c:list):
    for i in c:
        b=0
        b=b+int(i)
    print(b)
sum(c)  

a=input("enter")
b=a.split()
c=0
for i in range(len(b)):
    print(b)
    for j in range(len(b)):
        if b[i]>=b[j]:
            c=int(b[i])
            print(c)
            print(b)
        else:
            b[i]=b[j]
            c=int(b[j])
            print(b)        
print(c)    

def max(b):
    m=b[0]
    for n in b:
        if int(n)>int(m):
            m=n
    return m

print(b)        
print(max(b))




# map fliter
numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
print([number for number in numbers if number % 2!=0])
