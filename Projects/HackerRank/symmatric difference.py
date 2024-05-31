# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))
d = set()
d.update(N.difference(M))
d.update(M.difference(N))
d = list(d)
for _ in sorted(d):
    print(_)