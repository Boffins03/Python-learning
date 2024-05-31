a = [1,2,3,4,5,6,7,8,9]

b = [i for i in range(1,10) if i % 2 == 0]
print(b)
b.sort()
print(b)
a = sorted(a)
print(a)
print(sum(a))