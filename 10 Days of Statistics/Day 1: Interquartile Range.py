#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def quartiles(arr):
    def medianFinder(l, n):
        return l[n//2] if n % 2 == 1 else (l[n//2] + l[(n//2) - 1])/2
    Q2 = medianFinder(sorted(arr), len(arr))
    if len(arr) % 2 == 1:
        L = sorted(arr)[:len(arr)//2]
        U = sorted(arr)[(len(arr)//2)+1:]
    else:
        L = sorted(arr)[:len(arr)//2]
        U = sorted(arr)[len(arr)//2:]
    Q1 = medianFinder(L, len(L))
    Q3 = medianFinder(U, len(U))
    return list(map(int, [Q1, Q2, Q3]))

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    l = []
    for n, f in sorted(zip(values, freqs), key=lambda x:x[0]):
        l.extend([n]*f)
    quarts = quartiles(l)
    
    return round(quarts[2] - quarts[0], 1)
        

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    print(f'{interQuartile(val, freq):.1f}')

