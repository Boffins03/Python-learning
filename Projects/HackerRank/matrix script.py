
import math
import os
import random
import re
import sys

def replace_symbols(s):
    return re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', s)
    
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
s = list()
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(m):
    for _ in matrix:
        s.append(_[i])
s = "".join(s)
final_script = replace_symbols(s)
print(final_script)            