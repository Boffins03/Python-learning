import os
def multi(*list):
    a=1
    if len(list)>1:
        for i in list:
            a=a*i
        return a
    else:
        for i in list:
            a=i*i
        return a
    

x=multi(1,2,3,4,5)
print(x)  
def default(a,b=1,c=1,d=10):
    x=a*b*c*d
    return x

print(default(1,5,10,15))  