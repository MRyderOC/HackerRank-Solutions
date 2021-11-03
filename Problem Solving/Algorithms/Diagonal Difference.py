#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # result = diagonalDifference(arr)
    diag = 0
    inv_diag = 0
    for i in range(n):
        diag += arr[i][i]
        inv_diag += arr[i][n-i-1]
    
    fptr.write(str(abs(diag - inv_diag)) + '\n')

    fptr.close()

