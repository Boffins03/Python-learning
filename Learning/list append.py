# please work with the variable 'list_of_strings'
list_of_strings=list()
j=int(0)
a=input()
for i in a:
    list_of_strings.append(a)
    list_of_strings[j]=int(i+1)
    j+=1
print(list_of_strings)
