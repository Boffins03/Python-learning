# tuple is not changeable
# creating tuple
a = tuple()
b = ()
print(type(b))
c = ('a',)
d = ('a')
print(type(c))
print(type(d))

# nested
e = (1,2,3,(4,5))
print(e)
f = tuple("hello")
print(f)
# bulid-in
a = a + b + c
print(a)
print(max(a))
print(a.index('a'))

# print(a.pop())
