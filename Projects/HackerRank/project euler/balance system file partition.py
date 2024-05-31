#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def mostBalancedPartition(parent, files_size):
    # Calculate subtree sizes using DFS
    subtree_sizes = [0] * len(parent)
    
    def dfs(node):
        size = files_size[node]
        for child in range(len(parent)):
            if parent[child] == node:
                size += dfs(child)
        subtree_sizes[node] = size
        return size
    
    total_size = dfs(0)
    
    # Find the partition node with minimum difference in subtree sizes
    min_diff = float('inf')
    partition_node = -1
    
    def find_partition(node):
        nonlocal min_diff, partition_node
        for child in range(len(parent)):
            if parent[child] == node:
                diff = abs(2 * subtree_sizes[child] - total_size)
                if diff < min_diff:
                    min_diff = diff
                    partition_node = diff
                find_partition(child)
    
    find_partition(0)
    
    return partition_node
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    fptr.write(str(result) + '\n')

    fptr.close()
