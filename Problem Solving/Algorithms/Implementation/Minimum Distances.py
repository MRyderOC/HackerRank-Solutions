#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    d = defaultdict(list)
    for i, item in enumerate(a):
        d[item].append(i)

    min_distances = []
    for k, v in d.items():
        if len(v) == 1:
            continue
        min_distances.append(min([v[j+1] - v[j] for j in range(len(v) - 1)]))

    if min_distances:
        return min(min_distances)
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
