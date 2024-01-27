#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    colors_map = defaultdict(int)
    for item in b:
        colors_map[item] += 1

    vacants_num = colors_map.get("_", 0)
    if vacants_num != 0:
        colors_map.pop("_")

    for color, occurrence in colors_map.items():
        if occurrence == 1:
            return "NO"

    if vacants_num == 0:
        for i in range(1, len(b) - 2):
            if b[i] != b[i - 1] and b[i] != b[i + 1]:
                return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
