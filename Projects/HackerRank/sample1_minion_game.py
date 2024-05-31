S='banana'
b=list()
c=list()
d=list()

for i in range(1,len(S)+1):
    for j in range(len(S) - i):
        b.append(S[j:j + i + 1])
b=set(b)
b=list(b)
for k in range(len(S)):
    b.append(S[k])

print(b)
# print(set(b))