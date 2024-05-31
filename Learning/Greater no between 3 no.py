a=int(input('enter first number'))
b=int(input('enter second number'))
c=int(input('enter third number'))
if a>b:
    if a>c:
        print('a is greater number',a)
    else:
        print('c is greater number',c)
else:
    if b>c:
        print('b is greater number',b)
    else:
        print('c is greater number',c)
