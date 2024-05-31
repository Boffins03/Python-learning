import math
def fahrenheit_to_celsius(f):
    c=((f-32)*5/9)
    return c
a=round(fahrenheit_to_celsius(int(input("Temp. in fahrenheit"))),3)
print(a)
