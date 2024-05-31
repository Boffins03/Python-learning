a=input("enter a word:")
c=""
for b in a:
    if b in "aeiouAEIOU":
        c=c + "g"
    else:
        c=c+b    

print(c)        