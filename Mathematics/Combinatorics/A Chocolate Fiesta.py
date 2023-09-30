#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    odds, evens = 0, 0
    for item in a:
        if item % 2 == 0:
            evens += 1
        else:
            odds += 1

    if odds == 0:
        solution = (2 ** evens) - 1
    else:
        solution = ((2 ** (odds - 1)) * (2 ** evens)) - 1

    return solution % (10 ** 9 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
