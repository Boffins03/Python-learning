# list is changeable
# creating list
a1 = list()
a = []
b = [2]
c = [4,23]
d = ['a','b','c']
e = [3445,234,56,'adf','adfg']
# nested list
f = ['a','b','c',[1,2,3]]

# index 
print(b[0])
# bulid-in-func
print(len(e))
print(a in c)
for _ in e:
    print(_)

d[0] = 1
print(d)
# join list
x = a + b
print(x)
a1.extend(f)
#adding item in list
a.append(d) # add in last
print(a)
a.insert(0,a1)
print(a)
# pop
a.pop()
print(a)
# remove
c.remove(23)
print(a.count(()))
# clear
c.clear
print(c)
a.reverse()
print(a)
a.sort()
print(a)
