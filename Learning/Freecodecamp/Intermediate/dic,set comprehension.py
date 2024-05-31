# dictionary comprehension
pairs = [('a',1),('b',2),('c',3)] # list of pair items key,value

dic = {k:v for k,v in pairs} #comprehension

print(dic) # printing

# set comprehension

numbers = [2,3,5,6,3,2,4,5,6,6,6,4,3,2,1] # list with repeated numbers
s = set()
for i in sorted(numbers):
    print(i)
    s.add(i**2)

print(s)

s = {x ** 2 for x in sorted(numbers)} # comprehension

print(s) # printing