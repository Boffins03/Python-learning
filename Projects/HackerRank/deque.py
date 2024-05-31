from collections import deque

N = int(input())
name = deque()

for _ in range(N):
    i = input().split()
    if len(i) > 1:
        if i[0] == 'append':
            name.append(i[1])
        elif i[0] == 'appendleft':
            name.appendleft(i[1])
    else:
        if i[0] == 'pop':
            name.pop()
        elif i[0] == 'popleft':
            name.popleft()

# Print the elements of the deque
print(*name)
