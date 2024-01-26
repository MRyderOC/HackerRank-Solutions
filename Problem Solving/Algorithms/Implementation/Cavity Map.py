#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    n = len(grid)
    grid_list = [list(map(int, list(g))) for g in grid]

    idxs = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            cur_val = grid_list[i][j]
            if (
                cur_val > grid_list[i - 1][j] and
                cur_val > grid_list[i + 1][j] and
                cur_val > grid_list[i][j - 1] and
                cur_val > grid_list[i][j + 1]
            ):
                idxs.append([i, j])

    for idx in idxs:
        grid_list[idx[0]][idx[1]] = "X"

    return ["".join(list(map(str, row))) for row in grid_list]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
