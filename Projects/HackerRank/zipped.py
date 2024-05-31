N,X = map(int,input().split())
Marks = list()
for i in range(X):
    marks = list(map(float,input().split()))
    Marks.append(marks)

average = list()
for i in range(N):
  sum = 0
  for j in range(X):
    sum += Marks[j][i] 
  Average = sum/X
  print(sum,Average)
  average.append(Average)

for _ in average:
    print(_)