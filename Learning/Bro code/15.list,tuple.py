import random       # import random module

tuple=(4,5,6,3,2,1) # creating a tuple
list=[1,2,3,4,5]    # creating a list                
a={'a':1,'b':2,'c':3} # creating dictionary 
b=[[3,4,2],655,3,6,3,2] # creating 2D list
print(b[0][2]) # print 2 from inner list
c={"my","name","is","Huzaifa"} # creating set
c.pop() # pop last element
print(c)
for i in c:
    print(i)

print(a.items())

# print(round(abs(float(input("enter a number")))))

a="name"
def function_name(Name,Class): # Creating a function with two passing argument
    print(f'My name is {Name} and I am in class {Class}')

function_name("Huzaifa","B.CA") # calling fuction

def arg(*num): # function in which you can pass as many as argument  
    sum=0
    for i in num:
        sum += i
    return sum
    
b=arg(1,2,3,4,5)    
print(b)

def karg(**k): # function taking keyword argument 
    print(f"My name is {k['name']}. I live in {k['city']}. I am {k['age']} years old.")

karg(name="Huzaifa",city="Shamli",age=20)
print(random.choices(list))
print(random.choice(list))
print(random.shuffle(list))
print(list)




# n=eval(input("enter a list"))
# m=eval(input("enter a tuple"))

# print(n,m)
# print(type(n),type(m))

S=input("Enter a string :") 
a=len(S)
s=[]
for i in S:
   s.append(i) # appending every single element from string into list
   
s.sort() # sorting list
print(s) 