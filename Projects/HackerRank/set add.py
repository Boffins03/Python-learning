# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
country = set()
for i in range(N):
    country.add(input())
print(len(country))