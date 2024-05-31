a = [1,2,4,6,8,3]
for _ in a:
    print(_)

for i in range(len(a)-1,-1,-1):
    print(a[i])


a = a[::-1]
for _ in a:
    print(_)    