square=list()
for i in range(1,11):
    square.append(i*i)

print(square)

square=[i*i for i in range(1,11)]
print(square)

student=[100,90,80,70,60,50,40,30,20,10,0]
pass_student=list(filter(lambda d:d >=60,student))
print(pass_student)

pass_student=[i for i in student if i>=60]
print(pass_student)