N = int(input())
n = list(map(int, input().split()))
print(all(map(lambda x: x > 0, n)) and any(map(lambda x: str(x) == str(x)[::-1], n)))