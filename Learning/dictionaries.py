# store  in key:value pair
dic1 = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"July"}
print(dic1[1])
print(dic1.keys())
print(dic1.values())
print(dic1.get(2))
dic1[6] = "June"
print(dic1)
dic1[7] = "July"
dic1[8] = "Aug"
print(dic1)
del dic1[8]
