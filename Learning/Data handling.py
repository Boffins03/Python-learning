# integer number
a = 13
# float number
b = 13.0
# complex number
c = 33 + 2j
d = 3 + 3.1j
print(c-d)

print(c.real)
print(d.imag)

# string as a sequence of character
a = "Hello"
for _ in a:
    print(_, end="")

# indexing
print(a[0])
print(a[-1])
print(a[-1:0])
print(a[-1:-5])
print(a[0:-1])
print(a[2:4:1])

# list
x = [3]
z = [1,2,4,6,3,8]
z.append(x)
print(z)
print(z.sort)
print(x.insert(0,3))

# tuple
i = (9)
print(type(i))
j = (3,)
print(type(j))
k = ("adf","hnek",97)
print(k.index(97))
print(k.__add__(("hello",)))

# dictionary
dic = {"name":"huzaifa","age":21}
print(dic)
print(dic.get("age"))
print(dic.keys())
print(dic.items())
# dic.update("age")
# dic.update("home","shamli")
print(dic)

# mutable
# a[0] = "J"
print(a)

#Operators
#  Arithmetic
print(4 + 5)
print(9 - 1)
print(4 *2, 10/5, 9//2, 10%7, 2**5)
# unary 
a = 5
print(a)
a += 5
print(a)
a -= 1
print(a)
# relation operators
if a < 10 :
    print("hello")
elif a == 10:
    print("world")
else:
    print("hello world")

# bitwise
if (2 + 2 == 4) and (3 + 4 == 7):
    print(11)
elif (2 == 2) or (2 == 4):
    print(True)

#type convert
a = 10
print(type(a))
a = float(a) 
print(type(a))

# 
import random
# randint fuction take two value and find one in b/w
print(random.randint(10,100))
print(random.random())
# take 3 value start,end,gap
print(random.randrange(0,100,2))
