A = int(input())
set_a = set(map(int, input().split()))

# Read the number of other sets
N = int(input())
for i in range(N):
    command = input().split()
    set_n = set(map(int, input().split()))
    if command[0] == 'intersection_update':
        set_a.intersection_update(set_n)
    elif command[0] == 'update':
        set_a.update(set_n)
    elif command[0] == 'symmetric_difference_update':
        set_a.symmetric_difference_update(set_n)
    elif command[0] == 'difference_update':
        set_a.difference_update(set_n)
        
# Calculate and print the sum of elements in set A
print(sum(set_a))
