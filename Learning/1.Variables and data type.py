# input from user
a=int(input("Enter a number:"))
b=float(input("Enter a float number:"))
c=input("Enter a string:")
# printting multi line string
print('''hello
my name is huzaifa''')

# format string print
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#list print
x = {"apple", "banana", "cherry"}
print(x)
# print frozenset
x = frozenset({"apple", "banana", "cherry"})	
print(x)
#print bool
x = True
print(x)	
#print bytes
x = b"Hello"
print(type(x))
print(x)	
#print bytearray
x = bytearray(5)
print(x)
x = memoryview(bytes(5))
print(x)
x = None
print(x)
a=10^2
print(a)

b=1
def recursion(n):
    
    if n==1:
        return 1
    else:
        return(n*recursion(n-1))    

sum=recursion(5)
print(sum)        

a="35"
b=50
c=int(a)+b
print(c)

b=5.0
c=int(a)+b
print(c)

# try and exception

try:
    if a.isdigit() :
        print(a)
except ZeroDivisionError:
    print("A is not digit")  

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

