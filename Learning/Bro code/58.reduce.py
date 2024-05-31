import functools
text=['h','e','l','l','o']
word=functools.reduce(lambda x,y:x+y,text)
print(word)

#factorial of any input number 
a=int(input("Enter the number you want to factorial:"))
b=list()
for i in range(1,a+1):
    print(i)
    b.append(i)

print(b)
f=functools.reduce(lambda x,y:x*y,b)
print(f)    