# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

for _ in range(int(input())):
    input()  # We don't need to store the length of the deque
    
    # Create a deque from input elements
    d = deque(map(int, input().split()))

    # Initialize a variable to track the current comparison value
    current = float('inf')  # Set to positive infinity for comparison
    print(d)
    while d:
        # Compare the left and right ends of the deque
        if d[0] >= d[-1] and d[0] <= current:
            current = d.popleft()
            print(d)
        elif d[-1] >= d[0] and d[-1] <= current:
            current = d.pop()
            print(d)
        else:
            print('No')
            break
    else:  # Executed when the loop completes without hitting a 'break'
        print('Yes')
