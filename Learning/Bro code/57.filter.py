friend=[["Ross",20],["Lucy",12],["Mark",18],["Jonh",19],['Rachel',25]]

data=lambda data: data[1] >= 18
friend=list(filter(data,friend))

for i in friend:
    print(i)