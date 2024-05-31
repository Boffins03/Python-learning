# basic syntax
print("Hello World")
a=10
print(a)
b="hello\World"
print(b)
a="hello\nworld"
print(a)
print('''hello
      world how are you''')
print('\\')
print('abc')
print("\ab")
print("Seema\'s pen")
print("Amy's")

#create a variable and assign value 
a=10

#multi assignments
a=b=c=1
print(a,b,c)
a,b,c=1,2,3
print(a,b,c)
days=int(input("input:"))*3600*24
print(days)

#take a no and print 3 digit no as n(n+1)(n+2)
n=int(input("Enter a no:"))
n=2
no=str(n)+str(n+1)+str(n+2)
print(no)

#string slice
a="huzaifa"
print(a[0:])
print(a[:3])
print(a[0:6:2])
print(a[0:-4])
print(a[-2:])
print(a[-5:-1])
print(a[-1:0])

#list
list=list("hello")
list2=[2,4,6,8,10]
print(list,list2)
print(type(list))

#tuple
# tup=tuple(2,5,2,23,234)
tup2=(2,54,56,2,2)
print("tup",tup2)
# print(type(tup))

#arithmetic operator
a=5.0
b=10.0
c=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b%a)
print(2**3)
print(3^6) # don't know
print(b//c)

#Math library
import math
print(math.ceil(5.5))
print(math.sqrt(5))
print(math.exp(5))
print(math.fabs(-5))
print(math.floor(5.5))
print(math.log(5))
print(math.log10(5))
print(math.pow(5,2))
print(math.sin(5))
print(math.cos(5))
print(math.tan(5))
print(math.degrees(5))
print(math.radians(5))

#loops
for i in range(10):
    print(i)

i=1
while(i<10):
    print(i)
    i=i+1

#condition
if i>5:
    print("i is greater than 5")
elif i>10:
    print("i is greater than 10")
else:
    print("i is zero or i is less than zero")        

#nested loop and condition
a=int(input("Enter a no:")) 
if a>10:
    if a>20:
        print("a is greater than 20")
    else:
        print("a is less than 20 and greater than 10")
else:
    print("a is less than 10")
    for i in range(0,a):
        print(i)
        for j in (0,i):
            print(j)
            print(i*j)               
