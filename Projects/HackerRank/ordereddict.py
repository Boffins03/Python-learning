from collections import OrderedDict

N = int(input())
ordered_dict = OrderedDict()

# Read and process input
for _ in range(N):
    data = input().split()
    key = ' '.join(data[:-1])  # Extract key by joining all elements except the last one
    value = int(data[-1])      # Convert the last element to an integer
    ordered_dict[key] = ordered_dict.get(key, 0) + value  # Add value to the existing key or initialize it to 0

# Print the keys of the ordered dictionary
for key,value in ordered_dict.items():
    print(key, value)


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
l = list()
d = dict()
for i in range(N):
    l.append(list(input().split()))
    
   
for i in l:
    a = " ".join(i[:-1])
    b = int(i[-1])
    if a in d.items():
        d[a] += d[b]
    else:    
        d[a] = d[b]
for i in d:
    print(i)