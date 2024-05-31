# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# from collections import defaultdict


# if __name__ == '__main__':
#     s = input()
#     # name = deque()
#     word = defaultdict(int)
#     for _ in s:
#         word[_] += 1
    
#     sorted_word = sorted(word.items(), key=lambda x: x[1], reverse=True)
#     count = 0
#     # Print the sorted key-value pairs
#     for key, value in sorted_word:
#         count += 1
#         print(key, value)
#         if count == 3:
#             break

from collections import defaultdict

def check_same_values(d):
    value_set = set(d.values())
    return len(value_set) == 1
if __name__ == '__main__':
    s = input()
    word = defaultdict(int)
    for char in s:
        word[char] += 1
    
    # Sort the dictionary by values in descending order
    if check_same_values(word) == True:
        print("yes")
        sorted_word = sorted(word.items())
    else:    
        print("no")
        sorted_word = sorted(word.items(), key=lambda x: (-x[1],x[0]))
        
    # Print the top 3 frequent characters
    for char, frequency in sorted_word[:3]:
        print(char, frequency)

    
        
