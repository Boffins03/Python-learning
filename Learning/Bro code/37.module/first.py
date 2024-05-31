# import second
# second.greeting("name")
from second import greeting
greeting("name")

a=input("Enter your name:")
b=lambda a : greeting(a)
print(b)