# := is walrus operator

happy=True
print(happy)

#walrus
print(happy := True)

foods=list()
while True:
    food=input("what food do you like? : ")
    if food=='quit':
        break
    foods.append(food)

#walrus
foods=list
while food :=input("what food do you like? :") !="quit":
    foods.append(food)     
