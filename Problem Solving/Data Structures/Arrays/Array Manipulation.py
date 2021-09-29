#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate
import array

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    arr = array.array('q', [0] * n)
    for q in queries:
        a, b, k = q[0]-1, q[1]-1, q[2]
        arr[a] += k
        if b != n-1:
            arr[b+1] -= k
    return max(accumulate(arr))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

