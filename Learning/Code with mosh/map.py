a=input("enter")
for i in a:
    if a.islower()==True:
        print(a)
        break
    if i.isupper()==True:
        c=a.replace(i,'_'+i.lower())
        print(c)
