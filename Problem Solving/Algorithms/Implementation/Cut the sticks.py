#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    out = []
    while True:
        n = len(arr)
        if n == 0:
            return out

        out.append(n)
        shortest = min(arr)
        i = 0
        while i < len(arr):
            if arr[i] - shortest == 0:
                del arr[i]
                continue
            else:
                arr[i] -= shortest

            i += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
