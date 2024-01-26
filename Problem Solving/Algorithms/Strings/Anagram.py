#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    n = len(s)
    if n % 2 == 1:
        return -1

    half_idx = n // 2
    half1, half2 = Counter(s[:half_idx]), Counter(s[half_idx:])
    count = 0
    for letter, cnt in half1.items():
        count += max(cnt - half2.get(letter, 0), 0)

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
