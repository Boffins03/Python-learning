a=lambda b: b*b
print(a(int(input("enter a number:"))))
x = lambda a, b : a * b
print(x(5, 6))

multiply=lambda a,b=1:a*b
print(multiply(3,5))