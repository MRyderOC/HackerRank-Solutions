#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    mins, maxs = 0, 0
    base_min, base_max = scores[0], scores[0]
    for i in range(1, len(scores)):
        if scores[i] < base_min:
            mins += 1
            base_min = scores[i]
        elif scores[i] > base_max:
            maxs += 1
            base_max = scores[i]

    return [maxs, mins]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
