import random

country="india"
name="huzaifa"
letter=f"hey my name is {name} and I am from {country}"

list=[2,5,2,24,6,3,6,3,12,45]
print(letter)
random.shuffle(list)
print(list)
x=random.choice(list)
print(x)
print(random.random())
print(random.randint(2,10))
print(random.randrange(2,8,2))

try:
    print("Hello world")
except ZeroDivisionError:
    print("divide by 0")
except SyntaxError:
    print("hello")    