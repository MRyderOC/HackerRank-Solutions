#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    triplets_count = 0
    count_map = defaultdict(int)
    for item in arr:
        count_map[item] += 1

    for k, v in count_map.items():
        k_plus_d = count_map.get(k + d, 0)
        k_plus_2d = count_map.get(k + (2 * d), 0)
        triplets_count += (v * k_plus_d * k_plus_2d)

    return triplets_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
