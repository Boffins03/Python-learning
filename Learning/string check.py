# write your code here
# remember: the variable email is already defined
a="email@gmail.com"
j=0
i=()
for i in a:
    if i!='@':
        j+=1
        print(a[0:j])
    if i=='@':
        break
