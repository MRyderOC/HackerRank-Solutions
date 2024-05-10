#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#


def power_sum_helper(X, N, i):
    if i ** N > X:
        return 0
    elif i ** N == X:
        return 1
    else:
        new_X = X - (i ** N)
        return power_sum_helper(X, N, i + 1) + power_sum_helper(new_X, N, i + 1)


def powerSum(X, N):
    # Write your code here
    return power_sum_helper(X, N, 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
