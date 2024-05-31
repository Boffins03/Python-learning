import re
N = int(input())
regex_pattern = re.compile(r'^[789]\d{9}$')
answer = list()
for _ in range(N):
    number = input()
    if regex_pattern.match(number):
        answer.append("YES")
    else:
        answer.append("NO")

for _ in answer:
    print(_)