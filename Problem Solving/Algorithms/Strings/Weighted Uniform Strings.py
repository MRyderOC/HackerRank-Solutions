#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#


def weightedUniformStrings(s, queries):
    # Write your code here
    weight_map = {
        ch: i + 1
        for i, ch in enumerate(ascii_lowercase)
    }

    track_char, track_weight = "", 0
    uniform_weights = set()
    for ch in s:
        if track_char != ch:
            track_char = ch
            track_weight = weight_map[ch]
        else:
            track_weight += weight_map[ch]

        uniform_weights.add(track_weight)

    return [
        "Yes" if item in uniform_weights else "No"
        for item in queries
    ]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
