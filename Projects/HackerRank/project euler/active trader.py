#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    # Write your code here
    trader = {}
    for i in customers:
        if i in trader:
            trader[i] += 1
        else:
            trader[i] = 1
    
    # Filter out customers whose transaction frequency exceeds 5% of the total
    total = len(customers)
    final = []
    for key, value in trader.items():
        if value / total >= 0.05:
            final.append(key)
    
    return sorted(final)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
