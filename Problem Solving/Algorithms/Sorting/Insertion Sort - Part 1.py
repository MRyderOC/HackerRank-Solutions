#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    i = n - 1
    x = arr[i]
    while True:
        if i == 0 or arr[i - 1] <= x:
            arr[i] = x
            print(" ".join(list(map(str, arr))))
            break

        arr[i] = arr[i - 1]
        i -= 1
        print(" ".join(list(map(str, arr))))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
