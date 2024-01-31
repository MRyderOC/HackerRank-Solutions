#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    len_s, len_t = len(s), len(t)
    if len_s + len_t <= k:
        return "Yes"

    start_overlap = 0
    for i in range(min(len_s, len_t)):
        if s[i] != t[i]:
            break
        start_overlap += 1

    deletions = len_s - start_overlap
    appends = len_t - start_overlap
    operations_needed = deletions + appends
    if operations_needed <= k and (k - operations_needed) % 2 == 0:
        return "Yes"
    return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
