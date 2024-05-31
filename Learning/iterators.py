mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

a,b="4",3
print("A is "+a)
print("B is ",b)
print("Your age is ",b,"years old")

name=input("Enter your name:")
age=int(input("Enter your age:"))
if age>18:
    print(name,"is an adult now!")
else:
    print(name,"is under age",age)    

list=['name','class','rollno','srno']
for i in list:
    print(i)    