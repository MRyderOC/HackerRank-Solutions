#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def gameOfThrones(s):
    # Write your code here
    freq = defaultdict(int)
    for item in s:
        freq[item] += 1

    odds = 0
    for v in freq.values():
        if v % 2 == 1:
            odds += 1

    if len(s) % 2 == 1:
        if odds <= 1:
            return "YES"
        return "NO"
    else:
        if odds > 0:
            return "NO"
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
