#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])
    count = 0

    # Helper function to check if a cell is within bounds
    def is_valid_cell(i, j):
        return 0 <= i < n and 0 <= j < m

    # Helper function to check if a cell is dominant
    def is_dominant(i, j):
        cell_value = grid[i][j]
        print(f"cell-{cell_value}")
        for x in range(max(0, i - 1), min(i + 2, n)):
            for y in range(max(0, j - 1), min(j + 2, m)):
                if is_valid_cell(x, y) and (x != i or y != j):
                    if grid[x][y] >= cell_value:
                        print(f"grid-{grid[x][y]}")
                        return False
        return True

    # Iterate through each cell in the grid
    for i in range(n):
        for j in range(m):
            if is_dominant(i, j):
                print(f"grid_dom-{grid[i][j]}")
                count += 1

    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
