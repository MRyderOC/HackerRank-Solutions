#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    # Write your code here
    letter_map = {ascii_lowercase[i]: i for i in range(26)}

    seen = [0] * 26
    for rock in arr:
        for char in set(rock):
            seen[letter_map[char]] += 1

    count = 0
    num_of_rocks = len(arr)
    for s in seen:
        if s == num_of_rocks:
            count += 1

    return count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
