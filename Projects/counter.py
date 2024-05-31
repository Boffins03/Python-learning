print("""Welcome to counter app
'+' is for add
'-' is for subtract
'exit' is for Exit""")
a=""
count=0
print("Count=",count)
while a!="exit":
    a=input("Enter:")
    if a=='+':
        count+=1
        print("Count=",count)
    elif a=="-":
        count-=1
        print("Count=",count)
    elif a=="exit":
        print("Thanks for using counter app")
        break 
    else:
        print("Enter right option '+,-,exit'")
        continue
