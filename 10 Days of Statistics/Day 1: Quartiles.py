import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
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
    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

