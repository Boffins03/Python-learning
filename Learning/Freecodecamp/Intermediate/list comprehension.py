Number_list = list() # Creating empty list

# Through loop adding 1-9 number in list 
for i in range(10):  
    Number_list.append(i)

print(Number_list) # printing

number_list = [i for i in range(10)] # comprehension of the above loop

print(Number_list == number_list) # Checking the both list(comprehension and loop created)

even_number = []  # Creating empty list

# Adding even number in list through loop
for i in range(50):
    if i % 2 == 0:
        even_number.append(i)

print(even_number) # printing 

Even_number = [i for i in range(50) if i % 2 == 0] # comprehension of the above loop

print(even_number == Even_number) # Checking the both list(comprehension and loop created)

# comprehension with multiple condition

name = ['any','mike','apple','b','annay'] # list of random name
choose = [] # empty list
for n in name: # looping and checking condition of word starting with 'a' and ending with 'y' and adding in list
    if len(n) <= 1:
        continue
    if n[0] != 'a':
        continue
    if n[-1] != 'y':
        continue
    choose.append(n)

print(choose) # printing

choose_name = [n for n in name 
               if len(n) >= 2
               if n[0] == 'a'
               if n[-1] == 'y'] # comprehension of the above loop

print(choose == choose_name) # Checking the both list(comprehension and loop created)

# nested list comprehension
nested_list = [[2,3,56,3],[8,4,6,2],[2,6,1,9]] # nested list of random number
single_list = [] # empty list

for i in nested_list: # adding each element of the nested list in new list 
    for j in i:
        single_list.append(j)

print(single_list) # printing

Single_list = [j for i in nested_list for j in i] # comprehension of the above loop
print(single_list == Single_list) # Checking the both list(comprehension and loop created)

#  if/else comprehension

categories = [] # empty list

for i in range(20): # adding even and odd in list according to the value
    if i % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")    

print(categories)

Categories = ["Even" if i % 2 == 0 else "Odd" for i in range(20)] # comprehension of above loop

print(categories == Categories) # Checking the both list(comprehension and loop created)

# multi dimension array

empty_list = [] # empty list

for i in range(5): # 3-dimension list of lists
    l2 = []
    for j in range(5):
        l3 = []
        for k in range(5):
            l3.append(k)
        l2.append(l3)
    empty_list.append(l2)        

print(empty_list) # printing

Empty_list = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)] # comprehension of the above loop

print(empty_list == Empty_list) # Checking the both list(comprehension and loop created)

# using function in comprehension
#square function
def square(x):
    return x ** 2

# comprehension
square_list = [square(x) for x in range(10)]
print(square_list) # printing
