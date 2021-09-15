#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack = []
    track_max = []
    out = []
    for operation in operations:
        if operation.startswith('1'):
            x = int(operation.split()[1])
            stack.append(x)
            if not track_max:
                track_max.append(x)
            else:
                if x > track_max[-1]:
                    track_max.append(x)
                else:
                    track_max.append(track_max[-1])
        elif operation.startswith('2'):
            stack.pop()
            track_max.pop()
        elif operation.startswith('3'):
            out.append(track_max[-1])
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

