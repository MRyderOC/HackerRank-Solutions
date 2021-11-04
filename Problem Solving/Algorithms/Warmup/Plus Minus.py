#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
    
    n = len(arr)
    print(positive / n)
    print(negative / n)
    print((n - positive - negative) / n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

