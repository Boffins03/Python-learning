a = "world"
b = "WORLD"
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print("Nothing")

print(a.replace('w',"q"))
# a=c
print(a)
print(dir(a))

file=open('app.txt','r')
print(file.readlines())
# di=dict()
# for lin in file:
#     lin=lin.rstrip()
#     word=lin.split()
#     for w in word:
#         print(w)
#         if w in di:
#             di[w]=di[w]+1
#             print("***Existing***")
#         else:
#             di[w]=1
#             print("***New***")
#         print(w,di[w])