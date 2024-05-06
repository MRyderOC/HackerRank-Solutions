#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def makingAnagrams(s1, s2):
    # Write your code here
    f1 = defaultdict(int)
    for item in s1:
        f1[item] += 1

    f2 = defaultdict(int)
    for item in s2:
        f2[item] += 1

    f_intersect = set(f1.keys()).intersection(f2.keys())
    min_intersect_sum = sum(
        2 * min(f1[item], f2[item])
        for item in f_intersect)

    return len(s1) + len(s2) - min_intersect_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
