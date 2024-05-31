import pdb
a = "japan"
b = "ringo"
c = "12454"
# operation on string
d = a + b
print(d)
print(c*2)
print("pan" in a)
print("6" not in c)
print(a in d)
# camparison operator
print("a" == a)
print(a != "a")
print('a' < "A")
print('a' > "A")
# slice
pdb.set_trace()
print(a[1:4])
print(a[-3:-1])
# bulid-in function
print(c.isalnum())
print(a.find("ap"))
print(a.index("n"))
print(b.index("go"))
print(b.upper())
z = eval('5+2')
print(z)