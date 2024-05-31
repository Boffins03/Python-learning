a = list()
b = 0
i = 0
d = 0
while b == 0:
    n = int(input(''))
    a.append(n)
    if n == 0:
        break
c = int(len(a))
for i in range(c):
    d += a[i]

sum = d / (c-1)
print(sum)


