# pypy  3
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
N = int(input())
commands = []  # Renamed 'command' to 'commands' for better readability
for _ in range(N):
    c = input().split()
    commands.append(c)

for command in commands:
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        try:
            s.remove(int(command[1]))  # Convert the string to an integer
        except:
            pass    
    elif command[0] == 'discard':
        s.discard(int(command[1]))  # Convert the string to an integer

print(sum(s))  # Sum the elements of the set directly   

# pypy 3
n = input()
s = set(map(int, input().split()))
for i in range(int(input())):
    c = input().split()
    if c[0] == 'pop':
        s.pop()
    elif c == 'remove':
        s.remove(int(c[1]))
    else:
        s.discard(int(c[1]))
print(sum(s))