store=[["shirt",20.00],['Tshirt',15.00],['pants',17.00],['socks',5.00]]

to_euro=lambda data:(data[0],[data[1]*.82])
to_dollor=lambda data:(data[0],[data[1]/.82])

store=list(map(to_euro,store))
for i in store:
    print(i)