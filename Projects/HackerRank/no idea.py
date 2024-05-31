# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = int(input()).split()
array = int(input()).split()
A = set(int(input()).split())
B = set(int(input()).split())

happiness = 0
for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
        
print(happiness)        
        