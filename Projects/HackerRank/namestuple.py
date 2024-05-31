from collections import namedtuple
N, columns = int(input()),input().split() # Read input
Student = namedtuple('Student', columns) # Create a namedtuple dynamically
print(sum(int(Student._make(input().split())[columns.index("MARKS")]) for _ in range(N)) / N) # Calculate the average of marks


from collections import namedtuple
N = int(input())
c = input().split()
i = c.index("MARKS")
marks = list() 
for j in range(N):
    a = input().split()
    marks.append(int(a[i]))
    
print(sum(marks)/N)    
    
    